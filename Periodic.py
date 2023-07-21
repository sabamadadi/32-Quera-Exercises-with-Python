n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

sum = 0
for i in range(1, n-1):
    for x in range(1, m-1):
        if ((a[i][x] > a[i][x-1] and a[i][x] > a[i][x+1] and a[i][x] < a[i-1][x] and a[i][x] < a[i+1][x]) or
            (a[i][x] < a[i][x-1] and a[i][x] < a[i][x+1] and a[i][x] > a[i-1][x] and a[i][x] > a[i+1][x])):
            sum += 1

print(sum)
