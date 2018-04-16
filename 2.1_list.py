#coding=utf-8

data_goo = []

#循环7次，输入7个数据放入列表中
for inte in range(7):
    x = input("请输入第"+str(inte+1)+"个元素：")
    data_goo = data_goo + [x]
print "排序前：",data_goo

data_goo.sort()
print "排序后：",data_goo