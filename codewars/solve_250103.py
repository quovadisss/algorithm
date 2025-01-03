"""
Difference of Cubes
Task
Given an integer n (-2^64 ≤ n ≤ 2^64), return any pair of two integers (a, b) such that a^3 - b^3 = n. If there is no solution, return None (or your language's equivalent).

Examples
19 -> (3, 2)    # 3^3 - 2^3 = 19
64 -> (4, 0)    # 4^3 - 0^3 = 64
100 -> None     # or your language's equivalent
-37 -> (3, 4)   # 3^3 - 4^3 = -37
217 -> (9, 8)   # 9^3 - 8^3 = 217
"""
def find_cube_pairs(n):
    if abs(n) > 2**64:
        return None
    
    if n == 0:
        return (0, 0)
    
    is_negative = n < 0
    n = abs(n)
    
    limit = int(pow(n, 1/3)) + 2
    
    for a in range(-limit, limit + 1):
        for b in range(-limit, limit + 1):
            if a**3 - b**3 == n:
                return (a, b) if not is_negative else (b, a)
            elif b**3 - a**3 == n:
                return (b, a) if not is_negative else (a, b)
    
    return None

print(find_cube_pairs(1729))
