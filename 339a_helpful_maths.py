inp = input().split("+")
out = ""

for i in range(0, len(inp)):
    inp[i] = int(inp[i])

inp.sort()

for i in range(0, len(inp)):
    if i == len(inp) - 1:
        out+=str(inp[i])
    else:
        out+=str(inp[i])+"+"
print(out)
