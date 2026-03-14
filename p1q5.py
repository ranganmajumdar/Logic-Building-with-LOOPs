#print the multiplication table of a given number from n*1 to n*10 using while loop using python
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{n} * {i} = {n * i}")
    i += 1