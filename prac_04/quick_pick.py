import random
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("how many quick picks? "))
    while number_of_quick_picks < 0:
        print("please enter a number greater than 0")
        number_of_quick_picks = int(input("how many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(number_of_quick_picks):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
