T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # + 형태
    delta1 = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # x 형태
    delta2 = [[-1, -1], [-1, 1], [1, 1], [1, -1]]

    max_value = 0

    for i in range(N):
        for j in range(N):

            # 현재 값
            value = matrix[i][j]

            # + 와 x 모양 합계를 각각 계산
            delta1_sum_value = value
            delta2_sum_value = value

            # 분사 세기(M) 맞춰 중심으로부터 k만큼 떨어진 위치
            for k in range(1, M):
                # + 모양
                for di, dj in delta1:
                    ni, nj = i + k * di, j + k * dj
                    if 0 <= ni < N and 0 <= nj < N:
                        delta1_sum_value += matrix[ni][nj]

                # x 모양
                for di, dj in delta2:
                    ni, nj = i + k * di, j + k * dj
                    if 0 <= ni < N and 0 <= nj < N:
                        delta2_sum_value += matrix[ni][nj]

            # 전체 최댓값과 비교해 갱신
            max_value = max(max_value, delta1_sum_value, delta2_sum_value)

    print(f"#{tc} {max_value}")
