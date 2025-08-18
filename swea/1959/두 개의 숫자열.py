T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))

    answer = 0

    if N > M:
        N, M = M, N
        N_list, M_list = M_list, N_list

    for i in range(M - N + 1):
        sum_value = 0
        for j in range(N):
            sum_value += M_list[i + j] * N_list[j]
        answer = max(answer, sum_value)

    print(f"#{tc} {answer}")
