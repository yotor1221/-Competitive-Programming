if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr = sorted(arr,reverse=True)
    for i in range(n):
        if arr[i+1] < arr[i]:
            print(arr[i+1])
            break
