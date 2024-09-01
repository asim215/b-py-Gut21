# FE. Write a program that prints the sum of the prime numbers greater
# than 2 and less than 1000.
# Hint: you probably want to use a for loop that is a primality test
# inside a for loop that iterates over the odd integers between 3 and 999
sum = 0
for n in range(3, 1000, 2):
    for d in range(2, n):
        if n % d == 0:
            # not prime
            # print(f"{n} is not prime")
            break
    else:
        # no break happend. no successful dividion
        # it is prime
        sum += n
        print(f"{n} is prime, current sum is {sum}")
