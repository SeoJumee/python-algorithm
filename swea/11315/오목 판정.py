T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    matrix = [list(input()) for _ in range(N)]

    # 오른쪽, 아래, 우하향 대각선, 좌하향 대각선
    delta = [(0, 1), (1, 0), (1, 1), (1, -1)]

    answer = "NO"
    found = False

    for i in range(N):
        for j in range(N):
            # 현재 칸에 돌이 있는 경우 탐색 시작
            if matrix[i][j] == "o":

                # 정의된 4가지 방향에 대해 각각 탐색
                for di, dj in delta:
                    # 연속된 돌의 개수
                    cnt = 1
                    ni, nj = i + di, j + dj

                    # 다음 칸이 판의 범위 안에 있고, 그 칸에도 돌이 있는 동안 계속 반복
                    while 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == "o":
                        # 연속된 돌의 개수를 1 증가
                        cnt += 1
                        # 같은 방향으로 계속 이동
                        ni, nj = ni + di, nj + dj

                    # 연속된 돌의 개수가 5개 이상이면 오목
                    if cnt >= 5:
                        answer = "YES"
                        found = True
                        break
            if found:
                break
        if found:
            break

    print(f"#{tc} {answer}")
