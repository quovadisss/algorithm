import sys

start = sys.stdin.readline().strip()
end = sys.stdin.readline().strip()

answer = 0

while end != "":
    if end == start:
        answer = 1
        break

    if end.endswith("A"):
        end = end[:-1]
    else:
        end = end[:-1][::-1]

print(answer)

#%%
# 다른 사람의 코드
S, T = input(), input()
while len(T) > len(S):
    T = T[:-1] if T[-1] == 'A' else T[:-1][::-1]
print(1 if T == S else 0)