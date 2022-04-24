# import only system from os
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


clear()
print("First enter a string to be guessed.")
word = str(input("Type a string: "))
word = word.upper()
print("Now enter how many wrong guesses to give.")
num_of_guesses = int(input("Type an integer: "))
progress = int(0)
i = 0
clear()
print("Wrong Guesses left:", num_of_guesses)
while num_of_guesses > 0:
    letter_to_check = str(input('Type a letter to check: '))
    letter_to_check = letter_to_check.upper()
    string_length = (len(word)-word.count(" "))
    num_of_times = word.count(letter_to_check)
    progress += num_of_times
    i += 1
    if num_of_times > 0:
        print("Correct guess! You have %s / %s letters so far!" % (progress, string_length))
        print("Wrong Guesses left:", num_of_guesses)
        if progress == string_length:
            print("You won in %s guesses!" % i)
            break
    else:
        num_of_guesses -= 1
        print("Incorrect guess. %s tries remaining" % num_of_guesses)
if num_of_guesses == 0:
    print("You lose.  No more wrong guesses left.")
