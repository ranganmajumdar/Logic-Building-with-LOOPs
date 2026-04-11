# A
# B B
# C C C
# D D D D
# E E E E E
def p8q17():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(chr(64 + i), end=' ')
        print()