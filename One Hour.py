a, b = map(int, input().split())
a = ((a - 12) % 12) * (a > 12 and a < 24) + (12 - a) * (a < 12 and a != 0) + (0) * (a == 24 or a == 0)
b = (60 - b) * ((b != 0) and ((a != 6) or (a == 0)))
h = str(a).zfill(2)
m = str(b).zfill(2)
print(h + ":" + m)