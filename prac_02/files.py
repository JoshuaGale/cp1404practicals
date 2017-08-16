user_name = input("what is your name?: ")
out_file = open("name.txt", 'w')
out_file.write(user_name)
out_file.close()

in_file = open("name.txt", 'r')
user_name = in_file.read()
print("your name is {}".format(user_name))

in_file = open("numbers.txt", 'r')
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
print(number_1 + number_2)
in_file.close()

in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()
