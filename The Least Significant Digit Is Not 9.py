a = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]

def javab(n):
    if n < 10:
        return a[n]
    if ((n // 10) % 10) % 2 == 0:
        return (6 * javab(n // 5) * a[n % 10]) % 10
    else:
        return (4 * javab(n // 5) * a[n % 10]) % 10

n = int(input())
print(javab(n))
