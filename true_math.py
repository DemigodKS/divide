import math
def divine(first, second):
    if second == 0:
        print(math.inf)
    else:
        print(first / second)

divine(5,0)