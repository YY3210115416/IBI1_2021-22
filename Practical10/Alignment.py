import re

z=open('DLX5_human.fa') 
x=open('DLX5_mouse.fa') 
y=open('RandomSeq.fa') 
u=z.read()
v=x.read()
w=y.read()
u=re.sub(r"\n","",u)
v=re.sub(r"\n","",v)
w=re.sub(r"\n","",w)
u=u+">"
v=v+">"
w=w+">"

hum=re.findall(r'(MTG.+?)>',u)
mou=re.findall(r'(MTG.+?)>',v)
ran=re.findall(r'(GDY.+?)>',w)
print(hum)
print(mou)
print(ran)

hum_list=list(hum[0])
mou_list=list(mou[0])
ran_list=list(ran[0])

a=len(hum)
b=len(mou)
c=len(ran)

score1=0
for i in range(len(hum_list)):
    if hum_list[i]==mou_list[i]:
        score1=score1+1
    else:
        score1=score1
percentage1=score1/len(hum_list)
print(score1) 
print(percentage1)
   
score2=0
for i in range(len(hum_list)):
    if hum_list[i]==ran_list[i]:
        score2=score2+1
    else:
        score2=score2
percentage2=score2/len(hum_list)
print(score2) 
print(percentage2)

score3=0
for i in range(len(hum_list)):
    if ran_list[i]==mou_list[i]:
        score3=score3+1
    else:
        score3=score3
percentage3=score3/len(hum_list)
print(score3) 
print(percentage3)