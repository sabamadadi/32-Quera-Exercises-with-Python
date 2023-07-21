n = int(input())
print("\n".join(map(lambda i: " ".join(map(str, map(lambda j: i*j, range(1, n+1)))), range(1, n+1))))