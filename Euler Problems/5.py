x = 20
while any(x % i for i in range(1, 21)): 
    x += 20
print(x)