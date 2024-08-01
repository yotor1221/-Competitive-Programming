import sys
from collections import defaultdict

first_line = sys.stdin.readline().strip()
n, m = map(int, first_line.split())

A = []
for _ in range(n):
    word = sys.stdin.readline().strip()
    A.append(word)

B = []
for _ in range(m):
    word = sys.stdin.readline().strip()
    B.append(word)


checker = defaultdict(list)

for i in range(m):
    for j in range(n):
        if B[i] == A[j]:
            checker[i].append(j+1)
    if len(checker[i]) == 0:
        checker[i].append(-1)

for j in range(len(checker)):
    my_val = ' '.join(map(str, checker[j]))
    print(my_val)
