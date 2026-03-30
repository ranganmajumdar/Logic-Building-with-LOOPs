#Print the multiplication tables for all numbers from 1 to 10 using nested loops.
for i in range(1, 11):
    print(f"Multiplication Table for {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Print a blank line after each table