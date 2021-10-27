# Numeral System Counters
# Shows equivalent numbers in decimal, hexadecimal, and binary.
# https://nostarch.com/big-book-small-python-programming (BSD Licensed)

print('''We all know how much we love converting from decimal to
binary or hexadecimal and back again. After all, we do it all the
time just for the thrill of it. Even so, it can sometimes get a
little tedious which is why this program asks you which numbers you
would like to display and then shows you the equivalent numbers in
decimal (base 10), hexadecimal (base 16), and binary (base 2) numeral
systems.

If at any time you want to do this yourself and are tired of the computer
doing it for you, simply press Ctrl-C to quit.
''')

while True:
    response = input('Enter the number you would like to start at (e.g. 0) > ')
    if response == '':
        response = '0'  # Start at 0 by default.
        break
    if response.isdecimal():
        break
    print('Please enter a number greater than or equal to 0.')
start = int(response)

while True:
    response = input('Enter how many numbers would you like to display (e.g. 1000) > ')
    if response == '':
        response = '1000'  # Display 1000 numbers by default.
        break
    if response.isdecimal():
        break
    print('Please enter a number: ')
amount = int(response)

for number in range(start, start + amount):  # Main program loop.
    # Convert to hexadecimal/binary and remove the prefix:
    hexNumber = hex(number)[2:].upper()
    binNumber = bin(number)[2:]

    print('DEC: ', number, '   HEX: ', hexNumber, '   BIN: ', binNumber)
