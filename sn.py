nni,mm=map(int,input().split())
d=[]
for _ in range(nni):
	d.append(sorted(list(map(int,input().split()))))
for i in range(nni-1):
	for j in range(mm):
		for k in range(nni-i):
			if(d[i][j]>d[i+k][j]):
				d[i][j],d[i+k][j]=d[i+k][j],d[i][j]
for i in d:
	print(*i,sep=' ')       
