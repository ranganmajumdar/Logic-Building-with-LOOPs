#Search for a specific number in a list of inputs, and terminate the loop immediately
#when the number is found using break/ continue.
target = int(input("Enter the number to search for: "))
found = False
for _ in range(5):
    num = int(input("Enter a number: "))
    if num == target:
        found = True
        break
if found:
    print(f"{target} found in the list.")
else:   
    print(f"{target} not found in the list.")