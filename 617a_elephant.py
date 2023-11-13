inp = int(input())
out = 0

while (inp > 0):
    if inp >= 5:
        inp -= 5
        out += 1
    elif inp >= 4:
        inp -= 4
        out += 1
    elif inp >= 3:
        inp -= 3
        out += 1
    elif inp >= 2:
        inp -=2
        out += 1
    elif inp >= 1:
        inp -=1
        out += 1
print(out)
