T = int(input())
 
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(input())
    number_dict = {}
    max_key = 0
    max_value = 0
 
    for item in arr:
        if not item in number_dict.keys():
            number_dict[item] = 0
        number_dict[item] += 1
 
    for key in number_dict:
        if number_dict[key] > max_value:
            max_value = number_dict[key]
            max_key = key
        if number_dict[key] == max_value and key > max_key:
            max_key = key
 
    print(f"#{test_case} {max_key} {max_value}")