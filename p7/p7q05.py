# Print all numbers from 1 to n whose binary representation contains an even number of 1s.
def count_ones(num):
    return bin(num).count('1')
n = 100  # You can change this value to test with different n
for i in range(1, n + 1):
    if count_ones(i) % 2 == 0:
        print(i)
        