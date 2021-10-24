# https://nostarch.com/big-book-small-python-programming (BSD Licensed)
# Fibonacci Sequence
# Calculates numbers of the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13...

import sys

print('''Fibonacci was not the first to know about the sequence, it was known
in India hundreds of years before! His real name was Leonardo Pisano Bogollo,
and he lived between 1170 and 1250 in Italy. "Fibonacci" was his nickname, which
roughly means "Son of Bonacci". As well as being famous for the Fibonacci Sequence,
he helped spread Hindu-Arabi Numerals (like our present numbers 0, 1, 2, 3, 4, 5,
6, 7, 8, 9) through Europe in place of Roman Numberals (I, II, III, IV, V, etc).
Fibonacci Day is November 23rd, as it has the digits "1, 1, 2, 3" which is part
of the sequence. The Fibonacci sequence begins with 0 and 1, and the next number
is the sum of the previous two numbers. The sequence continues forever:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987...

To use this program, enter the length of the sequence you would like to generate
below. The higher number you choose the more of the sequence will be generated and
the longer it will take.\n''')

while True:  # Main program loop.
    
    while True:  # Keep asking until the user enters valid input.
        
        print('Enter the Nth Fibonacci number you wish to')
        print('calculate (such as 5, 50, 1000, 9999), or QUIT to quit:')
        response = input('> ').upper()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break  # Exit the loop when the user enteres a valid number.

        print('Please enter a number greater than 0, or QUIT.')
    print()

    # Handle the special cases if the user entered 1 or 2:
    
    if nth == 1:
        print('0')
        print()
        print('The #1 Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('The #2 Fibonacci number is 1.')
        continue

    # Display warning if the user entered a large number:
    
    if nth >= 10000:
        print('WARNING: This will take a while to display on the')
        print('screen. If you want to quit this program before it is')
        print('done, press Ctrl-C.')
        input('Press Enter to begin...')

    # Calculate the Nth Fibonacci number:
    
    secondToLast = 0
    last = 1
    NumCalculated = 2
    print('0, 1, ', end='')  # Display the first two Fibonacci numbers.

    # Display all the later numbers of the Fibonacci sequence:
    
    while True:
        nextNum = secondToLast + last
        NumCalculated += 1

        # Display the next number in the sequence:
        
        print(nextNum, end='')

        # Check if we've found the Nth number the user wants:
        
        if NumCalculated == nth:
            print()
            print()
            print('The #', NumCalculated, ' Fibonacci ',
                  'number is ', nextNum, sep='')
            break

        # Print a comma in between the sequence numbers:
        
        print(', ', end='')

        # Shift the last two numbers:
        
        secondToLast = last
        last = nextNum
