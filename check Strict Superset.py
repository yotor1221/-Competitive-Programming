import sys

input_line = sys.stdin.readline().strip()
A = set(map(int, input_line.split()))

n = int(sys.stdin.readline().strip())

N = []

for _ in range(n):
    set_line = sys.stdin.readline().strip()
    current_set = set(map(int, set_line.split()))
    N.append(current_set)

def checker(list1, sublist2):
    for num in sublist2:
        if num not in list1:
            return False
        
    
    for s in list1:
        if s not in sublist2:
            return True
    return False
    

for i in range(len(N)):
    superset = False
    if (checker(A, N[i])):
        superset = True
        continue
    else:
        superset = False
        break
        
print(superset)
