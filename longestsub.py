tp=input()
lii=list(map(int,input().split()))
maximum=0
i=0
while(i<len(lii)-1):
    count=0
    while(i<len(lii)-1 and lii[i]<lii[i+1]):
        count+=1
        i+=1
    if(count>maximum):
        maximum=count
    i+=1
print(maximum+1)
