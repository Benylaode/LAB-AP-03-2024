
n = int(input("N: "))
m = int(input("M: "))

for i in range(n): 
    if i % 2 == 0:
        for j in range(m):
            print("MOVE", i, j)
    else :
        for j in range(m-1, -1, 1):
            print("MOVE", i, j)