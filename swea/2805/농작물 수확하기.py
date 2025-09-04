T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    
    # 정중앙 인덱스
    mid = N // 2
    # 중앙으로부터 떨어진 거리 (간격)
    offset = 0
    answer = 0

    # 중앙에서 시작해 확장하며 계산
    while offset <= mid:
        # 초기
        if offset == 0:
            # 중앙 행의 모든 가치 더하기
            answer += sum(matrix[mid])
        else:
            # 중앙을 기준으로 대칭되는 위/아래 두 행의 수확 범위를 계산하여 더하기
            for i in range(offset, N - offset):
                answer += matrix[mid - offset][i]  # 위쪽 행
                answer += matrix[mid + offset][i]  # 아래쪽 행
        
        offset += 1

    print(f"#{tc} {answer}")