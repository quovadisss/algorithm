"""
Similarly to the previous kata, you will need to return a boolean value if the base string can be expressed as the repetition of one subpattern.

This time there are two small changes:

if a subpattern has been used, it will be present at least twice, meaning the subpattern has to be shorter than the original string;
the strings you will be given might or might not be created repeating a given subpattern, then shuffling the result.
For example:

"a" --> false; //no repeated shorter sub-pattern, just one character
"aaaa" --> true; //just one character repeated
"abcd" --> false; //no repetitions
"babababababababa" --> true; //repeated "ba"
"bbabbaaabbaaaabb" --> true; //same as above, just shuffled
Strings will never be empty and can be composed of any character (just consider upper- and lowercase letters as different entities) and can be pretty long (keep an eye on performances!).

"""
from collections import defaultdict


def get_prime_factors(number):
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    return set(factors)


def has_subpattern(st):    
    count_dict = defaultdict(int)
    for x in st:
        count_dict[x] += 1
    counts = sorted(list(set(count_dict.values())))
    
    if len(counts) == 1 and list(counts)[0] != 1:
        return True
    
    result = False
    first_prime_factors = get_prime_factors(counts[0])
    for pf in first_prime_factors:
        result_ = True
        for x in counts[1:]:
            if x % pf != 0:
                result_ = False
        
        if result_:
            result = True
    
    return result



print(has_subpattern("aaaabb"))
