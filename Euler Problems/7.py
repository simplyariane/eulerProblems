import math
count = 1
n = 2
while count < 10001:
    prime = True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:  
            prime = False
            break
    if prime == True:
        print(n)
        count += 1
        if count == 10001:
            print(n)
            print(count)
            break
    n += 1
        