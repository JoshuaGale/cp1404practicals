def main():
    numbers = []
    for number in range(5):
        input_number = int(input("Number:"))
        numbers.append(input_number)

    print("the first number is {} ".format(numbers[0]))
    print("the last number is {} ".format(numbers[-1]))
    print("the smallest number is {} ".format(min(numbers)))
    print("the largest number is {} ".format(max(numbers)))
    print("the average number is {} ".format(sum(numbers) / len(numbers)))

main()
