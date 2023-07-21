s = input()
ans = 1
for i in range(len(s)):
    if s[i] in ['L', 'F', 'T', 'D']:
        ans *= 2
print(ans)
