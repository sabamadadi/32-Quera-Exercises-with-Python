matrix = [list(map(int, input().split())) for _ in range(4)]

max_values = [max(row) for row in matrix]
max_index = max_values.index(max(max_values)) + 1

print(max_index)
