import sys


def sum(temp):
    suma = 0
    for i in temp:
        suma = suma + i
    return int(suma)


for x in sys.stdin:
    numbers_str = x.split()
    numbers_int = tuple(map(int, numbers_str))
    add = 0
    for i in range(len(numbers_int)):
        temp = list(numbers_int)
        deleted = temp.pop(i)
        if deleted == int(sum(temp)):
            print(deleted)
            break
