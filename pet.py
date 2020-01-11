One = sum(map(int, input().split()))
Two = sum(map(int, input().split()))
Three = sum(map(int, input().split()))
Four = sum(map(int, input().split()))
Five = sum(map(int, input().split()))
if One > Two and One > Three and One > Four and One > Five:
    print(1, One)
elif Two > One and Two > Three and Two > Four and Two > Five:
    print(2, Two)
elif Three > One and Three > Two and Three > Four and Three > Five:
    print(3, Three)
elif Four > One and Four > Two and Four > Three and Four > Five:
    print(4, Four)
elif Five > One and Five > Two and Five > Three and Five > Four:
    print(5, Five)