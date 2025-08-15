T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    a, b = [list(map(int, input().split())) for _ in range(2)]
    cnt = 0

    for i in range(N):
        if a[i] != b[i]:
            cnt += 1
            for j in range(i, N):
                a[j] = 1 - a[j]

    print(f"#{tc} {cnt}")