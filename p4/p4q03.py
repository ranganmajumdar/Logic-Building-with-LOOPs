#For every number from 1 to n, count and print the total numbers of its factors using nested loops.
n = 10  # You can change this value to count factors for different numbers
for i in range(1, n + 1):
    count_factors = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count_factors += 1
    print(f"The number of factors of {i} is: {count_factors}")