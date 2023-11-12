mat = [[0]*5 for i in range(5)]
mat_row = [5]
one_loc_x = 0
one_loc_y = 0
for i in range(0, 5):
    mat_row = input().split()
    for j in range (0, 5):
        mat_row[j] = int(mat_row[j])
        if(mat_row[j] == 1):
            one_loc_x = i
            one_loc_y = j
        mat[i][j] = mat_row[j]
dist_x = abs(one_loc_x - 2)
dist_y = abs(one_loc_y - 2)
out = dist_x + dist_y
print(out)
