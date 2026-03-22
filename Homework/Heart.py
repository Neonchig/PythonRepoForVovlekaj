# ((x**2 + y**2 - 1)**3 - (x*x*y*y*y))
N = int(input())

for i in range(N, -N, -1):
    for j in range(-2*N, 2*N):
        y = i / (N*0.6)
        x = j / (N*0.85)
        if ((x*x + y*y - 1)**3 - (x*x*y*y*y)) <= 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()