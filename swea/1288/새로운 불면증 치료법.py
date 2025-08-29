T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    storage = set()
    # 양을 센 횟수
    cnt = 0

    while len(storage) < 10:
        # 횟수 1 더하기
        cnt += 1
        # cnt 번째 양 번호 (cntN)
        cur_num = N * cnt

        # 각 자리수를 set에 추가
        for number in str(cur_num):
            storage.add(number)

    # 끝난 후 현재 양 번호
    print(f"#{tc} {cur_num}")