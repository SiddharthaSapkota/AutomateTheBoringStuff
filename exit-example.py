import sys

while True:
    print("Type exit to exit this while loop.")
    response = input()
    if response == "exit":
        print("You typed correctly. ")
        sys.exit()
    print("Your respose was " + response + ". ")