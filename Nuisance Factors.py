n = int(input())
sum = 0
count = 0

for i in range(1, n+1):
    for j in range(1, int(i**0.5)+1):
        if i % j == 0:
            sum += j
            count += 1
            if j != i//j:
                sum += i//j
                count += 1

print(count, sum)