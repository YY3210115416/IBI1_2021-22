import re

seq=open("cut_genes.fa") 
a=seq.read()
a=a+">"

a=re.sub(r"\n","",a)
sequence=re.findall(r' (.+?)>',a)
#sequence=re.findall(r"[AGCT]{4,}",a)
name=re.findall(r'>(.+?) ',a)  

#print(genes)
#print(names)
number=len(name)
#print(name)
#print(order)

names=[]
for i in range(number):
    names.append(name[i])
#print(names)

print(number)

fragments=[]
for i in sequence:
    cut=i.find('GAATTC')
    fragment=cut+2
    fragments.append(fragment)

print(len(fragments))

filename=input('filename:')
new=open(filename,'w')
for i in range(number):
    new.write(">")
    new.write(names[i])
    new.write(" ")
    new.write(str(fragments[i]))
    new.write("\n")
    new.write(sequence[i])
    new.write("\n")
new.close()
