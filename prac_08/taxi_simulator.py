from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
bill_to_date = 0

print("Let's Drive!")
menu_choice = (input("q)uit, c)hoose taxi, d)rive\n>>> ")).lower()
while menu_choice != "q":
    if menu_choice == "c":
        print("Taxis available:")
        print("0 - {}\n1 - {}\n2 - {}".format(taxis[0], taxis[1], taxis[2]))
        taxi_choice = int(input("Choose taxi: "))
        print("Bill to date: ${:.2f}".format(bill_to_date))

    elif menu_choice == "d":
        taxis[taxi_choice].start_fare()
        drive_distance = int(input("Drive how far? "))
        taxis[taxi_choice].drive(drive_distance)
        print("your {} trip cost you ${:.2f}".format(taxis[taxi_choice].name, taxis[taxi_choice].get_fare()))
        bill_to_date += taxis[taxi_choice].get_fare()
        print("Bill to date: ${:.2f}".format(bill_to_date))

    else:
        print("invalid menu choice")

    menu_choice = (input("q)uit, c)hoose taxi, d)rive\n>>>")).lower()

print("Total trip cost: ${:.2f}".format(bill_to_date))
print("Taxis are now:")
print("0 - {}\n1 - {}\n2 - {}".format(taxis[0], taxis[1], taxis[2]))