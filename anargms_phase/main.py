""" convent the word it in to differ meaning words with same letters"""
#psuedocode for clarity

# 1. load the dictionary
# 2. convert it in to word_list
# 3. empty list for holding anargms
# 4. Get the word from the user and make it lower for use
# 5. for word in word_list
# 6.    sorted the word
# 7.    if the word not equal to user_word:
# 8.         if sorted_user_word equal to sorted_word
# 9.              add the word to the empty list anargms
# 10. printing the anargms


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
