"""Joshua Gale"""


def main():
    name = get_name()
    letter_frequency = get_letter_frequency()
    print_parts(name, letter_frequency)


def print_parts(name, letter_frequency):
    print(name[::letter_frequency])


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
