T = int(input())

for tc in range(1, T + 1):
    # N: 컨테이너 수, M: 트럭 수
    N, M = map(int, input().split())
    # 화물 무게 리스트
    weights = list(map(int, input().split()))
    # 트럭 적재용량 리스트
    trucks = list(map(int, input().split()))

    # 화물 무게와 트럭 적재용량을 내림차순으로 정렬
    weights.sort(reverse=True)
    trucks.sort(reverse=True)
    
    # 옮겨진 화물 무게
    total_weight = 0

    # 현재 확인 중인 화물과 트럭 인덱스
    w_idx, t_idx = 0, 0

    # 사용 가능한 화물과 트럭이 남아있는 경우 반복
    while w_idx < N and t_idx < M:
        # 트럭이 화물을 실을 수 있을 경우
        if trucks[t_idx] >= weights[w_idx]:
            # 총 무게에 더하기
            total_weight += weights[w_idx]
            # 다음 화물과 트럭으로 이동
            w_idx += 1
            t_idx += 1
        # 트럭이 화물을 실을 수 없는 경우 (화물의 무게가 적재용량을 초과)
        else:
            # 다음 화물로 이동
            w_idx += 1

    print(f"#{tc} {total_weight}")