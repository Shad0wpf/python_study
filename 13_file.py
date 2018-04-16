#coding=utf-8

# 把国替换成央，把9替换成8,末尾添加人民政府

# f = open('D:\\Code\\Python\\13_file.txt','r+')

# print(f.seek(0,2))

# f.seek(4)
# f.write('O')
# f.seek(15)
# f.write('8')

# f.seek(0,2)
# f.write('\nPython')


# pack()方法

# import struct
# n = 100
# x = 80.5
# b = True
# s = 'a1@中国'

# sn = struct.pack('if?',n,x,b,s)

# print(sn)
# f = open('D:\\Code\\Python\\13_file2.txt','wb')
# f.write(sn)
# # f.write(s)
# f.close()


# pickle方法

# import pickle

# f = open('D:\\Code\\Python\\13_file2.dat','wb')

# n = 100
# x = 80.5
# b = True
# s = 'a1@中国'
# lst = [1,3,54,'342','fasdf',3452]
# tup = ('sdf','23452',234234)

# try:
#     pickle.dump(n,f)
#     pickle.dump(x,f)
#     pickle.dump(b,f)
#     pickle.dump(s,f)
#     pickle.dump(lst,f)
#     pickle.dump(tup,f)
# except:
#     print("写入文件异常")

# f.close()

# # 读取二进制文件

# import pickle

# f = open('D:\\Code\\Python\\13_file2.txt','rb')
# n = pickle.load(f)

# print(n)
# print(len(pickle.loads))
# i=0
# while i < 5:
#     x = pickle.load(f)
#     print(x)
#     i += 1
# f.close()


# 复制文件

# def FileCopy(tar_file, res_file):
#     try:
#         f1 = open(res_file, 'rb')
#         f2 = open(tar_file, 'wb')
#     except:
#         print('打开文件异常！')
#         return -1
#     s = f1.read()
#     f2.write(s)
#     f2.close()
#     return 0

# FileCopy('D:\\Code\\Python\\13_file3.txt','D:\\Code\\Python\\13_file2.txt')

# 复制二进制文件
# import pickle

# def FileCopy(tar_file, res_file):
#     try:
#         f1 = open(res_file, 'rb')
#         f2 = open(tar_file, 'wb')
#     except:
#         print('打开文件异常！')
#         return -1
#     s = pickle.load(f1)
#     pickle.dump(s,f2)
#     f2.close()
#     return 0

# FileCopy('D:\\Code\\Python\\13_file3.dat','D:\\Code\\Python\\13_file2.dat')


# 统计文本中大写字母、小写字母、数字字符及其它字符出现的次数

f = open('D:\\Code\\Python\\13_file.txt','r+')
nA = 0
na = 0
nd = 0
no = 0

while True:
    x = f.read()
    if x == '':
        break
    if x.isupper():
        nA += 1
    elif x.islower():
        na += 1
    elif x.isdigit():
        nd += 1
    else:
        no += 1
f.close()
print(nA)
print(na)
print(nd)
print(no)
