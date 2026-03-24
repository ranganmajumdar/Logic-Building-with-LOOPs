# print the fibonacci series up to n terms using do while loop
n = int(input("Enter the number of terms: "))
a = 0
b = 1
count = 0
while True:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
    if count >= n:
        break
