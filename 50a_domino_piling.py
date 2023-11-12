dim = []
dim = input().split()
for i in range(0, len(dim)):
    dim[i] = int(dim[i])
tot_sqrs= dim[0] * dim[1]
out = tot_sqrs // 2
print(out)
