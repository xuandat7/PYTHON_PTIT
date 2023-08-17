t = int(input())
while t > 0:
    n = input()
    idx = len(n)
    if n[idx-1] == '6' and n[idx-2] == '8':
        print("YES")
    else:
        print("NO")
    t -= 1