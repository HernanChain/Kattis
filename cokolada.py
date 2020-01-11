k = int(input())
size_bar = 1
cont = []
while size_bar < k:
    cont.append(size_bar)
    size_bar *= 2
sum = 0
aux = 0
if k == size_bar:
    print(size_bar,0)
else:
    for x in cont[::-1]:
        sum += x
        aux += 1
        if sum == k :
            print(size_bar,aux )
        elif sum > k:
            sum -= x