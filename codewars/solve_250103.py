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
def cubes(n: int) -> tuple[int, int] | None:
    if n == 0:
        return (0, 0)
    
    limit = int(pow(n, 1/3)) + 3

    for a in range(-limit, limit):
        b = -n + (a**3)
        print(b)
        pow_b = -pow(abs(b), 1/3) if b < 0 else pow(b, 1/3)
        print(a, pow_b)

        if type(pow_b) == float and int(pow_b) == pow_b:
            return (a, int(pow_b))

    return None

print(cubes(7110))