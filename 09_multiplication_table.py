#Print multiplication table of a number entered by user (using for loop with range).
# Example: for 5 → 5 x 1 = 5, 5 x 2 = 10, … up to 10.
num = int(input("enter a number : "))

for i in range(1,11):
    result = num * i
    print(f"{num } x {i} = {result}")


