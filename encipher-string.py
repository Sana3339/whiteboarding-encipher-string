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

    alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



    new_txt = []

    for char in txt:            #abcxyz, shift =3
        make_uppercase = False
        if char.isalpha():      #'x'
            if char.isupper() == True:
                make_uppercase = True       #make_uppercase = False
            char = char.lower()
            char_idx = alpha_list.index(char)   #char_idx = 23
            new_char_idx = char_idx + shift     #new_char_idx = 26
            if new_char_idx >= 26:
                new_char_idx -= 26
            new_char = alpha_list[new_char_idx]     #new_char = 'a'
            if make_uppercase == True:
                new_char = new_char.upper()
            new_txt.append(new_char)

        else:                                   #new_txt = ['d', a']
            new_txt.append(char)

    return ''.join(new_txt)






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
