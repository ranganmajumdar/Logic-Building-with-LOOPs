# A
# B C
# D E F
# G H I J
# K L M N O 
def p8q16():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(chr(64 + j), end=' ')
        print()
