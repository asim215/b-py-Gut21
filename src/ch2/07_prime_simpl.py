# Exhaustive enumeration
# Test if an int > 2 is prime. If not, print smallest divisor
# Modified to print largest divisor
# y*z=x, if y - smallest, then z is largest
x = int(input("Enter an integer greater than 2: "))
smallest_divisor = None
# largest_divisor = None
if x % 2 == 0:
    smallest_divisor = 2
else:
    for guess in range(3, x, 2):
        if x % guess == 0:
            smallest_divisor = guess
            # largest_divisor = x // smallest_divisor
            break
if smallest_divisor is not None:
    print(f"{x} is not prime")
    # print(f"Smallest divisor {smallest_divisor}, Largest divisor {largest_divisor}")
    print(f"Smallest divisor {smallest_divisor}")
else:
    print(f"{x} is a prime number")
