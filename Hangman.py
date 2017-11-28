# Derek D
# Hangman Puzzle Game
# 11/1



def show_start_screen():
    print("********************")
    print("* Guess the Word!  *")
    print("********************")

def show_credits():
    print("****************************************************************")
    print("* This game was created by Derek and was completed on 11/17/17 *")
    print("****************************************************************")

def get_puzzle():
    return "hangman"

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def ask_name():
    print("What is your name?")
    name = input()
    return name

def get_guess(name):
    guess = input("C'mon" + " " + name + "!" + " " + "Enter a letter: ")
    return guess

def display_board(solved):
    print(solved)

def show_result(name):
    print("You Win" + " " + name + "!")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n)   ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
           return False
        else:
            print("What? I don't understand.  Please enter 'y' or 'n'.")
    
show_start_screen()
name = ask_name()
    
def play():
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)

    strikes = 6
    limit = 6

    print(solved)

    while solved != puzzle:
        letter = get_guess(name)

        if letter not in puzzle:
            strikes -= 1
            if strikes == 0:
                print("You lose" + " " + name + "!" + " " + "The word was" + " " + puzzle + "!") 
            
       
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)

    show_result(name)

playing = True

while playing:
    play()
    playing = play_again()
   
