n = int(input())
tm = list(map(int, input().split()))
count = 0
tmp = 0
for i in range(1, 1001):
    for j in range(n):
        if i % tm[j] == 0:
            count += 1
    if count == n:
        tmp += 1
    count = 0
print(tmp)
