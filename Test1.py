a=int(input());
d=1;
c=int(a/2)-1;
b=list(map(int,input().split()));
for i in range(int(a/2)):
    i=i+1;
    if(d==1):

        if(b[i-1]<b[i] and b[i]>b[i+1]):
            print(b[i]);
            d=2;
