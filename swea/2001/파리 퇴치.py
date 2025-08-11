T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    MAX = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum = 0
            for i2 in range(M):
                for j2 in range(M):
                    sum += matrix[i + i2][j + j2]
            MAX = max(MAX, sum)

    print(f"#{test_case} {MAX}")
