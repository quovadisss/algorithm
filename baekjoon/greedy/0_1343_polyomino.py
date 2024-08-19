# my code
import sys

results = []
for x in sys.stdin.readline().split("."):
    replaced = x.replace("XXXX", "AAAA")
    replaced = replaced.replace("XX", "BB")
    results.append(replaced)

results = ".".join(results)
if "X" in results:
    print(-1)
else:
    print(results)

#%%
# others' code
b = input()

pan = ['AAAA','BB']
board = b.replace('XXXX', pan[0])
board = board.replace('XX', pan[1])

if 'X' in board:
    print(-1)
else:
    print(board)

"""
어차피 polyomino는 이어져 있기에 replace를 하면 .은 건너뛰게 된다.
굳이 split 해줄 필요가 없다.
불필요한 곳에 시간을 쓰지 말자!
"""