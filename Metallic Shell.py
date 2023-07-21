t, w = map(int, input().split())

distance = t / (2 * (1 - 0.5 ** w))
print(f"{distance:.4f}")
