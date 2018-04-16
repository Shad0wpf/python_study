#coding=utf-8

import os


# 判断文件是否存在
print(os.path.exists('D:\\Code\\Python'))
print(os.path.exists('D:\\Code\\Python2'))

# 重命名文件
# os.rename('D:\\Code\Python\\14_test.txt','D:\\Code\Python\\14_file.txt')

# 返回文件属性
stats  = os.stat('D:\\Code\Python\\14_file.txt')
print(stats)

# 获取文件路径
file_dir = os.path.dirname('D:\\Code\Python\\14_file.txt')
print(file_dir)

# 获取文件路径及文件名
file_dir2 = os.path.dirname('D:\\Code\Python\\14_file.txt')
print(os.path.split(file_dir2))



# 文件复制

# import shutil
# shutil.copyfile('D:\\Code\Python\\14_test.txt','D:\\Code\Python\\14_file.txt')

# 文件重命名
# filename = 'D:\\Code\Python\\14_file.txt'
# rename = 'D:\\Code\Python\\14_test.txt'

# file_list = os.listdir('D:\\Code\Python\\')

# if os.path.basename(filename) in file_list:
#     while os.path.basename(rename) in file_list:
#         choice = input('Have same file, Continue?(Y/N)')
#         if choice in ['Y','y']:
#             rename = ('Please input new filename:')
#         else:
#             break
#     else:
#         os.rename(filename,rename)
#         print("File name changed!")
# else:
#     print("File not exist!")

# os.path.splitext()


# 比较文件内容
import difflib
