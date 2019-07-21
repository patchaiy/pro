def number(numi):
    x=0
    for i in range(0,len(numi)):
        s1=numi[0:i]+numi[i+1::]
        if(int(s1)%8==0):
            x=1
            break
    if(x==1):
        print("yes")
    else:
        print("no")
numi=input()
number(numi)
