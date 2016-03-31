# Hangman game

import random
import string
import os.path

fileName = str(os.path.dirname(__file__)) + r"\words.txt"

def getWords(fileName):
    """
    Input: a file only containing words in one line.
    Return: string, a lowercase words pick up at random.

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
    Input: string, containing user input.
    Return: boolean value, True if userInput is valid.

    Guarantee userInput to meet the following constraints:
    * userInput.length = 1
    * only alphabet accept
    * ignore case
    '''
    if len(userInput) == 0 or len(userInput) > 1:
        return False
    else:
        return userInput.isalpha()

def showCharGuessed(charGuessed, targetWord, guessed):
    '''
    charGuessed: list, storing letters have been guessed.
    targetWord: string, storing the secret word the user is guessing.
    guessed: boolean value, True if targetWord is guessed.
    Return: string, comprised of letters and underscores that represents
        what letters in secretWord have been guessed.
        eg. '_ _ _ a _'
    '''
    tagetLength = len(targetWord)
    showGuessed = ''

    # Initialize as '_ _ _ _ _'
    if len(charGuessed) == 0:
        for i in range(tagetLength):
            showGuessed += '_ '
    # Base on targetWord, append character properly
    elif not guessed:
        for i in range(tagetLength):
            if targetWord[i] in charGuessed:
                showGuessed = showGuessed + targetWord[i] + ' '
            else:
                showGuessed = showGuessed + '_ '
    # Show answer when fully guessed
    else:
        showGuessed = targetWord
    return showGuessed

'''
def isWordGuessed(letterGuessed, target):

def getGuessedWord(letterGuessed, target):

def narrowRange(letterGuessed):


def hangman():
'''

