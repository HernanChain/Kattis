value = float(input())
lawns = int(input())
cost = 0
for i in range(lawns):
    lenght, width = map(float, input().split())
    cost += value * (lenght * width)
print(cost)
