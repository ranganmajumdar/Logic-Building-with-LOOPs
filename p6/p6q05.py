# Print the first n terms of a geometric progression for the given first term and common ratio.
a = int(input("Enter the first term: "))
r = int(input("Enter the common ratio: "))
n = int(input("Enter the number of terms: "))
for i in range(n):
    print(a * (r ** i), end=" ")