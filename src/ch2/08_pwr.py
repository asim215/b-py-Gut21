# Write a program that asks the user to enter an integer and prints two
# integers, root and pwr, such that 1 < pwr < 6 and root**pwr is equal
# to the integer entered by the user. If no such pair of integers exist,
# it should print a message to that effect.

x = int(input("Enter an integer: "))
root: int = 0
pwr: int = 0
find = False
for pwr in range(2, 6):
    while root**pwr <= x:
        if root**pwr == x:
            find = True
            froot = root
            break
        root += 1
    if find is True:
        fpwr = pwr
        break
if find:
    print(f"Root: {froot}; Power: {fpwr}")
else:
    print("Such pair of root and pwr doen't exist")
