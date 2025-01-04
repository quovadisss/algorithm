"""
Given an array of positive or negative integers

 I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

Example:
I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes:

It can happen that a sum is 0 if some numbers are negative!
Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.

In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.
"""
"""
1. 각 숫자마다 prime number를 구한다
 - prime number를 구하면서 만약 defaultdict(int)에 해당 숫자들을 더한다
2. 마지막으로 리스트를 만든다.


"""
from collections import defaultdict


def sum_for_list(lst):
    sum_nums = defaultdict(int)

    for num in lst:
        check_dict = {}
        n = abs(num)

        while n % 2 == 0:
            if 2 not in check_dict:
                sum_nums[2] += num
                check_dict[2] = None
            n = n // 2
    
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                if i not in check_dict:
                    sum_nums[i] += num
                    check_dict[i] = None
                n = n // i

        if n > 1:
            sum_nums[n] += num
                
    result = [[k, v] for k, v in sorted(sum_nums.items(), key=lambda x: x[0])]
    return result