"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if 1000 > sales:
        bonus = 0.1 * sales
    else:
        bonus = 0.15 * sales
    print("your bonus is: {}".format(bonus))
    sales = float(input("Enter sales: $"))
print("now exiting sales calculator")

# sales = float(input("Enter sales: $"))
# while sales >= 0:
#     try:
#         sales = float(input("Enter sales: $"))
#         if 1000 > sales >= 0:
#             bonus = 0.1 * sales
#             print("your bonus is: {}".format(bonus))
#         elif sales >= 1000:
#             bonus = 0.15 * sales
#             print("your bonus is: {}".format(bonus))
#     except ValueError:
#         print("invalid sales value")
# print("now exiting sales calculator")
