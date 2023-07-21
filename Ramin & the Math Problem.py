from math import isqrt

n = int(input())
m = [str(isqrt(r) - isqrt(l) + (1 if isqrt(l) * isqrt(l) == l else 0)) for _ in range(n) for l, r in [map(int, input().split())]]

print("\n".join(m))
