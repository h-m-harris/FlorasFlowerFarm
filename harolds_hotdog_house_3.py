    # Flora's Flower Farm
    # Filename: harold_flower_house_3.py
    # Version: 3
    # Description: OOP POS Program

# Cost of flower for the customer
FLOWER_COST = 3.99


class FlorasFlowers:
    def __init__(self):
        self.get_input()
        self.calculate()
        self.display()

    def get_input(self):
        # TODO: Get int input from user how many flowers sold
        self.number_of_flowers = int(input("Enter number of flowers: "))

    def calculate(self):
        # TODO: Calculate cost of the flowers purchased
        self.total_sale = self.number_of_flowers * FLOWER_COST

    def display(self):
        # TODO: Display transaction for customer
        print(f"Your total was: ${self.total_sale:,.2f}")


floras_flowers = FlorasFlowers()