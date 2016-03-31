# Hangman game

import random
import string
import os.path

fileName = str(os.path.dirname(__file__)) + r"\words.txt"

def loadWords(fileName):
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    fileHandle = open(fileName, 'r')
    line = fileHandle.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def chooseWord(wordlist):

'''
def isLegal(input):

def isWordGuessed(letterGuessed, target):

def getGuessedWord(letterGuessed, target):

def narrowRange(letterGuessed):


def hangman():
'''

hangman()
