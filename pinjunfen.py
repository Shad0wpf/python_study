#coding=utf-8


score = {'zhang':67, "li":89, "wang":93, "zhao":95, "wu":76}

min_score = 100
max_score = 0
n = 0
sum_score = 0
for i in score.keys():
    if score[i] > max_score:
        max_score = score[i]
    if score[i] < min_score:
        min_score = score[i]
    n += 1
    sum_score = sum_score + score[i]

avg_score = sum_score/n

s1 = "最高分是:"+str(max_score)
print (s1.encode('gb2312'))
s2 =  "最低分是:"+str(min_score)
print (s2.encode('gb2312'))
print (u"最低分是:"+str(min_score))
s3 = "员工共有"+str(n)+"人，平均分是:"+str(avg_score)+"分。"
print (s3.encode('gb2312'))


