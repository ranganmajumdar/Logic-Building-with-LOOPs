# print the HCF of given numbers using do while loop
def hcf(a, b):
    while True:
        if a == b:
            return a
        elif a > b:
            a -= b
        else:
            b -= a