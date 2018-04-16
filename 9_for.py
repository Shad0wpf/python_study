#coding=utf-8


score = [23, 56, 78, 89,34, 97, 87, 79]

# 写法一
# avg = sum(score)/len(score)
# print u'平均分是：',avg

# 写法二
# zf = 0
# rs = 0
# for i in score:
#     zf = zf + i
#     rs = rs + 1
# avg = zf / rs
# print u'平均分是：',avg

# 写法三
# zf = 0
# rs = 0
# for i in range(len(score)):
#     print score[i]
#     zf += score[i]
# avg = zf/len(score)
# print u'平均分是：',avg

# 求 1 + 1/2 + 1/3 + ... + 1/n

# s = 0.0
# n = int(input('Please input a number:'))

# for i in range(1, n+1, 1):
#     s = s + 1.0/i
# print s


# 乘法表

# for x in range(1,10,1):
#     for y in range (1,x+1,1):
#         print y,'*',x,'=',x*y,"\t",
#     print '\n'


# 数字排序

# score = [34, 45, 78, 234, 89, 345]
print u'排序前:',score
print u'排序后:',sorted(score)

#使用for
for i in range(len(score)-1):
    min_score = score[i]
    k = i
    for j in range(i+1,len(score),1):
        if min_score > score[j]:
            min_score = score[j]
            k = j
    score[i],score[k] = score[k],score[i]

print u'排序前:',score


# 求200内能被17整除的最大正整数
for i in range(200,1,-1):
    if i % 17 == 0:
        print i
        break

# 判断是否为素数
# x = int(input('Please input a number:'))

# for i in range(2,x,1):
#     if x % i == 0:
#         break
# if i == x - 1:
#     print x,u'是素数'
# else:
#     print x,u'不是素数'


# 200以内所有能被17整除的正整数
s = 0
for i in range(1,201,1):
    if i % 17 != 0:
        continue
    print i
    s += 1
print u'共有数量：',s