    # Flora's Flower Farm
    # Filename: floras_flowers_1.py
    # Version: 1
    # Description: POS Program

# Cost of flower for the customer
FLOWER_COST = 2.99

# TODO: Get int input from user how many flowers sold
number_of_flowers = int(input("Enter number of flowers: "))

# TODO: Calculate cost of the flowers purchased
total_receipt = number_of_flowers * FLOWER_COST

# TODO: Display transaction for customer
print(f"Your total was: ${total_receipt:,.2f}")
