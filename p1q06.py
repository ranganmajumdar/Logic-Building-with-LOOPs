#print the sum of first n natural number using while loop using python
n = int(input("Enter a number: "))
total_sum = 0
i = 1
while i <= n:
    total_sum += i
    i += 1
print(f"The sum of first {n} natural numbers is: {total_sum}") 