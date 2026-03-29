#Print all numbers between a and b that are divisible by 7 bu using a for loop.
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print(f"Numbers between {a} and {b} that are divisible by 7:")
for i in range(a, b + 1):
    if i % 7 == 0:
        print(i)