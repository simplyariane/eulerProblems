import math

ans = 17
count = 10

while count < 2000000:
    prime = True
    for i in range(2, math.ceil(math.sqrt(count)) + 1):
        if count % i == 0:
            prime = False
            break
    if prime == True:
        print(count)
        ans += count
    count += 1
print(ans)