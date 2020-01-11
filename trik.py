moves = input()
status = 1
for i in range(len(moves)):
    if moves[i] == 'A' and status == 1:
        status = 2
    elif moves[i] == 'A' and status == 2:
        status = 1
    elif moves[i] == 'A' and status == 3:
        status = 3
    elif moves[i] == 'B' and status == 1:
        status = 1
    elif moves[i] == 'B' and status == 2:
        status = 3
    elif moves[i] == 'B' and status == 3:
        status = 2
    elif moves[i] == 'C' and status == 1:
        status = 3
    elif moves[i] == 'C' and status == 2:
        status = 2
    elif moves[i] == 'C' and status == 3:
        status = 1
print(status)