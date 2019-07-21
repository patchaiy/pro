numi,k3=map(int,input().split())
l3 = list(map(int,input().split()))
count = 0
for i in range(0,len(l3)):
    if (l3[i]+k3)<=5:
        count+=1
print(count//3)
