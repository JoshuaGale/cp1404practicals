"""Joshua Gale"""

LETTER_FREQUENCY = 3


def main():
    odd_letter_name = ""

    name = get_name()
    letter_frequency = get_letter_frequency()
    odd_letter_name = get_every_second_letter(name, odd_letter_name, letter_frequency)
    print(odd_letter_name)


def get_every_second_letter(name, odd_letter_name, letter_frequency):
    for char in range(len(name)):
        if char % letter_frequency == letter_frequency - 1:
            odd_letter_name += name[char]
    return odd_letter_name


def get_name():
    name = input("What is your name: ")
    while name == "":
        print("Please enter a valid name: ")
        name = input("What is your name: ")
    return name


def get_letter_frequency():
    isvalid = False
    while not isvalid:
        try:
            letter_frequency = int(input("What is the interval you want to print letters at?: "))
            isvalid = True
        except:
            print("invalid letter frequency")
    return letter_frequency

main()
