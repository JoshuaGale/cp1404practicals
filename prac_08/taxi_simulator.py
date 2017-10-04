from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0

    print("Let's Drive!")
    print(MENU)
    menu_choice = (input(">>> ")).lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            display_taxi(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]

        elif menu_choice == "d":
            current_taxi.start_fare()
            drive_distance = int(input("Drive how far? "))
            current_taxi.drive(drive_distance)
            print("your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
            bill_to_date += current_taxi.get_fare()

        else:
            print("invalid menu choice")
        print("Bill to date: ${:.2f}".format(bill_to_date))
        print(MENU)
        menu_choice = (input(">>> ")).lower()

    print("Total trip cost: ${:.2f}".format(bill_to_date))
    print("Taxis are now:")
    display_taxi(taxis)


def display_taxi(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, str(taxi)))

main()