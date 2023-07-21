def multiply(x, res, res_size):
    carry = 0
    for i in range(res_size):
        prod = res[i] * x + carry
        res[i] = prod % 10
        carry = prod // 10
    while (carry):
        res[res_size] = carry % 10
        carry = carry // 10
        res_size += 1
    return res_size

def factorial(n, birth):
    MAX = 1000
    res = [0] * MAX
    counter = 0
    res[0] = 1
    res_size = 1
    for x in range(2, n+1):
        res_size = multiply(x, res, res_size)
    for i in range(res_size-1, -1, -1):
        if (res[i] == birth):
            counter += 1
    print(counter)

n, birth = map(int, input().split())
factorial(n, birth)