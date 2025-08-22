T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    game = [list(map(int, input().split())) for _ in range(M)]
    board = [[0] * N for _ in range(N)]
    delta = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1),           (0, 1),
             (1, -1), (1, 1), (1, 0)]
    white = 0
    black = 0

    # 초기 게임판 돌 세팅
    mid = N // 2
    board[mid - 1][mid - 1] = 2
    board[mid - 1][mid] = 1
    board[mid][mid - 1] = 1
    board[mid][mid] = 2

    # 범위 확인 함수
    def inside(i, j):
        return 0 <= i < N and 0 <= j < N

    for y, x, r in game:
        # 상대 돌의 색깔
        opp = 3 - r
        
        # 해당 위치에 돌 놓기
        board[y - 1][x - 1] = r

        # 8개의 방향으로 탐색
        for di, dj in delta:
            # 내 색깔로 바꿀 상대의 돌의 좌표들을 담을 배열
            rocks = []
            # 내가 방금 놓은 돌을 기준으로 하는 근처 돌의 좌표
            i, j = y - 1 + di, x - 1 + dj

            # 범위 안에 없거나, 상대의 돌이 아니면 continue
            if not inside(i, j) or board[i][j] != opp:
                continue

            # 상대의 돌이 연속되면 범위 안에서 전진
            while inside(i, j) and board[i][j] == opp:
                # 해당 좌표를 rocks 배열에 추가해두기
                rocks.append((i, j))
                # 현재 방향으로 한 칸 더 이동
                i += di
                j += dj

            # 내 돌을 만나면 멈추고 rocks 안에 있는 좌표의 돌들을 전부다 바꾸기
            if inside(i, j) and board[i][j] == r and rocks:
                for ri, rj in rocks:
                    board[ri][rj] = r

    # 게임이 전부 끝난 보드의 흑돌, 백돌 개수 계산
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print(f"#{tc} {black} {white}")