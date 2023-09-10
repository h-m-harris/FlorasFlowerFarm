    # Flora's Flower Farm
    # Filename: floras_flowers_class.py
    # Version: 3
    # Description: 

# Cost of flower for the customer
FLOWER_COST = 3.99

class FlorasFlowers:
    def __init__(self):
        pass


    def calculate(self, number_of_flowers):
        # TODO: Calculate cost of the flowers purchased
        self.number_of_flowers = number_of_flowers
        self.total_sale = number_of_flowers * FLOWER_COST

