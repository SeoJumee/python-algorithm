import math

N, K = map(int, input().split())
# 학년별 남학생, 여학생 수를 저장할 딕셔너리
man, woman = {}, {}
cnt = 0

for _ in range(N):
    S, Y = map(int, input().split())

    # 여학생일 경우
    if S == 0:
        # 해당 학년을 +1, 없을 경우 1로 추가
        if Y in woman:
            woman[Y] += 1
        else:
            woman[Y] = 1
    # 남학생일 경우
    else:
        if Y in man:
            man[Y] += 1
        else:
            man[Y] = 1

# 남학생과 여학생 딕셔너리를 순회하며 방 개수 계산
for s in [man, woman]:
    # 딕셔너리의 각 값 (학년별 학생 수)
    for value in s.values():
        # 학생 수를 K로 나눈 뒤 올림하여 방 개수 구하기
        cnt += math.ceil(value / K)

print(cnt)
