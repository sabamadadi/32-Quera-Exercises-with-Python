def recursive_sum(n): return n * (len(n) == 1) or recursive_sum(str(sum(map(int, list(n)))))
print(recursive_sum(input()))