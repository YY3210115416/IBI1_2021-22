import re


file=open("go_obo.xml") 
go=file.read()

term=re.findall(r'GO:\d+',go)

num=len(term)
print(num)