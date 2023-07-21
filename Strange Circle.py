n, k = map(int, input().split())

hasani = 1
r = 0

while True:
    hasani += k
    hasani %= n

    r += 1

    if hasani == 1:
        break

print(r)
