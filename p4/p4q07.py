# Print a matrix, then calculate and display the sum of each row and the sum of each column.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

# Calculate and display the sum of each row
print("\nSum of each row:")
for i, row in enumerate(matrix):
    print(f"Row {i + 1}: {sum(row)}")

# Calculate and display the sum of each column
print("\nSum of each column:")
for j in range(len(matrix[0])):
    column_sum = sum(matrix[i][j] for i in range(len(matrix)))
    print(f"Column {j + 1}: {column_sum}")