"""
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:
   12 --> "10 + 2"
   45 --> "40 + 5"
70304 --> "70000 + 300 + 4"
NOTE: All numbers will be whole numbers greater than 0.
"""


def expanded_form(num):
    str_num = str(num)
    nums = []
    for i in range(len(str_num)):
        if str_num[i] == "0":
            continue
        zero_len = len(str_num) - i - 1
        nums.append(str_num[i] + ("0"*zero_len))
    return " + ".join(nums)