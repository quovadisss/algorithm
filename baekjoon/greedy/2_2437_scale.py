import sys

N = int(sys.stdin.readline())
nums = [int(x) for x in sys.stdin.readline().split()]
nums.sort()

target = 1
for num in nums:
    if target < num:
        break

    target += num

print(target)