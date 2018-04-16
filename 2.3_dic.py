#coding=utf-8

#定义一个字典

dic1 = {"a":"学习Python","b":"学习Java", "c":"学习C#"}

#输入查询关键字进行字典的查询
word = str(raw_input("请输入要查询的关键字（a-d）："))

print word

# while word >= 'a' and word <= "f":
while 'a' <= word <= "f":
    print "查询结果：",dic1[word]
    word = raw_input("请输入要查询的关键字（a-d）：")

