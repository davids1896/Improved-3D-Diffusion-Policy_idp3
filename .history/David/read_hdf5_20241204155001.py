import h5py
import numpy as np

file_path = '/home/davids1896/David/data/idp3_data/raw_data_example/0.h5'

with h5py.File(file_path, 'r') as f:
    # 读取数据集内容
    action_data = f['action'][:]
    env_qpos_data = f['env_qpos_proprioception'][:]
    
    # 查看第一个样本
    print("Action data (first sample):")
    print(action_data[0])  # 查看第一个动作数据
    
    print("\nEnv qpos data (first sample):")
    print(env_qpos_data[0])  # 查看第一个环境的传感器数据
    
    # 检查数据的统计信息
    print("\nAction data statistics:")
    print("Min:", np.min(action_data), "Max:", np.max(action_data), "Mean:", np.mean(action_data))
    
    print("\nEnv qpos data statistics:")
    print("Min:", np.min(env_qpos_data), "Max:", np.max(env_qpos_data), "Mean:", np.mean(env_qpos_data))
