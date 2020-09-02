n = int(input())
for _ in range(n):
    px, py, qx, qy = list(map(int, input().split()))

    rx, ry = 2*qx - px, 2*qy - py

    print("{} {}".format(rx, ry))
