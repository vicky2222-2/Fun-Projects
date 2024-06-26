""" This is a prototype of decoding route ciper"""

#  Pseudo code for clarity:
# 1. load the ciper text
# 2. Spilt the word in the ciper text and create list to hold it.
# 3. Get input of rows and cols
# 4. Get input the ciper key
# 5. Convert the key into spilted number in list
# 6. create a list to hold transposed matrix
# 7. for everynumber in ciper key:
# 8.    Create a newlist that append every n items in the ciper_list
# 9.    reverse the newlist if it is negative,if not then do nothing
# 10.   append this newlist to the transposed matrix
# 11.create ciper text to decoded list
# 12.for row in rows:
# 13.   create a emtpy list to hold last word
# 14.   for transposed_list in the transposed matrix
# 15.        remove the last word from the transposed_list
# 16.        add this last word to the ciper text



encrypted_text = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
ciper_list = list(encrypted_text.split(" "))

rows, cols = 5 , 4
key = [-1,2,-3,4]

start = 0
stop = rows

transposed_list = [None] * cols # creating empty nexted list

for num in key:
    new_list = ciper_list
    if num < 0:
        transposed_list[abs(num)-1] = new_list[start:stop]
    elif num > 0:
        transposed_list[abs(num)-1] = list(reversed(new_list[start:stop]))
    stop += rows
    start += rows

print(f" The transposed matrix:{transposed_list}")

decrypted_text = ""

#loop through nested list to pop off last item to text
for row in range(0,rows):
    for col_list in transposed_list:
        decrypted_text += str(col_list.pop()) + " "

print(f"\n\nciper text:{decrypted_text}")
