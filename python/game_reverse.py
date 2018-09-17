# Game where computer guesses Your number!
# Smartninja.lv homework

print("Hey, please imagine the number from 1 to 100. I will try to guess it.")
input("Press ENTER when ready...")

min = 1
max = 100

iter = 1

while True:
    computer_guess = min + ((max - min) // 2)
    print("My guess is: " + str(computer_guess))
    print("If actual number is smaller, press s")
    print("If actual number is larger, press l")
    print("If I have guessed correctly, press c")
    print("if You want to quit, press q")
    user_input = input("Your choice: ")
    user_input = user_input.lower()

    if user_input == "q":

        print("Good bye! Thanks for playing.")
        break  # allows to terminate loop
    if user_input == "c":
        print("Nice!!! I did it in " + str(iter) + " moves. Thanks for playing.")
        break  # allows to terminate loop
    if user_input == "l":
        print("Ok, let me think ...")
        min = computer_guess + 1
    if user_input == "s":
        print("Ok, let me think...")
        max = computer_guess - 1
    print("\n\n")  # \n is special symbol for ENTER

    iter += 1

