pieces = input().split()
chess = (1, 1, 2, 2, 2, 8)
result = []
for i in range(6):
    result.append(chess[i] - int(pieces[i]))
    print(result[i], end=" ")
