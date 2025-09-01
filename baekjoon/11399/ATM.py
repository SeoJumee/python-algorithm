N = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 최종 결과
total_time = 0
# 각 사람이 기다린 시간
wait_time = 0

for time in arr:
    # 현재 사람이 기다려야 하는 시간 (이전에 기다린 값 + 본인 시간)
    wait_time += time
    # 총 대기시간 + 현재 사람의 대기 시간
    total_time += wait_time

print(total_time)
