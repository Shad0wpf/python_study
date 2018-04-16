#coding=utf-8

# 数字求和

# tsy = 
# tsy = tsy.encode('gb2312')
s = input('请输入几个数字，用逗号分割：')

li = s.split(',')
sum = 0 
for i in li:
    sum += float(i)

print('和是：',sum)




