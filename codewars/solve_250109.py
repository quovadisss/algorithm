"""
Write a function that takes an arbitrary number of strings and interlaces them (combines them by alternating characters from each string).

For example combineStrings('abc', '123') should return 'a1b2c3'.

If the strings are different lengths the function should interlace them until each string runs out, continuing to add characters from the remaining strings.

For example combineStrings('abcd', '123') should return 'a1b2c3d'.

The function should take any number of arguments and combine them.

For example combineStrings('abc', '123', '£$%') should return 'a1£b2$c3%'.
"""

def combine_strings(*args):
    args = list(args)
    combined_len = sum([len(x) for x in args])
    combined = ""
    while len(combined) < combined_len:
        for i in range(len(args)):
            if args[i]:
                combined += args[i][0]
                args[i] = args[i][1:]
    return combined