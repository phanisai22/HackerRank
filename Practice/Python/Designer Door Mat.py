N, M = list(map(int, input().split()))
# N , M = 7, 21

if 5 < N < 101 and 15 < M < 303:
    for i in range(1, N, 2):
        print((".|."*i).center(M, "-"))
    print(("WELCOME".center(M, "-")))
    for i in range(N - 2, 0, -2):
        print((".|."*i).center(M, "-"))
