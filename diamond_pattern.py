n = 5
for i in range(n):
    for j1 in range(i, n):
        print(" ", end=" ")
    for j2 in range(i):
        print("*", end=" ")
    for j3 in range(i + 1):
        print("*", end=" ")
    print()
for i in range(n,-1, -1):
    for j1 in range(i, n):
        print(" ", end=" ")
    for j2 in range(i):
        print("*", end=" ")
    for j3 in range(i + 1):
        print("*", end=" ")
    print()
