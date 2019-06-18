def hcfnaive(a,b): 
 if(b==0): 
  return a 
 else: 
  return hcfnaive(b,a%b) 
a,b = [int(a) for a in input().split()] 
print (end="") 
print (hcfnaive(a,b)) 
