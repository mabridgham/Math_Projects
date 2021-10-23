# https://nostarch.com/big-book-small-python-projects
# Cho-Han
# The traditional Japanese dice game of even-odd.

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-han is an intrinsic part of Japanese culture, with the game
stretching back centuries in its popularity. It was originally played by
bakuto, who were nomadic gamblers who moved from town to town winning bets
off the local people. They are considered forerunners of organised crime
groups like the Yakuza, among whom Cho-han is still popular today.

The rules of Cho-han quite simple. To play, a dealer shakes two dice inside
a bamboo cup, then turns it over to conceal the dice within. At this point,
players must place their bets on whether the total of the numbers on the
upturned faces of the dice will be even (Cho) or odd (Han).

In this program, you are in a Japanese gambling house. The game of choice is
Cho-Han. The stakes are high. You have 5000 coins in your purse to start. See
if you can win but be careful or the Yakuza may just think you are cheating and
a money will be the least of your problems.
''')

purse = 5000
while True:  # Main game loop.
    
    # Place your bet:
    
    print('You have', purse, 'mon. How much do you dare to bet? (or QUIT)')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Hey! Come back! We weren\'t done playing yet!!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            
            # This is a valid bet.
            
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer smiles as he swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    
    print('Slowly the dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine if the player won:
    
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    
    if playerWon:
        print('You won! The dealer eyes you suspiciously as you take', pot, 'mon.')
        purse = purse + pot  # Add the pot from player's purse.
        print('The dealer smiles as the house collects a', pot // 10, 'mon fee for it\'s troubles.')
        purse = purse - (pot // 10)  # The house fee is 10%.
    else:
        purse = purse - pot  # Subtract the pot from player's purse.
        print('The dealer laughs as he takes your money. Too bad. That\'s rotten luck! Dare to try again friend?')

    # Check if the player has run out of money:
    
    if purse == 0:
        print('Hmm. Looks like your well has run dry my friend. Come back again when you have more money.')
        print('Better luck next time!')
        sys.exit()
