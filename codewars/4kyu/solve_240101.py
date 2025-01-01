def expanded_form(num):
    str_num = str(num)
    nums = []
    for i in range(len(str_num)):
        if str_num[i] == "0":
            continue
        zero_len = len(str_num) - i - 1
        nums.append(str_num[i] + ("0"*zero_len))
    return " + ".join(nums)