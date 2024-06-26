"""

             Encrypt a Civil War 'rail fence' type cipher.


         This is for a "2-rail" fence cipher for short messages.
         Example text to encrypt: 'Buy more Maine potatoes'
         Rail fence style: B Y O E A N P T T E
                            U M R M I E O A O S
              Read zigzag: \/\/\/\/\/\/\/\/\/\/
         Encrypted: BYOEA NPTTE UMRMI EOSOS
"""
#------------------------------------------------------------------------------

def main ():
    """ for encrypting the message and run the programs """

    # looping for trying again
    while True:
        # user input

        # inputing the meassage need to encrypted
        message = input("enter the message to encrypted:")

        # inputing how many it need to be encrypted
        times = int(input("Enter how many times it need to encrypted:"))

        # user input finished

        i = 0
        #looping for repeating the encryption until given times finished
        while i < times:
            # preparping message for encryption
            pre_message = prep_for_encryption(message)

            railed_message = railing_message(pre_message)
            encrypted_message = encrypt(railed_message)
            message = encrypted_message
            i += 1

        print(f"The encrypted message:{message}")

        #for trying the encrytion again
        try_again = (input("press enter for try again or n for quit")).lower()
        if try_again == 'n':
            break
def prep_for_encryption(message):

    """ removing the space and joining the message and make it capital"""
#    print(f"{message}")
    pre_message = ("".join(message.split())).upper()

    return pre_message

def railing_message(message):
    """ shuffling the letter according to the rail fence(zigzag) shape"""

    # making upper and lower row for zigzag
    upper_row = message[::2]
    lower_row = message[1::2]

    Shuffled_message = upper_row+lower_row

    return Shuffled_message

def encrypt(message):
    """ encrypting the message by dividing 5 parts the railed message """

    encrypting_message = " ".join(message[0 + i:5+i] for i in range(0,len(message),5) )

    return encrypting_message

if __name__ == "__main__":
    main()