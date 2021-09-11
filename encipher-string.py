"""Write a function that encrypts a string with a variable rotary cipher.

The function should take in a number and string and shift the string's
characters by that number:

>>> rot_encode(1, 'abcxyz')
'bcdyza'

It should be able to shift characters by any number:

>>> rot_encode(3, 'abcxyz')
'defabc'

It should preserve capitalization, whitespace, and any special characters:

>>> rot_encode(1, 'Wow! This is 100% amazing.')
'Xpx! Uijt jt 100% bnbajoh.'
"""


def rot_encode(shift, txt):
    """Encode `txt` by shifting its characters to the right."""

    #create a new string to hold our final answer
    encoded_string = ""

    #create rotary alphanumeric dictionary
    alpha =

    #for index of each letter in txt, add the shift number to get the index of the new letter

    #use the dictionary to look up index

    #append new letter to our string




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
