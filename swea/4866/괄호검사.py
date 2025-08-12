def is_valid(paren_str):
    stack = []
    data_dict = {")": "(", "}": "{"}
    for ch in paren_str:
        if ch in data_dict.values():
            stack.append(ch)
        elif ch in data_dict:
            if not stack or stack[-1] != data_dict[ch]:
                return 0
            stack.pop()

    if len(stack) == 0:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    data = input()
    print(f"#{tc} {is_valid(data)}")
