from itertools import chain

def sel_reverse(arr,l):
    if l == 0:
        return arr
    result = []
    for i in range(0, len(arr), l):
        splited = arr[i:i+l]
        splited.reverse()
        result.extend(splited)
    return result