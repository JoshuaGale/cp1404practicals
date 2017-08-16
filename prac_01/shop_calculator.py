invalid_number_of_items = True
invalid_item_prices = True

while invalid_number_of_items:
    try:
        number_of_items = int(input("Number of items: "))

        if number_of_items < 0:

            print("invalid Number of items")

        else:

            invalid_number_of_items = False

    except ValueError:

        print("invalid Number of items")

while invalid_item_prices:

    total_price = 0

    for i in range(number_of_items):

        try:

            item_price = input("Price of item {}: ".format(i + 1))

            total_price += int(item_price)

            invalid_item_prices = False

        except ValueError:

            print("invalid Item Price, please re-enter item prices")

            invalid_item_prices = True

            break

if total_price >= 100:
    total_price -= total_price * 0.1

print("total price for {} items is ${:.2f}".format(number_of_items, total_price))
