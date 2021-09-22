# Amar Nagim
# Je kunt herhaald getallen raden
# het spel stopt na 20 te raden getallen of als je aangeeft (eerder) te willen stoppen. Elke te raden getal heet een ronde. Het spel heeft dus maximaal 20 ronden.
# Het programma neemt een random geheim te raden getal in gedachten tussen de 1 en de 1000
# Je mag 10 keer raden. Is het dan nog niet geraden, dan stopt die ronde.
# Voor elk geraden getal wordt de score opgehoogd met 1. Je kunt dus maximaal 20 punten scoren.
# Na elke gok geeft het programma antwoord:
# geraden, of hoger of lager
# Als het (absolute) verschil tussen het getal dat jij gokt en het geheime te raden getal kleiner is dan 50 dan meldt het programma in de terminal: 'Je bent warm’
# Als het (absolute) verschil tussen het getal dat jij gokt en het geheime te raden getal kleiner is dan 20 dan meldt het programma in de terminal: 'Je bent heel warm’
# Na elke ronde meldt het programma de score tot dan toe in de terminal
# Na elke ronde vraagt het programma: ‘Nog een getal raden?’ tenzij er al 20 ronden zijn geweest.
# Aan het einde meldt het programma de eindscore.
# Tip: begin met het automatiseren van alleen de ronde


import time
import random
import sys



print("""
You will attempt to guess the random chosen number. It will always be between 1 and 1000.
You\'ll get 20 rounds. Every round consists of 10 guesses. If you haven\'t guessed the right number
within 10 tries the game will ask you if you want to continue to the next round, or if you want to quit the game.
At the end of the game and each round you will be prompted with your score. (the maximum possible score is 20)""")

print()

def a_round(round_count):
    score = 0
    print(F"This is round: {round_count}/20")
    print()

    number = random.randint(1, 1000)
    print(number)
    print('Random number has been generated.')
    print('')
    time.sleep(1)
    print('Guess a number between 1 and 1000')
    print(f'Attempt 1/10')
    for guess_count in range(10):
        guess_count +=1
        guess = int(input('Your guess: '))
        print()
        difference = guess - number

        if guess != number:
            if guess_count == 10:
              print('Unfortunately you haven\'t guessed the right number.')
              continueOrBreak = input("Press Enter to continue and 'Q' if you want to stop...").lower()
              print()
              if continueOrBreak == 'q':
                print(F'Your score is: {score}/{round_count}')
                print(F'{round_count = }')
                raise SystemExit
              elif continueOrBreak == '':
                print(F'Your current score is: {score}/20')
                break
            else:
              guess_count += 1
              print(f'Attempt {guess_count}/10')
              print()

        if guess == number:
         print('You\'ve guessed the right number!')
         score += 1
         print()
         continueOrBreak = input("Press Enter to continue and 'Q' if you want to stop...").lower()
         print()
         if continueOrBreak == 'q':
          print(F'Your score is: {score}/{round_count}')
          print(F'{round_count = }')
          raise SystemExit
         else:
          print(F'Your current score is: {score}/20')
          break

        elif difference <= 20 and difference >= 1 or difference <= -1 and difference >= -20:
          print('You are very warm..')
        elif difference <= 50 and difference >= 1 or difference <= -1 and difference >= -50:
          print('You are warm..')    

        if guess < number: 
          print('Tip: higher')
        elif guess > number:
          print('Tip: lower')    

for round_count in range(1, 21):

    a_round(round_count)

