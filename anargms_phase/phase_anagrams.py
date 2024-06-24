
""" creating the anagram phase from name with user choice"""

import sys
import load_dictionary
from collections import Counter
from pprint import pprint

#global variable

#load_dictionary convert the text file in to the list
word_list = load_dictionary.load('wordsforanargms.txt')

User_name = input("Enter your name: ")
#joining the string without gaps
User_name = ''.join(User_name.lower().split())

def find_anargms(name, wordlist):
    """ Find the anargms from the given name and dictionary list"""

    # empty list for holding anargms
    anargms = []
    username_map = Counter(name)

    for word in wordlist:
        word_map = Counter(word)
        # Using test to allow the anargms that are lower len than name
        # for example:  name = ballet anargms = ball,bat,tab etc
        test = ""
        for letter in word:
            if word_map[letter] <= username_map[letter]:
                test += letter

        if Counter(test) == word_map:
            anargms.append(word)

    pprint(anargms)
    print(f"remaining number of the words: {len(name)}")
    print(f"remaining number of anargms: {len(anargms)}")


def user_choice(name):

    """ getting the choice from user for anargms"""

    while True:
        choice = input("Enter the choice from above words (OR) Press enter to start over (OR) enter # to exist:")

        # if user enter then end the process
        if choice=="":
            main()

        elif choice == "#":
            sys.exit()

        else:
            canditates = "".join(choice.lower().split())

        # check the choice is correct or wrong
        left_of_list = list(name)

        for letter in canditates:
            if letter in left_of_list:
                left_of_list.remove(letter)

        if (len(name) - len(left_of_list))==len(canditates):

            print("your choice is correct")
            break

        else:
            print("you made a wrong choose so enter the choose again")
            continue

    name = "".join(left_of_list)
    return choice,name


def main():
    """ creating anagrams phase using limit"""

    name = "".join(User_name.lower().split())
    name = name.replace("-","")

    limit = len(name)
    phase = ""
    running = True

    while running:
        temphase = phase.replace(" ","")

        if len(temphase) < limit:

            find_anargms(name,word_list)

            print(f"The current phase:{phase}")
            choice, name = user_choice(name)

            phase += choice + " "

        elif len(temphase) == limit:

            print("PROCESS IS FINISED")
            print(f"The anargms phase: {phase}")


            try_again = input("Press enter for try again or n for quit")

            if try_again == 'n':
                running = False
                sys.exit()

            else:
                main()


if __name__ == '__main__':
    main()













