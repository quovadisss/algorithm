"""
Given n representing the number of floors build a beautiful multi-million dollar mansions like the ones in the example below:

     /\
    /  \
   /    \
  /______\  number of floors 3
  |      |
  |      |
  |______|

     /\
    /  \
   /____\
   |    |   2 floors
   |____|

     /\
    /__\    1 floor
    |__|
Note: whitespace should be preserved on both sides of the roof. Number of floors will go up to 30. There will be no tests with invalid input.

"""

def my_crib(n):
    rows = []
    for i in range(1, n*2 + 2):
        if i < n+2:
            out_space = " "*(n+1 - i)
            roof_middle = " " if i != n+1 else "_"
            row = out_space + "/" + roof_middle*(i-1)*2 + "\\" + out_space
        else:
            wall_middle = " "*(n*2) if i != n*2+1 else "_"*(n*2)
            row = "|" + wall_middle + "|"
        rows.append(row)
    return "\n".join(rows)