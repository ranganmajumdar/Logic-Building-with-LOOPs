# print all number from a to b that are divisible by 3
a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))
print("Numbers from", a, "to", b, "that are divisible by 3:")
for i in range(a, b + 1):
    if i % 3 == 0:
        print(i)