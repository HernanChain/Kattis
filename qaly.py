n = int(input())
accumulate = 0
for i in range(n):
    q, y = map(float, input().split())
    accumulate += q*y
print(accumulate)