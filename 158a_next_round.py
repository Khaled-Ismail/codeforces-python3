inp1=input().split()
for i in range(0, len(inp1)):
    inp1[i] = int(inp1[i])
inp2=input().split()

for i in range (0, len(inp2)):
    inp2[i] = int(inp2[i])

cont=0
for i in range (0, inp1[1]):
    if inp2[i] < inp2[inp1[1]-1]:
        break
    elif (inp2[i] >= inp2[inp1[1]-1]) and (inp2[i] != 0):
        cont+=1

for i in range (inp1[1], len(inp2)):
    if inp2[i] != inp2[inp1[1]-1]:
        break
    elif (inp2[i] == inp2[inp1[1]-1]) and (inp2[i] != 0):
        cont+=1
print(cont)
