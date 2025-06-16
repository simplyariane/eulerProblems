ans = 0
for x in range(1000, 100, -1):
    for y in range(1000, 100, -1):
        if str(x * y) == str(x * y)[::-1]:
            if ans < x * y:
                ans = x * y
                break
print(ans)