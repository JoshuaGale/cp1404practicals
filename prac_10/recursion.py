"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)

# print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n <= 0:
        print(n ** 2)
    else:
        print(n ** 2)
        do_something(n - 1)

# do_something(4)


def calculate_pyramid_blocks(number_of_rows):
    block_count = 0
    for row_number in range(number_of_rows):
        block_count += (number_of_rows - row_number)
    return block_count


# print(calculate_pyramid_blocks(3))


def calculate_pyramid_blocks_recursion(n):
    if n <= 0:
        return 0
    return n + calculate_pyramid_blocks_recursion(n - 1)


# print(calculate_pyramid_blocks_recursion(6))