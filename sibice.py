import math
n, w, h = map(int, input().split())
diagonal = math.sqrt(math.pow(w, 2) + math.pow(h, 2))
for i in range(n):
    if int(input()) <= diagonal:
        print("DA")
    else:
        print("NE")