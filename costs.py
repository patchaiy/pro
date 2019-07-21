n,m=map(int,input().split())
li=[]
for i in range(m):
  li.append(list(map(int,input().split())))
costi=10000000
n1=0
for i in range(m):
  if(li[i][0]==1):
    s=li[i][1]
    c=li[i][2]
    for j in range(i+1,m):
      if(li[j][0]==s):
        s=li[j][1]
        c+=li[j][2]
    if(c<costi and s==n):
      costi=c
      n1+=1
if(n1==0):
  print(-1)
else:
  print(costi)
