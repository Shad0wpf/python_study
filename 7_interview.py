#coding=utf-8

tsy1 = "请输入你的年龄："
tsy1 = tsy1.encode('gb2312')
tsy2 = "请输入你的专业："
tsy2 = tsy2.encode('gb2312')
tsy3 = "是否是重点大学？"
tsy3 = tsy3.encode('gb2312')

# age = 22
# subject = '软件信息工程'
# college = '非重点大学'

age = input(tsy1)
subject = str(raw_input(tsy2))
college = str(raw_input(tsy3))
subject = subject.decode('gb2312')
college = college.decode('gb2312')

print subject
print college

if (age > 24 and subject == str('软件信息工程').decode('utf-8')) or (college == str('重点大学').decode('utf-8')) or (age < 28 and subject == str('计算机软件').decode('utf-8')):
    print u'恭喜您获得面试资格！'
else:
    print u'抱歉您不符合面试要求。'
