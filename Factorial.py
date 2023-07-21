def factorial(n): return (n and (n * factorial(n-1))) or 1
print(factorial(int(input())))