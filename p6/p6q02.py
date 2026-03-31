#Find and print the sum of the first n even numbers.
n = int(input("Enter the value of n: "))
sum = 0
for i in range(1, n + 1):
    sum += 2 * i
print("The sum of the first", n, "even numbers is:", sum)