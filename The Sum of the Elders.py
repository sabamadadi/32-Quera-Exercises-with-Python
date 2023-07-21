a = input()
command = input()
b = input()
operations = {
    '+': lambda x, y: x[:len(x)-len(y)] + str(int(x[len(x)-len(y)])+1) + x[len(x)-len(y)+1:],
    '*': lambda x, y: x + '0' * (len(y)-1)
}
a = operations.get(command, lambda x, y: x)(*(sorted([a, b], key=len, reverse=True)))
print(a)