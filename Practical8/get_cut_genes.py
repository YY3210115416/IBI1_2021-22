import re
seq=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') 

a=seq.read()
a=re.sub(r"\n","",a)
a=a+">"

genes=re.findall(r'](.+?)>',a)
names=re.findall(r'gene:(.+?) gene',a)  

seq_needed=[] 
order=[]
yy=0

for i in genes:
    if i.find('GAATTC')>=0:
        order.append(yy)
        seq_needed.append(i)
    yy=yy+1

names1=[]
for i in order:
    names1.append(names[i])

lengths=[]
for i in seq_needed:
    length=len(i)
    lengths.append(length)

new=open('cut_genes.fa','w')
for i in range(len(order)):
    new.write(">")
    new.write(names1[i])
    new.write(" ")
    new.write(str(lengths[i]))
    new.write("\n")
    new.write(seq_needed[i])
    new.write("\n")
new.close()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    







      
