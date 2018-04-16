#coding=utf-8


# 写通讯录
# f = open('D:\\Code\\Python\contact.txt','w')

# f.write('姓名'+'\t性别'+'\t电话'+'\t\t地址'+'\n')
flag  = 'Y'


# while flag.lower() == 'y' or flag == '':
#     name = input('请输入姓名：')
#     sex = input('请输入性别：')
#     phone = input('请输入电话号码：')
#     address = input('请输入联系地址：')
#     s = name + '\t' + sex + '\t' + phone + '\t' + address + '\n'
#     f.write(s)

#     flag = input('是否继续输入？（Y/n）')
# f.close()

# 读通讯录

# f = open('D:\Code\Python\contact.txt','r')

# while True:
#     line = f.readline()
#     if line == '':
#         break
#     print(line)
# f.close()


# 写文件、然后读取文件长度
# s = 'a1@中国\n'

# f = open('D:\\Code\\Python\\12_test.txt','w')

# f.write(s)
# f.seek(0,2)

# length = f.tell()
# print(length)

# 读取文件5个字节

f = open('D:\Code\Python\contact.txt','r')
text = f.read(5)
print(text)
print(len(text))
f.close()
