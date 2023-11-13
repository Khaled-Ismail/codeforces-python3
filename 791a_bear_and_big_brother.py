inp = input().split()
count = 0
l = 0
b = 0
for i in range(len(inp)):
    inp[i] = int(inp[i])

l = inp[0]
b = inp[1]

if  (l == b):
    print(1)
    exit()

while l <= b:
    l *= 3
    b *= 2
    count += 1

print(count)
