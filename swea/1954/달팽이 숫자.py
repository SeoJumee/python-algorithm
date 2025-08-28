T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    arr = [[0] * N for _ in range(N)]
    # 우 하 좌 상
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 현재 위치
    i, j = 0, 0
    
    # 넣어줄 값, 2부터 시작
    cnt = 2
    
    # 시작점 (0, 0)에 1 넣기
    arr[0][0] = 1

    # 모든 칸 (N * N)을 다 채울 때까지 반복
    while cnt <= N * N:
        # 4가지 방향을 순서대로 순회
        for di, dj in delta:
            ni, nj = di + i, dj + j
            # 인덱스가 유효하고 0으로 빈 칸이라면
            while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                # 1. 값 채워주기
                arr[ni][nj] = cnt
                # 2. 현재 위치를 업데이트
                i, j = ni, nj
                # 3. 같은 방향으로 다음 칸을 검사하기 위해 ni, nj 업데이트
                ni += di
                nj += dj
                # 4. 다음에 채울 숫자를 +1
                cnt += 1

    print(f"#{tc}")
    for row in arr:
        print(*row)