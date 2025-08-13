T = int(input())

for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    max_value = 0
    min_value = 10000 * M

    for base_idx in range(N - M + 1):
        sum_value = 0
        for part_idx in range(0, M):
            sum_value += arr[base_idx + part_idx]
        max_value = max(max_value, sum_value)
        min_value = min(min_value, sum_value)
    print(f"#{test_case} {max_value - min_value}")
