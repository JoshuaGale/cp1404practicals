from prac_07.guitar import Guitar


def run_tests():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    guitar_1 = Guitar(name, year, cost)
    guitar_2 = Guitar("Another Guitar", 2012, 500)

    print(guitar_1)
    print("{} get_age() - Expected {}. got {}".format(guitar_1.name, 95, guitar_1.get_age()))
    print("{} is_vintage() - Expected {} got {}".format(guitar_1.name, True, guitar_1.is_vintage()))

    print()
    print(guitar_2)
    print("{} get_age() - Expected {}. got {}".format(guitar_2.name, 5, guitar_2.get_age()))
    print("{} is_vintage() - Expected {} got {}".format(guitar_2.name, False, guitar_2.is_vintage()))


if __name__ == '__main__':
    run_tests()
