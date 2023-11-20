inp = list(input())
count_cap = 0
count_small = 0

out = "".join(inp)

for i in range(len(inp)):
    if inp[i].isupper():
        count_cap += 1
    else:
        count_small += 1

if count_cap > count_small:
    out = out.upper()
else:
    out = out.lower()

print(out)
