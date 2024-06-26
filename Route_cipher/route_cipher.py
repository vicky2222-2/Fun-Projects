"""
                    Decrypting the text along route cipher

     This project is for the whole-word transposition coloumn with the given row and column.
     Key is used to get the direction of the column to be transpoted
     The goal is to get the decrypted text with the given key.

    Example below the show the direction of the encrypted route:

      the matrix of 4x5:

            Key: -1,2,-3,4

             ___ ___ ___ ___
            | ^ | | | ^ | | | MESSAGE IS WRITTEN
            |_|_|_v_|_|_|_v_|
            | ^ | | | ^ | | | ACROSS EACH ROW
            |_|_|_v_|_|_|_v_|
            | ^ | | | ^ | | | IN THIS MANNER
            |_|_|_v_|_|_|_v_|
            | ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
            |_|_|_v_|_|_|_v_|
START END

Required input : text message, no of rows and cols, key

"""
#========================================================================================================
# user input

#encrypted text for decoding
encrypted_text = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

# no of rows and cols for transposing
rows, cols = 5 , 4

#key with space between number for spliting
key = "-1 2 -3 4"

# USER input finished =================================================================================


def main():
    """ run program and get decrypted plaintext"""

    # spliting every word to make list
    ciper_list = list(encrypted_text.split(" "))

    #checking the rows and cols having enough for ciper list
    valide_ciper_list(ciper_list)
    key_int = array_int(key)
    translation_matrix = build_matrix(key_int, ciper_list)
    plaintext = decrypt(translation_matrix)
    print("Plaintext = {}".format(plaintext))

def valide_ciper_list(ciper_list):
    """ for checking the row and column with the ciper_list for matrix"""


    # lenght  of the ciper_list
    len_ciper = len(ciper_list)

    validate_row_x_cols = []
    for matrix_size in range(2,rows): # excluding the one row matrix
        if len_ciper % matrix_size == 0:
            validate_row_x_cols.append(matrix_size)

    #checking for row x col are valide matrx
    if rows*cols != len_ciper:
        print("entered rows and cols are not right with given message:")
        print(f" The valide rowXcol are: {validate_row_x_cols}")


def array_int(key):
    """ spliting the text key in to integer list and check for any mistakes in key"""

    splited_key = list( int(i) for i in (key).split(" "))

    # lowest value in keys
    low_key = int(min(splited_key))
    # highes value in keys
    high_key = int(max(splited_key))

    #check for any mistakes in the key

    if len(splited_key) != cols or low_key < -cols or high_key >cols:
        print("your key is wrong")
    else:
        return splited_key

def build_matrix(key_int, cipherlist):
    """Turn every n items in a list into a new item in a list of lists."""
    translation_matrix = [None] * cols
    start = 0
    stop = rows
    for k in key_int:
        if k < 0:  # read bottom-to-top of column
            col_items = cipherlist[start:stop]
        elif k > 0:  # read top-to-bottom of columnn
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k) - 1] = col_items
        start += rows
        stop += rows
    return translation_matrix


def decrypt(translation_matrix):
    """Loop through nested lists popping off last item to a string."""
    plaintext = ''
    for i in range(rows):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + ' '
    return plaintext

if __name__ == '__main__':
    main()

