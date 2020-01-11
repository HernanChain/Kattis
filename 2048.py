from builtins import range


def job(matrix):
    for i in range(4):
        matrix[i] = moveNumber(matrix[i])
        for j in range(3):
            if matrix[i][j] == matrix[i][j + 1]:
                current = matrix[i][j]
                next = matrix[i][j + 1]
                sum = current + next
                matrix[i][j] = sum
                matrix[i][j + 1] = 0
                matrix[i] = moveNumber(matrix[i])
    return matrix


def left(matrix):
    solved_matrix = job(matrix)
    return solved_matrix


def up(matrix):
    solved_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    temporal_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for x in range(4):
        for y in range(4):
            temporal_matrix[x][y] = matrix[y][x]
    temporal_matrix = job(temporal_matrix)
    for x in range(4):
        for y in range(4):
            solved_matrix[x][y] = temporal_matrix[y][x]
    return solved_matrix


def right(matrix):
    solved_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    temporal_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for x in range(4):
        cont = 3
        for y in range(4):
            temporal_matrix[x][y] = matrix[x][cont]
            cont -= 1
    temporal_matrix = job(temporal_matrix)
    for x in range(4):
        cont = 3
        for y in range(4):
            solved_matrix[x][y] = temporal_matrix[x][cont]
            cont -= 1
    return solved_matrix


def down(matrix):
    solved_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    temporal_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for x in range(4):
        cont = 3
        for y in range(4):
            temporal_matrix[x][y] = matrix[cont][x]
            cont -= 1

    temporal_matrix = job(temporal_matrix)
    aux = 3
    for x in range(4):
        for y in range(4):
            solved_matrix[x][y] = temporal_matrix[y][aux]
        aux -= 1
    return solved_matrix


def moveNumber(row):
    moved = [0,0,0,0]
    act = 0
    for i in range(4):
        if row[i] != 0:
            moved[act] = row[i]
            act += 1
    return moved


def printMatrix(matrix):
    a = ""
    for i in range(4):
        for j in range(4):
            a += str(matrix[i][j]) + " "
        print(a)
        a = ""


matrix = []
for line in range(4):
    a, b, c, d = map(int, input().split())
    row = [a, b, c, d]
    matrix.append(row)
move = int(input())
solution = [range(4) for i in range(4)]
if move == 0:
    solution = left(matrix)
elif move == 1:
    solution = up(matrix)
elif move == 2:
    solution = right(matrix)
elif move == 3:
    solution = down(matrix)
printMatrix(solution)