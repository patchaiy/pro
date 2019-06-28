def  sumap(N,  A,  D): 
  sum1= (N/ 2) * (2 * A + (N - 1) * D) 
  return sum1  
N, A, D = [int(N) for N in input().split()] 
print(sumap(N, A, D)) 
  
