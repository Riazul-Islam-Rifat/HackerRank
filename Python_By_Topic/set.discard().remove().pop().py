length=int(input())
inpt_set=set(map(int,input().split()))
operations=int(input())
for item in range(operations):
    operation=input()
    if operation[0]=='p':
        inpt_set.pop()
    elif operation[0]=='r':
        l=operation.split()
        oprtn,val=l
        inpt_set.remove(int(val))
    elif operation[0]=='d':
        l=operation.split()
        oprtn,val=l
        inpt_set.discard(int(val))

if len(inpt_set)==0:
    print(0)
else:
    sum=0
    for item in inpt_set:
        sum=sum+item
    print(sum)