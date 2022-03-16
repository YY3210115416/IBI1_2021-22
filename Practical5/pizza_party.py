#Initial
p = 1
n = 0
#When there are less than 64 pieces of cake, we need to continue cutting.
while p < 64:
 n = n + 1
 p = (n*n+n+2)/2
 print("n =", n, "p =", p)
 #When there are enough pieces of cake, we stop cutting.
 if p >= 64:
  print("n =", n, "p =", p,)
  break
 
 
