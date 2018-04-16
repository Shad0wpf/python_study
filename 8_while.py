#coding=utf-8



# print u'请输入若干个整数进行求和操作，当输入负数时结束。'

# tsy = u'请输入一个整数:'
# tsy = tsy.encode('gb2312')

# sum = 0
# x = input(tsy)

# while x >= 0:
#     sum = sum + x
#     x = input(tsy) 
# else:
#     sum = sum + x

# print u'和是',sum


# x = 1
# sum = 0
# while x < 101:
#     sum = sum + x
#     x += 1
#     print sum



# list1 = [123, 34, 3424, 345, 657 ,67567,'adf']
# i = 0
# while i < len(list1):
#     print u'列表第',i+1,u'个元素是：',list1[i]
#     i += 1


# tsy2 = u'请输入字符，当输入#号是结束该程序。'
# tsy3 = u'请输入一个字符：'
# tsy3 = tsy3.encode('gb2312')
# tsy4 = u'您输入的字符是：'
# tsy4 = tsy4.encode('gb2312')

# print tsy2.encode('gb2312')
# while True:
#     x = raw_input(tsy3)
#     if x != '#':
#         print tsy4,x
#     else:
#         break


# 求1~100直接能被7整除，但不能被5整除的所有整数。
# i = 1
# while i < 100+1:
#     if (i % 7 == 0) and (i % 5 != 0):
#         print i
#     i += 1


# 求水仙花数（三位的十进制数，各位数字的立方和等于该数本身）
# i = 100
# while i < 1000:
#     gw = int(str(i)[2])
#     sw = int(str(i)[1])
#     bw = int(str(i)[0])
#     if i == gw**3 + sw**3 + bw**3:
#         print i,u'是水仙花数。'
#     i += 1

i = 100
while i < 1000:
    gw = i % 10
    sw = (i % 100)/10
    bw = i / 100
    if i == gw**3 + sw**3 + bw**3:
        print i,u'是水仙花数。'
    i += 1

