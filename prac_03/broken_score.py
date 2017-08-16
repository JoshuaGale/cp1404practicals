

def main():
    valid_input = False
    while not valid_input:
        try:
            score = int(input("Enter score: "))
            valid_input = True
        except ValueError:
            print("invalid input")
    result = calculate_grade(score)
    print(result)


def calculate_grade(score):
            if score > 100 or score < 0:
                return "Invalid score"
            elif score >= 90:
                return "Excellent"
            elif score >= 50:
                return "Passable"
            else:
                return "Bad"

main()
