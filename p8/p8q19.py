#    A
#   BCD
#  EFGHI
# JKLMNOP
#QRSTUVWXY 
def p8q19():
    for i in range(1, 6):
        for j in range(1, 2 * i):
            print(chr(64 + j), end=' ')
        print()