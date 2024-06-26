"""

          Decrypt a Civil War 'rail fence' type cipher.

       This is for a 2-rail fence cipher for short messages.

     Example plaintext: 'Buy more Maine potatoes'
     Rail fence style: B Y O E A N P T T E
                        U M R M I E O A O S
     Read zigzag: \/\/\/\/\/\/\/\/\/\/

     Ciphertext: BYOEA NPTTE UMRMI EOSOS
"""

import itertools
import math

def main():

    """ run the program and decrypt the message"""

    # looping for trying again
    while True:
        # get the input of message need to be decoded
        message = input(" the message need to be decoded:")

        # inputing how many it need to be encrypted
        times = int(input("Enter how many times it need to encrypted:"))
        i = 0
        while i < times:
            # prepare the message for decoding
            prep_decode = prepare_message(message)

            ROW1, ROW2 = split_message(prep_decode)
            plain_text = decrypt(ROW1, ROW2)

            message = plain_text
            i += 1

        print(f"plain text: {plain_text}")

        # for trying again until pressing n
        try_again = (input("press enter for try again or n for quit")).lower()
        if try_again=='n':
            break

def prepare_message(message):

    """ remove the space and join the text"""
    prep_decode = "".join(message.split())
    return prep_decode

def split_message(message):
    """ split the message into two part for decode"""
    len_row1 = math.ceil(len(message)/2)

    row1 = message[:len_row1]
    row2 = message[len_row1:]

    return row1,row2

def decrypt(row1, row2):

    """ Join the two row using zigzag join to decrypt"""

    final_list = []
    for Row1, Row2 in itertools.zip_longest(row1,row2):
        #append the Row1,Row2 for join it later
        final_list.append(Row1)
        final_list.append(Row2)

    plaintext = "".join(final_list)
    return plaintext

if __name__ == '__main__':
    main()