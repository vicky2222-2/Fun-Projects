""" convent the word it in to differ meaning words with same letters"""

#importing load dictionary for converting the text file into the list of words
import load_dictionary

word_list = load_dictionary.load('wordsforanargms.txt')

#for holding anargms
anargms = []
user_word = input("enter the word for anargms:")
user_word = user_word.lower()

# sort the words and find anargms
for word in word_list:
    sorted_word =  sorted(word)
    if word != user_word:
        if sorted(user_word) == sorted_word:
            anargms.append(word)

if len(anargms) == 0:
    print("\n entered dictionary is enough or enter new word")

else:
    print(f"anargms for the word \"{user_word}\" is {anargms}")
