T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 1
 
    cur = 0
    next_value = 1
 
    arr.sort(key=lambda x: x[1])
 
    while next_value < N:
        if arr[next_value][0] >= arr[cur][1]:
            cur = next_value
            next_value = cur + 1
            cnt += 1
        else:
            next_value += 1
 
    print(f"#{tc} {cnt}")