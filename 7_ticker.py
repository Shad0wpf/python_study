#coding=utf-8

tsy1 = '请问您需要乘坐多少站？'
tsy2 = '您需要多买几张票？'
tsy1 = tsy1.decode('utf-8').encode('gb2312')
tsy2 = tsy2.decode('utf-8').encode('gb2312')

zz = input(tsy1)
rs = input(tsy2)

if rs <=0 or zz <=0:
    print u'输入错入，请重新输入：'
    zz = input(tsy1)
    rs = input(tsy2)


if zz <= 4:
    pj = 3
    zj = pj * rs
elif zz <=9:
    pj = 4
    zj = pj * rs
else:
    pj = 5
    zj = pj * rs

print u'共需付款',zj,u'元。'