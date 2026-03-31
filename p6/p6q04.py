#Print the first n terms of an arithmetic progression for the given first term and common difference
a = int(input("Enter the first term: "))
d = int(input("Enter the common difference: "))
n = int(input("Enter the number of terms: "))
for i in range(n):
    print(a + i * d, end=" ")