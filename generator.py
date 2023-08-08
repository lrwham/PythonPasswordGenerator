import random

def strip_string(s):
    return ''.join(char for char in s if char.isalpha())

def create_passphrase(wordlist, length):
    words = []
    
    with open(wordlist, 'r') as f:
        words = f.readlines()
    
    words = [strip_string(word) for word in words]

    passphrase = ""

    for i in range(length):
        passphrase += random.choice(words).title()

    return passphrase