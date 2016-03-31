# Hangman game

import random
import string
import os.path

fileName = str(os.path.dirname(__file__)) + r"\words.txt"

def getWords(fileName):
    """
    Input: a file only containing words in one line.
    Return: a valid words at random. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    fileHandle = open(fileName, 'r')
    line = fileHandle.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist).lower()

targetWord = getWords(fileName)

def isValid(userInput):
    '''
    Input: a string containing user input.
    Return: a boolean value, True if userInput is valid.

    Guarantee userInput to meet the following constraints:
    * userInput.length = 1
    * only alphabet accept
    * ignore case
    '''
    if len(userInput) == 0 or len(letterInput) > 1:
        return False
    else:
        return letterInput.isalpha()



'''
def isWordGuessed(letterGuessed, target):

def getGuessedWord(letterGuessed, target):

def narrowRange(letterGuessed):


def hangman():
'''

