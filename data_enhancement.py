# 对较少的数据集进行数据增强
import os
# 翻转
from PIL import Image, ImageOps, ImageFilter

file_path = r'F:\数据集\苗+庆数据集\enhancement_data\train\1'
file_list = os.listdir(file_path)

for file in file_list:
    img = Image.open(os.path.join(file_path, file))
    img = ImageOps.flip(img)
    img.save(os.path.join(file_path, 'enhancement_flip' + file))
# 旋转
for file in file_list:
    img = Image.open(os.path.join(file_path, file))
    img = img.rotate(90)
    img.save(os.path.join(file_path, 'enhancement_rotate' + file))
# 模糊
for file in file_list:
    img = Image.open(os.path.join(file_path, file))
    img = img.filter(ImageFilter.BLUR)
    img.save(os.path.join(file_path, 'enhancement_blur' + file))
# 锐化
for file in file_list:
    img = Image.open(os.path.join(file_path, file))
    img = img.filter(ImageFilter.SHARPEN)
    img.save(os.path.join(file_path, 'enhancement_sharpen' + file))
