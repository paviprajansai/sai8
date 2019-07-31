n11,k11=map(int,input().split())
c11=0
l=list(map(int,input().split()))
for i in range(0,len(l)):
	if l[i]==k11:
		c11=c11+1
print(c11)
