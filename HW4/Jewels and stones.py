def count_jewels(stones, jewels):
    n=0
    for i in stones:
        if i in jewels:
            n+=1
    return n

stones=list(input())
jewels=list(input())
print(count_jewels(stones, jewels))
