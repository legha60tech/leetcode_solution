def climbstairs(n):
    if n <= 2:
        return n
    c,d=1,2
    for i in range(3, n + 1):
        c,d = d, c + d
    return d
n = int(input("Enter number of steps: "))
result = climbstairs(n)
print("Number of ways:", result)
