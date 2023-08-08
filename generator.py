import random

# The word lists may include line numbers and white space.
def strip_string(s):
    return ''.join(char for char in s if char.isalpha())

def create_passphrase(wordlist, length):
    words = []
    
    with open(wordlist, 'r') as f:
        words = f.readlines()

    passphrase = ""

    for i in range(length):
        # choose random word
        # strip line numbers and white space
        # capitalize for easier recognition
        word = random.choice(words)
        word = strip_string(word)
        word =  word.title()

        passphrase += word

    return passphrase