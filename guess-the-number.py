import random

secret_number = random.randint(1,20)
print("I am thinking of a number between 1 to 20")


#Ask player to guess the numeber but keep in mind he/she has only six chance as i will add a range of 1 to 7 below:

for guessTaken in range(1,7):
    print("Take a guess:")
    guess = int(input())

    if guess <secret_number:
        print("Your Guess is too low.")
    elif guess > secret_number:
        print("Your Guess is too high.")
    else:
        break

    if guess == secret_number:
        print("You guess the secret number on" +str(guessTaken)+ " guesses ")
    else:
        print("Sorry! you couldn't guess the right number. ")
        print("The num i was thinking of was", secret_number, ".")
