#coding=utf-8

score = [56,65,67,89,90,98,56,87,97,76]

y = 0
l = 0
z = 0
c = 0

for fs in score:
    print fs
    if fs >= 90:
        y +=1
    elif 80 <= fs < 90:
        l +=1
    elif 70<= fs <80:
        z +=1
    else:
        c +=1
print y,l,z,c

zgf = max(score)
zdf = min(score)
print zgf
print zdf

sl = len(score)
zf = sum(score)
pjf = zf/sl

print pjf