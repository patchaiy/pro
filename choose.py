numi=int(input())
l1=[]
m1=len(str(numi))
s1=0
for _ in range(m1):
	s1+=9
for i in range(numi-s1,numi):
	r=0
	d=i
	while d>0:
		r+=(d%10)
		d=d//10
	if r+i==numi:
		l1.append(i)
print(len(l1),*l1,sep='\n')
