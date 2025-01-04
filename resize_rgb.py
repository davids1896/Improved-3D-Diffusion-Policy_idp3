import os
from PIL import Image
from tqdm import tqdm

def resize_images_in_episode(episode_dir, target_size=(848, 480)):
    # 原始图像和目标保存路径
    images_dir = os.path.join(episode_dir, "images")
    resized_images_dir = os.path.join(episode_dir, "resized_images")
    
    # 创建保存路径
    os.makedirs(resized_images_dir, exist_ok=True)
    
    # 获取所有图像文件
    image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png'))]
    
    for image_file in tqdm(image_files, desc=f"Resizing images in {episode_dir}"):
        # 图像路径
        input_path = os.path.join(images_dir, image_file)
        output_path = os.path.join(resized_images_dir, image_file)
        
        # 打开、调整大小并保存
        with Image.open(input_path) as img:
            resized_img = img.resize(target_size)
            resized_img.save(output_path)

def main(data_root, target_size=(848, 480)):
    # 获取所有 episode 目录
    episode_dirs = [os.path.join(data_root, d) for d in os.listdir(data_root) if os.path.isdir(os.path.join(data_root, d))]
    
    for episode_dir in tqdm(episode_dirs, desc="Processing all episodes"):
        resize_images_in_episode(episode_dir, target_size)

if __name__ == "__main__":
    # 根目录路径
    data_root = "/mnt/hpfs/baaiei/DavidHong/data/leju/data_new/home/kuavo/rosbag_record/pick-lemon/output_directory_new"
    
    # 目标分辨率
    target_size = (848, 480)
    
    main(data_root, target_size)
