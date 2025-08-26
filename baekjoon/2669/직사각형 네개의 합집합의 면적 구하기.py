# 겹치는 부분을 중복하여 저장 않도록 set 이용
answer = set()

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    # 사각형이 차지하는 x, y 좌표 순회
    for x in range(x1, x2):
        for y in range(y1, y2):
            answer.add((x, y))

# 넓이 출력
print(len(answer))