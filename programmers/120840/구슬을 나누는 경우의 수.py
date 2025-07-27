# 풀이1
def solution(balls, share):
    n = factorial(balls)
    m = factorial(balls - share) * factorial(share)
    answer = n / m
    return answer


def factorial(n):
    sum = 1

    for i in range(1, n + 1):
        sum *= i

    return sum


# 풀이2
import math


def solution(balls, share):
    return math.comb(balls, share)
