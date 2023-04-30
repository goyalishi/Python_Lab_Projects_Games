'''*************************GUESS THE NUMBER***********************'''
import random
comp=random.randint(1,100)
print("Guess a number between 1-100")
user=int(input("Please enter your guessed number"))
trial=1
while(user!=comp):
    print("Sorry!! you guessed a wrong number")
    if (user>comp):
        print("number guessed is high")
    else:
        print("number guessed is low")
    
    user=int(input("Again guess a number:"))
    trial+=1

print("congratulations!!!!")
print("You nailed it!")
print(f"You guessed the number in {trial} trials")