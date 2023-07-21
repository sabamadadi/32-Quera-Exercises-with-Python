i1,i2=input().split()
i1=int(i1)
tempt=0
for i in i2:
    tempt*=2
    if i=='R':
        tempt+=0
    else:
        tempt+=1
for i in range(i1-len(i2)):
    tempt+=2**(i1-i)
print(tempt+1)