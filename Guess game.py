 #----guess game
import random
random = random.Random()
secret_number = random.randint(1,9)
user_guess = int(input('guess number btween 1 and 9:'))
if user_guess == secret_number:
    print("You win!")
else:
    print("You lose!")
