def sum_digits(num):
    num = str(num)
    sum = 0
    for j in range(len(num)):
        sum += int(num[j])
    return sum


l = int(input())
d = int(input())
x = int(input())
cont = 0
n = 0
m = 0
for i in range(l, d+1):
    if l == d:
        n = l
        m = d
    else:
        if sum_digits(i) == x and cont == 0:
            n = i
            cont += 1
        elif sum_digits(i) == x and cont == 1:

            m = i
if m == 0:
    m = n
print(n)
print(m)