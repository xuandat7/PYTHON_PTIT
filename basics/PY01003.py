t = int(input())
while t>0:
    n = (input())
    # luu cac n vao list de xu ly
    arr = list(int(i) for i in n)
    #duyet tu hang don vi tro ve
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] >= 5:
            arr[i-1] += 1
        arr[i] = 0
    # xu ly chu so dau tien
    if arr[0] == 10:
        arr[0] = 0
        arr = [1] + arr
    for i in arr:
        print(i, end='')
    t -=1
    print()