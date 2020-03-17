a=int(input());
k=0;
c=[]
amit = list(map(int, input().strip().split(' ')));
for i in range(0,a):
        c[k]=amit.count(amit[i]);
        k=k+1;
c=c.sort();
if(c.count(c[0])>1):
    print("-1")
else:
    print(c[0])