import math
a = 600851475143
i = 3

while True:
    if a % i == 0:
        print(i)
        a = a // i
        i = i + 2
    else:
        i = i + 2
        