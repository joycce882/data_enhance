import os
import random
import shutil

# 设置路径
folder_A = 'F:\数据集\苗+庆数据集\line'  # 请将"path_to_folder_A"替换为A文件夹的实际路径
dealed_data_folder = os.path.join(os.path.dirname(folder_A), 'dealed_data')

# 创建dealed_data文件夹
os.makedirs(dealed_data_folder, exist_ok=True)

# 获取B和C文件夹的路径
folder_B = os.path.join(folder_A, '0')
folder_C = os.path.join(folder_A, '1')

# 创建train和test文件夹以及相对应的0和1文件夹
train_folder = os.path.join(dealed_data_folder, 'train')
test_folder = os.path.join(dealed_data_folder, 'test')
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)
train_folder_0 = os.path.join(train_folder, '0')
train_folder_1 = os.path.join(train_folder, '1')
test_folder_0 = os.path.join(test_folder, '0')
test_folder_1 = os.path.join(test_folder, '1')
os.makedirs(train_folder_0, exist_ok=True)
os.makedirs(train_folder_1, exist_ok=True)
os.makedirs(test_folder_0, exist_ok=True)
os.makedirs(test_folder_1, exist_ok=True)

# 获取B文件夹中的所有图片文件
image_files_B = [f for f in os.listdir(folder_B) if f.endswith('.jpg') or f.endswith('.png')]

# 获取C文件夹中的所有图片文件
image_files_C = [f for f in os.listdir(folder_C) if f.endswith('.jpg') or f.endswith('.png')]

# 打乱两个文件夹的图片文件列表
random.shuffle(image_files_B)
random.shuffle(image_files_C)

# 计算划分比例
total_files_B = len(image_files_B)
total_files_C = len(image_files_C)

train_ratio = 0.7  # 3:7划分比例
num_train_B = int(total_files_B * train_ratio)
num_train_C = int(total_files_C * train_ratio)

# 将B文件夹的文件复制到train文件夹下的0文件夹
for file in image_files_B[:num_train_B]:
    source_path = os.path.join(folder_B, file)
    destination_path = os.path.join(train_folder_0, file)
    shutil.copyfile(source_path, destination_path)

# 将B文件夹的文件复制到test文件夹
for file in image_files_B[num_train_B:]:
    source_path = os.path.join(folder_B, file)
    destination_path = os.path.join(test_folder_0, file)
    shutil.copyfile(source_path, destination_path)

# 将C文件夹的文件复制到train文件夹
for file in image_files_C[:num_train_C]:
    source_path = os.path.join(folder_C, file)
    destination_path = os.path.join(train_folder_1, file)
    shutil.copyfile(source_path, destination_path)

# 将C文件夹的文件复制到test文件夹
for file in image_files_C[num_train_C:]:
    source_path = os.path.join(folder_C, file)
    destination_path = os.path.join(test_folder_1, file)
    shutil.copyfile(source_path, destination_path)

print("数据集划分完成，结果存放在dealed_data文件夹中的train和test子文件夹中。")
