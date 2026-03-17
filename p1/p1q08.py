#calculate and print the sum of all the odd number from 1 to n using while loop using python.
n = int(input("Enter a number: "))
total_sum = 0
i = 1
while i <= n:
    if i % 2 != 0:
        total_sum += i
    i += 1
print(f"The sum of all odd numbers from 1 to {n} is: {total_sum}")