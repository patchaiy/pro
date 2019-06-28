def  sumOfAP(N,  A,  D): 
  sum = (N/ 2) * (2 * A + (N - 1) * D) 
  return sum  
N, A, D = [int(N) for N in input().split()] 
print(sumOfAP(N, A, D)) 
  
