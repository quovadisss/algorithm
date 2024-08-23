import sys

N = int(sys.stdin.readline())
order = [int(x) for x in sys.stdin.readline().split()]
indices = list(range(N))
answer = [0] * N
for i, x in enumerate(order):
    answer[indices.pop(x)] = i+1

print(" ".join(map(str, answer)))


#%%
# 다른 유저의 답변..
N = int(sys.stdin.readline())
order = [int(x) for x in sys.stdin.readline().split()]
ans = []
for i in range(N-1,-1,-1):
    ans.insert(order[i], i+1)

print(*ans)
#%%