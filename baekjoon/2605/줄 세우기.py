N = int(input())
numbers = list(map(int, input().split()))
line = []

for i in range(N):
    student_number = i + 1
    position = numbers[i]
    # 현재 줄의 길이에서 뽑은 번호만큼 앞으로 간 위치에 학생 숫자 삽입
    line.insert(len(line) - position, student_number)

print(*line)