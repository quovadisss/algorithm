"""
In this kata, you should determine the values in an unknown array of numbers. You'll be given a function f, which you can call like this:

f(a, b)
where a and b are indexes of two different elements in the unknown array, 1 or 2 indexes apart. f will return the sum of those two elements.

The absolute difference between a and b must not be 0 nor greater than 2 (that is: the chosen indexes must be exactly 1 or 2 apart).

Your goal is to figure out the correct array.

The whole procedure is:

You are given f and the length of the array n.
Ask f for any element sums you want.
Create and return the correct array according to the answers.
The array will always have at least 3 elements.
"""

def guess(f, n):
    answer = [0] * n
    
    sum_01 = f(0, 1)
    sum_02 = f(0, 2)
    sum_12 = f(1, 2)
    answer[0] = (sum_01 + sum_02 - sum_12) // 2
    answer[1] = sum_01 - answer[0]
    answer[2] = sum_12 - answer[1]
    
    if n > 3:
        for i in range(3, n):
            answer[i] = f(i-1, i) - answer[i-1]
        
    return answer