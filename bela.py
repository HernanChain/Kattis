n, b = input().split()
n = int(n)
dominant = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
not_dominant = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}
sum = 0
for i in range(4*n):
    card = input()
    if card[1] == b:
        sum += dominant[card[0]]
    else:
        sum += not_dominant[card[0]]
print(sum)