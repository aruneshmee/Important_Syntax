def divisibleSumPairs(n, k, ar):
    count=0
    for _ in range(0, len(ar)):
        x = ar[0]
        for y in ar[1:]:
            if (x + y)%k==0:
                count+=1
        ar.pop(0)
    return count
