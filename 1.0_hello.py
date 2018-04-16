# #coding=utf-8

# print "Hello World"

# if True:
#     print 'I am Ture4'
#     print 'I am in a if body'



# class A():
#     '''
#     doc string of A
#     '''
# print A.__doc__


#变量的引号
# a = 'string a\n'
# b = "string b\n"
# c = '\''     使用\转义
# d = '''aaa
# bbb'''


#数组
# example_list = ['a',1,2,3,4,5]
# print example_list[0],example_list[:2],example_list[-1]

#元组
# example_tuple = (1,2,3)
# print example_tuple
# print example_tuple[0]

# print type((1)),type((1,))

# #条件语句
# flag = "RAA"
# if flag == 'SA':
#     print 'open'
# elif flag == 'R' or flag == 'RA':
#     print 'closed'
# else:
#     print 'get packet with flag',str(flag)

# #列表
# iplist = '''#127.0.0.1
# 192.168.1.1'''.split('\n')
# print iplist
# #删除#开头
# for ip in iplist:
#     if ip.startswith('#'):
#         iplist.remove(ip)
# print iplist

# # continue, break

# for i in range(100):
#     if i%2 == 0:
#         continue
#     if i == 21:
#         break
#     print i

# #死循环
# while True:
#     pass

# 函数

def foo(a,b):
    return a+b

print foo(1,2)
print foo('a','b')

