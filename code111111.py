import math
def primeFactors(n):
    c = n
    a = [1]
    sum = 0
    # a.append(1)
    while n % 2 == 0:
        a.append(int(2))
        n = n / 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            a.append(i)
            n = n / i
    if n > 2:
        a.append(int(n))
    for i in a:
        c = c // i
        sum =(sum + c)
    print(a)
    print(sum)
    
n = 6
primeFactors(n)
  