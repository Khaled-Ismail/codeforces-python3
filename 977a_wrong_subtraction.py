inp = input().split(" ")

num = int(inp[0])
dvsr = int(inp[1])

out = num

for i in range (1, dvsr+1):
    if out % 10 == 0:
        out //= 10
    else:
        out -= 1

print(out)
