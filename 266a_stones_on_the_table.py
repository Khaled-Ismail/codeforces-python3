inp_len = int(input())
inp = list(input())
count = 0

for i in range (1, len(inp)):
    if inp[i] == inp[i-1]:
        count += 1
print(count)
