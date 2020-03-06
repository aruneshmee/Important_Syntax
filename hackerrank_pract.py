# HackerRank Algorithms

def divisibleSumPairs(n, k, ar):
    count=0
    for _ in range(0, len(ar)):
        x = ar[0]
        for y in ar[1:]:
            if (x + y)%k==0:
                count+=1
        ar.pop(0)
    return count

# Ordered Dictionary
from collections import OrderedDict
count = OrderedDict()
for i in ar:
    count.setdefault(i, 0)
    count[i] += 1
    
x = max(count, key=count.get)
print( x)

#Array Manu
def miniMaxSum(arr):
    mins=0
    maxs=0
    arr.sort()
    a = arr.pop(0)
    for i in arr:
        maxs += i
    arr.pop(-1)
    arr.append(a)
    arr.sort()
    for i in arr:
        mins += i
    print(mins,maxs)

# dictionaries and maps
n = int(input())
book ={}
for _ in range(n):
    item = input().split()
    book[item[0]]=int(item[1])

while True:
    try:
        query = input()
    except EOFError:
        break
    if query in book:
        print(query,'=',book[query])
    else:
        print('Not found')

 # Count Utopian trees
 def count(n):
    growth = 1
    cycle = 1
    for _ in range(n):
        if cycle%2==0:
            growth+=1
        else:
            growth = growth*2
        cycle +=1
    return growth

# Maximum Hourglass value in a 2-D 6x6 array
row = 0
col = 0
maxx = []
for _ in range(4):
    for _ in range(4):
        summ = (arr[row][col]+arr[row][col+1]+arr[row][col+2])+arr[row+1][col+1]+(arr[row+2][col]+arr[row+2][col+1]+arr[row+2][col+2])
        maxx.append(summ)
        col+=1
    row+=1
    col=0
print(max(maxx))
