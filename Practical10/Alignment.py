import re
import pandas as pd

file="BLOSUM.xlsx"
score=pd.read_excel(file)
print(score.iloc['A','T'])

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


match1=0
score1=0
for i in range(len(hum_list)):
    X=hum_list[i]
    Y=mou_list[i]
    Z=score.loc[score['First']==X,Y]
    value=int(Z)
    score1+=value
    if hum_list[i]==mou_list[i]:
        match1=match1+1
    else:
        match1=match1
percentage1=match1/len(hum_list)
print(match1) 
print(percentage1)
print(score1)
   
match2=0
for i in range(len(hum_list)):
    if hum_list[i]==ran_list[i]:
        match2=match2+1
    else:
        match2=match2
percentage2=match2/len(hum_list)
print(match2) 
print(percentage2)

match3=0
for i in range(len(hum_list)):
    if ran_list[i]==mou_list[i]:
        match3=match3+1
    else:
        match3=match3
percentage3=match3/len(hum_list)
print(match3) 
print(percentage3)

A=[]
for i in range(23):
    if score.iloc[i,0]=="A":
        A.append(True)
    else:
        A.append(False)

A_data=score.iloc[A]

B=[]
for i in range(23):
    if A_data.iloc[i,0]=="A":
        B.append(True)
    else:
        B.append(False)
B_data=A_data.iloc[B]
print(B_data)