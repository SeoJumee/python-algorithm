T = int(input())

for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    for _ in range(M):
        i, j = list(map(int, input().split()))

        for k in range(1, j + 1):
            before = i - 1 - k
            after = i - 1 + k

            if before < 0 or after > N - 1:
                break

            if arr[before] == arr[after]:
                if arr[before] == 0:
                    arr[after] = 1
                    arr[before] = 1
                else:
                    arr[before] = 0
                    arr[after] = 0

    print(f"#{test_case} {' '.join(list(map(str, arr)))}")
