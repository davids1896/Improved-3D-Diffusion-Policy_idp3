import h5py

def read_h5_file(file_path):
    try:
        # 打开 HDF5 文件
        with h5py.File(file_path, 'r') as h5_file:
            print("File Structure:")

            # 打印文件结构
            def print_structure(name, obj):
                if isinstance(obj, h5py.Group):
                    print(f"[Group] {name}")
                elif isinstance(obj, h5py.Dataset):
                    print(f"[Dataset] {name}, shape: {obj.shape}, dtype: {obj.dtype}")

            h5_file.visititems(print_structure)

            # 示例：读取特定数据集内容
            print("\nSample Data:")
            for key in h5_file.keys():
                try:
                    dataset = h5_file[key]
                    if isinstance(dataset, h5py.Dataset):
                        print(f"Dataset: {key}, Data: {dataset[()]}")
                except Exception as e:
                    print(f"Error reading {key}: {e}")

    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = "/home/davids1896/David/data/idp3_data/raw_data_example/0.h5"
    read_h5_file(file_path)
