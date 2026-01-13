n, k = map(int, input().split())
a=list(map(int,input().split()))
sk=a[k-1]
c=0
for x in a:
    if x>= sk and x>0:
        c+=1
        
print(c)
    
