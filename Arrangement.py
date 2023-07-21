column_number = int(input())
column_height = [int(input()) for _ in range(column_number)]

average = sum(column_height) // len(column_height)

i_sum = sum(max(0, average - i) for i in column_height)

print(i_sum)
