def solution(emergency):

    answer = []
    arr = sorted(emergency)
    arr.reverse()

    for i in emergency:
        answer.append(arr.index(i) + 1)

    return answer
