k = int(input())
ramz = input()
m = [input() for _ in range(k)]
s = sum(9 - m[i].index(ramz[i]) if m[i].index(ramz[i]) > 4 else m[i].index(ramz[i]) for i in range(k))
print(s)
