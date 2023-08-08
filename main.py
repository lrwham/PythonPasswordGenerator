import menu
import generator

wordlist = menu.choose_wordlist()
length = menu.choose_length()

print(wordlist)
print(length)

print(generator.create_passphrase(wordlist, length))