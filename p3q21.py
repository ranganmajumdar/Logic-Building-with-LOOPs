#Find and print the sum of all odd numbers from 1 up to n using for loop.
n = int(input("Enter a number: "))
total_sum = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        total_sum += i
print(f"The sum of all odd numbers from 1 to {n} is: {total_sum}")