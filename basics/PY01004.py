import math

t = int(input())

def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

while(t > 0):
    n = int(input())
    cnt = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            cnt += 1
    if isPrime(cnt):
        print("YES")
    else:
        print("NO")
    t -= 1
    