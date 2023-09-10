    # Flora's Flower Farm
    # Filename: floras_flowers_2.py
    # Version: 2
    # Description: Functional POS Program

# Cost of flower for the customer
FLOWER_COST = 2.99


def main():
    num_of_flowers = get_input()
    total_sale = calculate(num_of_flowers)
    display(total_sale)


def get_input():
    # TODO: Get int input from user how many flowers sold
    number_of_flowers = int(input("Enter number of flowers: "))
    return number_of_flowers


def calculate(number_of_flowers):
    # TODO: Calculate cost of the flowers purchased
    total_sale = number_of_flowers * FLOWER_COST
    return total_sale


def display(total_sale):
    # TODO: Display transaction for customer
    print(f"Your total was: ${total_sale:,.2f}")

if __name__ == '__main__':
    main()