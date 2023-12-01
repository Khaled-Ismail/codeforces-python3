stops_no = int(input())

tram_stops = [[0]*2 for i in range(stops_no)]

max_cap = 0
curr_cap = 0

for i in range(stops_no):
    tram_stops[i] = input().split()
    tram_stops[i][0] = int(tram_stops[i][0])
    tram_stops[i][1] = int(tram_stops[i][1])
    curr_cap += tram_stops[i][1] - tram_stops[i][0]
    if max_cap <= curr_cap:
        max_cap = curr_cap

print(max_cap)
