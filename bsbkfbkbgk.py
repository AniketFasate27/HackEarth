n = 2222
len1 = len(str(n))//2
print(len1)
sum1 = 0
sum2 = 0

while (len1 > 0):
    r = n%10
    sum2 +=r
    len1  = len1 - 1
    n = n//10

len1 = len(str(n))//2+1

while (len1 > 0):
    r = n%10
    sum1 +=r
    len1  = len1 - 1
    n = n//10

print(sum2)
print(sum1)