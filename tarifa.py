plan = int(input())
n = int(input())
days = []
for i in range(n):
    days.append(int(input()))
print(((n+1)*plan)-sum(days))