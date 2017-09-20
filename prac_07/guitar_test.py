from prac_07.guitar import Guitar

guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar_2 = Guitar("Another Guitar", 2012, 500)

print(guitar_1)
print("Expected 95. got {}".format(guitar_1.get_age()))
print("Expected True got {}".format(guitar_1.is_vintage()))

print(guitar_2)
print("Expected 5 got {}".format(guitar_2.get_age()))
print("Expected False got {}".format(guitar_2.is_vintage()))
