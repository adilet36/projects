def main():
    print_square(4)

def print_square(size):
    # for each row in square
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()