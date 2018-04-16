#coding=utf-8
import sys
import math

tsy='请输入一个数字：'
tsy=tsy.decode('utf-8').encode('gb2312')
x = input(tsy)

if x > 0:
    print u'您输入的是正数！'
else:
    print (u'您输入的不是正数。')


tsy2='请输入圆的半径：'
tsy2=tsy2.decode('utf-8').encode('gb2312')
r = input(tsy2)

if r > 0:
    area = math.pi * r * r
    print area

