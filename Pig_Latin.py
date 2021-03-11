"""Moving Around first cosonants and adding 'ay' or 'way if vowels to form Pig Latin"""
# Filip Serwinski
# Impractical Python Projects
# Project #2, Pig Latin

import sys
import re


def word_check(word):
    """Check the beginning of letter of the word and apply rules"""
    """Rule 1: if consonant, move it to the end and add 'ay'"""
    """Rule 2: if vowel, add 'way' at the end"""
    p = re.compile('[A-Za-z]')
    check = p.match(word)
    print(check)

    if check is None:
        print('bad')
    else:
        first_letter = re.compile('[aeiouy]')
        vowel_check = first_letter.match(word)

        if vowel_check is None:
            "print('consonant')"
            word = word[1:None] + word[0] + 'ay'
            "print(word)"
            return word
        else:
            "print('vowel')"
            word = word + 'way'
            "print(word)"
            return word


def main():
    """Input from User, validate that it is a word"""
    print("Welcome to 'Pig Latin' \n")

    while True:
        word = input("Enter any English word else n to quit\n")

        word = word_check(word)
        print(word)

        if word.lower() == 'n':
            exit()


if __name__ == "__main__":
    main()