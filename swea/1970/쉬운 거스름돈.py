T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    pay = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    answer = []

    for i in pay:
        answer.append(N // i)
        N = N % i

    print(f"#{tc}")
    print(*(answer))
