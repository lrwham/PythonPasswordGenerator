import menu
import generator

run = True

while run:
    wordlist = menu.choose_wordlist()
    length = menu.choose_length()

    # print(wordlist)
    # print(length)

    print() # blank line
    print(generator.create_passphrase(wordlist, length))
    print() # blank line