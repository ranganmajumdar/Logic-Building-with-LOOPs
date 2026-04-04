# Print all numbers between 1 and 100 whose sum of digits is even.
for i in range(1, 101):
    if sum(int(digit) for digit in str(i)) % 2 == 0:
        print(i)