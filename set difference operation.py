ne = int(input())
e = list(map(int,input().split()))
nf = int(input())
f = list(map(int,input().split()))

numOfEng = 0

for num in e:
    if num in f:
        continue
    else:
        numOfEng += 1
print(numOfEng)
