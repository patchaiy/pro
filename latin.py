si=input()
minimum3=len(si)
i=0
while(i<minimum3):
    m3=0
    k3=0
    for j in range(len(si)):
        k3+=1
        if(si[i]==si[j]):
            if(k3>m3):
                m3=k3
            k3=0
        if(k3>minimum3):
            break
    if(k3>m3):
        m3=k3
    if(m3<minimum3):
        minimum3=m3
    i+=1
print(minimum3)
