invalid_input = True
while invalid_input:
    try:
        score = int(input("Enter score: "))
        if score > 100 or score < 0:
            print("Invalid score")
        elif score >= 90:
            print("Excellent")
        elif score >= 50:
            print("Passable")
        else:
            print("Bad")
        invalid_input = False
    except ValueError:
        print("invalid input")
