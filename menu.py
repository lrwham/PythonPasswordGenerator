def print_help_choosing():
    print("After choosing a list, you will be asked to enter a length.")
    print("The length determines how many words will be in your passphrase.")
    print("1. EFF's Long Wordlist has the longest words. Longer words may be more secure and may also be easier (or harder) to remember.")
    print("2. EFF's Short Wordlist #1 has shorter words. Shorter words may be less secure, but will definetly be overall shorter in length.")
    print("3. EFF's Short Wordlist #2 has short, but slightly longer than list #1, words. These may be more memorable.")


def choose_wordlist():
    print("Choose a wodlist:")
    print("1. EFF's Long Wordlist")
    print("2. EFF's Short Wordlist #1")
    print("3. EFF's Short Wordlist #2")
    print("4. Help me choose")
    numerical_choice = '0'

    while numerical_choice not in ['1','2','3']:
        numerical_choice = input("Enter your choice: ")

        if numerical_choice == '4':
            print_help_choosing()

    if numerical_choice == '1':
        return "wordlists/eff_large_wordlist.txt"
    elif numerical_choice == '2':
        return "wordlists/eff_short_wordlist_1.txt"
    elif numerical_choice == '3':
        return "wordlists/eff_short_wordlist_2_0.txt"

def choose_length():
    print("Choose a length for your passphrase")
    length = ""

    while length.isnumeric() == False or int(length) < 1:
        length = input("Enter a number: ")
        if length.isnumeric() and int(length) > 0:
            return int(length)

