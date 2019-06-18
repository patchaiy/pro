def  sumOfAP(a,  d,  n): 
  sum = (n / 2) * (2 * a + (n - 1) * d) 
  return sum  
a, d, n = [int(a) for a in input().split()] 
print(sumOfAP(a, d, n)) 
  
