p3=int(input())
q3=list(map(int,input().split()))
a3i=0
b3=0
q3.sort(reverse=True)
for i in q3:
  q3=a3i+i
  if b3>q3:
    a3i=q3
  else:
    a3i=b3
    b3=q3
print(a3i,b3)
