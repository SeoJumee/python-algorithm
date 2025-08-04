n, k = map(int, input().split())

list = list(range(1, n + 1))
answer = []
index = 0

for i in range(n):
    index = index + k - 1
    if index >= len(list):
        index = index % len(list)
    answer.append(list.pop(index))

print('<' + str(answer)[1:-1] + '>')