t = int(input())
def check(n):
    arr = list(int(i) for i in n)
    for i in arr:
        if i != 4 and i != 7:
            return False
    return True
while t > 0:
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")
    t -= 1