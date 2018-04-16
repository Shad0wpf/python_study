#coding=utf-8

import os


path1 = 'D:\\Code'


# 列当前目录文件
# print(os.listdir(path1))


# for i in os.listdir(path1):
#     path2 = os.path.join(path1,i)
#     if os.path.isfile(path2):
#         print(i,'\n')
#     else:
#         pass

# 列当前目录及子目录文件

def list_dir(path):
    for i in os.listdir(path):
        path2 = os.path.join(path,i)
        if os.path.isdir(path2):
            list_dir(path2)
        else:
            print(path2)

if __name__ == "__main__":
    print("************** Call ListDir")
    list_dir(path1)