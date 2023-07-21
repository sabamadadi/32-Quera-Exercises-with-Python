n = int(input())
num = [int(i) for i in input().split()]
num.sort(reverse=True)
ans = []
while len(num) >= 2:
    ans.append(num[0])
    ans.append(num[-1])
    num = num[1: -1]
if len(num) > 0:
    ans.append(num[0])

print(" ".join(str(x) for x in ans))