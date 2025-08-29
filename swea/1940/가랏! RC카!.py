T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    speed = 0
    answer = 0

    for _ in range(N):
        C = list(map(int, input().split()))
        
        # 가속 or 감속일 경우
        if len(C) == 2:
            # T: 명령어 종류, V: 가속도
            T, V = C
            # 가속일 경우
            if T == 1:
                # 가속
                speed += V
                # 거리 더하기
                answer += speed
            # 감속일 경우
            else:
                # 감속 후 속도가 0 미만으로 떨어지지 않도록 처리
                speed = max(0, speed - V)
                # 거리 더하기
                answer += speed
        # 속도 유지일 경우
        else:
            # 현재 속도 그대로 거리 더하기
            answer += speed

    print(f"#{tc} {answer}")