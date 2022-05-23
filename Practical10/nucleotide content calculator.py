#In this function, I use the sequence"AcGtTgCa"as example.
DNA=input('DNA:')
def nucle_feq(DNA):
   A=0
   G=0
   C=0
   T=0
   l=list(DNA)
   for i in l:
       if i== "A":
           A=A+1
       if i== "a":
           A=A+1
       if i== "T":
           T=T+1
       if i=="t":
           T=T+1
       if i=="C":
           C=C+1
       if i=="c":
           C=C+1    
       if i=="G":
           G=G+1
       if i=="g":
           G=G+1   
   A_feq=A/len(l)
   T_feq=T/len(l)
   G_feq=G/len(l)
   C_feq=C/len(l)
   print("A:",A_feq,"T:",T_feq,"G:",G_feq,"C:",C_feq)
   return (A_feq,T_feq,G_feq,C_feq)
nucle_feq(DNA)
#In the example,the percentages of the nucleotides are all 0.25.
