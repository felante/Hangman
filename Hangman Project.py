import random

def display_interface(solution, interface):
    print('\n')
    for x in range(len(solution)):
        print(interface[x], end='')
    print('\n')

def game(solution: str):

    # user gets 7 guesses
    lives = 7
    # list of incorrect guesses
    incorrect_letters = []
    # list of correct guesses
    correct_letters = []
    # empty dictionary that will be used for the UI
    interface = {}
    # condition for the game function to continue
    guessing = True

    # initializes interface
    for x in range(len(solution)):
        interface[x] = '_'

    display_interface(solution, interface)

    while guessing == True and lives > 0:
        guess = input("Guess a letter or the solution")

        # activates if the user is guessing the word
        if len(guess) > 1:
            # prints "You Won!" if user guessed correctly
            if guess == solution:
                print(f"You won! The word was {solution}!")
                guessing = False
            # prints "You guessed incorrectly." and decrements lives of user
            else:
                print(f"You guessed incorrectly. The word was not \"{guess}\".")
                lives -= 1
                print(f"You have {lives} guess(es) remaining.")
                display_interface(solution, interface)
                if lives == 0:
                    print(f"The word was {solution}.")

        # activates if the user is guessing one character
        elif len(guess) == 1:
            # prevents user from guessing a character they have already guessed.
            while guess in incorrect_letters + correct_letters:
                print(f"Guessed characters: {incorrect_letters + correct_letters}")
                guess = input("Please enter a character you have not already guessed.")
            # activates if guess is correct
            if guess in solution:
                # appends to the correct letters list
                correct_letters.append(guess)
                # updates dictionary/interface to reflect guessed letters in their correct position
                for x in correct_letters:
                    count = 0
                    for y in solution:
                        if x == y:
                            interface[count] = x
                        count += 1
                display_interface(solution, interface)
                # checks if user has spelled the entire word without guessing it
                if set(correct_letters) == set(solution):
                    print(f"You won! The word was \"{solution}\"!")
                    guessing = False
            # activates if guess is incorrect
            else:
                # appends guess to incorrect letters list
                incorrect_letters.append(guess)
                print(f"'{guess}' is not in the word.")
                lives -= 1
                print(f"You haves {lives} guess(es) remaining.")
                display_interface(solution, interface)
                if lives == 0:
                    print(f"The word was {solution}.")

        # activates if the user inputs no guess
        elif len(guess) == 0:
            print("Don't give up!")
            display_interface(solution, interface)

def main():
    words = ["banana", "apple", "orange", "strawberry", "grape", "cherry", "mango", "pear", "peach", "lemon", "tomato", "potato", "lettuce", "carrot", "onion", "pumpkin", "broccoli", "eggplant", "spinach", "corn"]

    solution = random.choice(words)
    playing = True

    while playing == True:
        game(solution)
        answer = input("Enter '1' to play again.")
        if answer == '1':
            # selects random word
            solution = random.choice(words)
            playing = True
        else:
            playing = False

    print("Thanks for playing!")

if __name__ == "__main__":
    main()