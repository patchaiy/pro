ppi,qq3=input().split()
ppi=int(ppi)
qqi=int(qq3)
s3=''
u3=2
if(ppi+qq3<=3):
    for i in range(0,ppi+qq3):
        if(i%2!=0):
            s3=s3+'0'
        else:
            s3=s3+'1'
else:    
    for i in range(0,ppi+qq3):
        if(i==u3):
            s3=s3+'0'
            if(u3==qq3):
                u3=u3+2
            else:
                u3=u3+3
        else:
            s3=s3+'1'
x=len(s3)-1
if(int(s3[x])==0):
    print('-1') 
elif ppi==1 and qq3==2: 
     print("011")
else:
    print(s3)
