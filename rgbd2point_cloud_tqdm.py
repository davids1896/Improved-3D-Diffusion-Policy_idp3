import os
import numpy as np
import open3d as o3d
from tqdm import tqdm

def rgbd_to_pointcloud(rgb_image, depth_image, intrinsics):
    # 提取内参
    fx, fy, cx, cy = intrinsics['fx'], intrinsics['fy'], intrinsics['cx'], intrinsics['cy']
    height, width = depth_image.shape
    
    # 创建像素网格
    u, v = np.meshgrid(np.arange(width), np.arange(height))
    
    # 计算 3D 坐标
    z = depth_image
    x = (u - cx) * z / fx
    y = (v - cy) * z / fy
    points = np.stack((x, y, z), axis=-1).reshape(-1, 3)
    
    # 获取颜色信息
    colors = rgb_image.reshape(-1, 3) / 255.0  # 归一化到 [0, 1]
    
    # 创建点云对象
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)
    point_cloud.colors = o3d.utility.Vector3dVector(colors)
    
    return point_cloud

def process_episode(episode_dir, intrinsics):
    depth_dir = os.path.join(episode_dir, 'depth_images')
    rgb_dir = os.path.join(episode_dir, 'resized_images')
    
    depth_files = sorted([f for f in os.listdir(depth_dir) if f.endswith('.jpg')])
    rgb_files = sorted([f for f in os.listdir(rgb_dir) if f.endswith('.jpg')])
    
    for depth_file, rgb_file in tqdm(zip(depth_files, rgb_files), total=len(depth_files), desc=f'Processing {episode_dir}'):
        depth_image = o3d.io.read_image(os.path.join(depth_dir, depth_file))
        rgb_image = o3d.io.read_image(os.path.join(rgb_dir, rgb_file))
        
        depth_image = np.asarray(depth_image)
        rgb_image = np.asarray(rgb_image)
        
        point_cloud = rgbd_to_pointcloud(rgb_image, depth_image, intrinsics)
        output_file = os.path.join(episode_dir, 'resized_point_clouds', f'{os.path.splitext(depth_file)[0]}.ply')
        o3d.io.write_point_cloud(output_file, point_cloud)

def main(data_root, intrinsics):
    episode_dirs = [os.path.join(data_root, d) for d in os.listdir(data_root) if os.path.isdir(os.path.join(data_root, d))]
    
    for episode_dir in tqdm(episode_dirs, desc='Processing episodes'):
        os.makedirs(os.path.join(episode_dir, 'resized_point_clouds'), exist_ok=True)
        process_episode(episode_dir, intrinsics)

if __name__ == "__main__":
    data_root = '/mnt/hpfs/baaiei/DavidHong/data/leju/data_new/home/kuavo/rosbag_record/pick-lemon/output_directory_new'
    intrinsics = {'fx': 604.299, 'fy': 603.457, 'cx': 317.093, 'cy': 253.238}
    main(data_root, intrinsics)