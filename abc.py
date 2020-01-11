num1, num2, num3 = map(int, input().split())
order = input()
mayor = 0
medio = 0
menor = 0
if num1 > num2 > num3:
    mayor = num1
    medio = num2
    menor = num3
elif num1 > num3 > num2:
    mayor = num1
    medio = num3
    menor = num2
elif num2 > num1 > num3:
    mayor = num2
    medio = num1
    menor = num3
elif num2 > num3 > num1:
    mayor = num2
    medio = num3
    menor = num1
elif num3 > num1 > num2:
    mayor = num3
    medio = num1
    menor = num2
elif num3 > num2 > num1:
    mayor = num3
    medio = num2
    menor = num1
elif num1 == num2 == num3:
    mayor = num1
    medio = num2
    menor = num3
elif num1 == num2 > num3:
    mayor = num1
    medio = num2
    menor = num3
elif num1 == num3 > num2:
    mayor = num1
    medio = num3
    menor = num2
elif num2 == num1 > num3:
    mayor = num2
    medio = num1
    menor = num3
elif num2 == num3 > num1:
    mayor = num2
    medio = num3
    menor = num1
elif num3 == num1 > num2:
    mayor = num3
    medio = num1
    menor = num2
elif num3 == num2 > num1:
    mayor = num3
    medio = num2
    menor = num1

if order[0] == 'A' and order[1] == 'B' and order[2] == 'C':
    print(menor, medio, mayor)
elif order[0] == 'A' and order[1] == 'C' and order[2] == 'B':
    print(menor, mayor, medio)
elif order[0] == 'B' and order[1] == 'A' and order[2] == 'C':
    print(medio, menor, mayor)
elif order[0] == 'B' and order[1] == 'C' and order[2] == 'A':
    print(medio, mayor, menor)
elif order[0] == 'C' and order[1] == 'A' and order[2] == 'B':
    print(mayor, menor, medio)
elif order[0] == 'C' and order[1] == 'B' and order[2] == 'A':
    print(mayor, medio, menor)
