# https://nostarch.com/big-book-small-python-programming (BSD Licensed)
# Collatz Sequence
# Generates numbers for the Collatz sequence, given a starting number.
# More info at: https://en.wikipedia.org/wiki/Collatz_conjecture


import sys, time

print('''The Collatz sequence is a sequence of numbers produced from a starting
number n, following three rules:

1) If n is even, the next number n is n / 2.
2) If n is odd, the next number n is n * 3 + 1.
3) If n is 1, stop. Otherwise, repeat.

It is generally thought, but so far not mathematically proven, that
every starting number eventually terminates at 1.
''')

print('Enter the number (greater than 0) you would like to start with or type \'QUIT\': ')
response = input('> ')


while response != 'QUIT':

    if not response.isdecimal() or response == '0':
        print('I\'m sorry but you must enter an integer greater than 0.')
        print('Please try again.')
        print('Enter the number (greater than 0) you would like to start with or type \'QUIT\': ')
        response = input('> ')

    if response == 'QUIT':
        sys.exit()

    n = int(response)
    print(n, end='', flush=True)
    while n != 1:
        if n % 2 == 0:  # If the number is even, divide it by two.
            n = n // 2
        else:  # If the number is odd, triple it and add one.
            n = 3 * n + 1

        print(', ' + str(n), end='', flush=True)
        time.sleep(0.1)
    print()
    print('Enter the number (greater than 0) you would like to start with or type \'QUIT\': ')
    response = input('> ')
