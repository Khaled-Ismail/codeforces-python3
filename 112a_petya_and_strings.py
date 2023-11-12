frst = []
frst_sum = 0

scnd = []
scnd_sum = 0

frst = list(input())
scnd = list(input())

out = 0

for i in range (0, len(frst)):
    frst[i] = frst[i].lower()
    #frst_sum += ord(frst[i])
    scnd[i] = scnd[i].lower()
    #scnd_sum += ord(scnd[i])
    if ord(frst[i]) < ord(scnd[i]):
        out = -1
        break
    elif ord(scnd[i]) < ord(frst[i]):
        out = 1
        break
    elif ord(frst[i]) == ord(scnd[i]):
        out = 0

print(out)
