result = list(map(lambda a, b: a - b, [1, 1, 2, 2, 2, 8], list(map(int, input().split()))))
print(*result, end=" ")