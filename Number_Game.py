#Creating Guessing the number game
import random

guesses = 1
comp_num = random.randint(1,10)
print("Hello there!! Take a guess between 1 to 10")

while(guesses <= 5):
    your_num = int(input("Your Number: "))
    
    guessesLeft = 5 - guesses
    guesses += 1
    
    
    if your_num < comp_num:
        print(f"Your guess is low!! You have {guessesLeft} guesses left.")

    elif your_num > comp_num:
        print(f"Your guess is high!! You have {guessesLeft} guesses left.")

    else:
        if your_num == comp_num:
            break

if your_num == comp_num:
    print(f"Good Job !! You guessed the number in {guesses-1} tries")

if your_num != comp_num:
    print("Sorry, You lost it!! The number is : {}".format(comp_num))
  

    
