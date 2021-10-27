# Factor Finder
# Finds all the factors of a number.
# https://nostarch.com/big-book-small-python-programming (BSD Licensed)


import math, sys

print('''Factors are the numbers you multiply together to get another number.
Example: 2 and 3 are factors of 6, because 2 × 3 = 6. Factors are whole numbers,
not fractions.

If a number only has two factors (1 and itself), it is called a prime
number. Otherwise, it is called a composite number.

See if you can spot some prime numbers...

''')

while True:  # Main program loop.
    
    print('Enter a positive whole number to factor (or QUIT):')
    response = input('> ')
    if response.upper() == 'QUIT':
        sys.exit()

    if not (response.isdecimal() and int(response) > 0):
        continue
    number = int(response)

    factors = []

    # Find the factors of number:
    
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:  # If there's no remainder, it is a factor.
            factors.append(i)
            factors.append(number // i)

    # Convert to a set to get rid of duplicate factors:
    
    factors = list(set(factors))
    factors.sort()

    # Display the results:
    
    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print(', '.join(factors))
