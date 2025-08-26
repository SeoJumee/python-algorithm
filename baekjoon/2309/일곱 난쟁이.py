arr = [int(input()) for _ in range(9)]
arr.sort()

# 스파이 2명의 키 합 찾기
target = sum(arr) - 100

def erase_two(nums, target):
    # 모든 쌍을 순회
    for i in range(9):
        for j in range(i + 1, 9):
            if nums[i] + nums[j] == target:
                # 찾은 스파이 값들을 pop
                nums.pop(j)
                nums.pop(i)
                # 찾으면 즉시 return
                return

erase_two(arr, target)

# 나머지 7명을 출력
for x in arr:
    print(x)