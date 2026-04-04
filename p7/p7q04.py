# print all numbers from 1 to 100 whose sum of digits is a multiple of 3.
for i in range(1, 101):
    if sum(int(digit) for digit in str(i)) % 3 == 0:
        print(i)