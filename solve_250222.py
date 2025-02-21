"""
Given an array of numbers (in string format), you must return a string. The numbers correspond to the letters of the alphabet in reverse order: a=26, z=1 etc. You should also account for '!', '?' and ' ' that are represented by '27', '28' and '29' respectively.

All inputs will be valid.

"""
def switcher(arr):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    num2alphabet = {f"{i+1}": x for i, x in enumerate(alphabet[::-1])}
    num2alphabet.update({"27":"!", "28": "?", "29": " "})
    return "".join([num2alphabet[x] for x in arr])