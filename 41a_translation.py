inp1 = list(input())
inp2 = list(input())

for i in range(len(inp1)):
    if (inp1[i] != inp2[len(inp2)-i-1]):
        print('NO')
        exit()

print('YES')
