    # Flora's Flower Farm
    # Filename: floras_flowers_class.py
    # Version: 3
    # Description: 

# Cost of flower for the customer
FLOWER_COST = 3.99


class FlorasFlowers:
    def __init__(self):
        pass

    def get_number_flowers(self):
        # validation
        if self._number_of_flowers > 0:
            return self._number_of_flowers
        else:
            return "You must order at least one flower."

    def get_total_sale(self):
        return self._total_sale

    def calculate(self, number_of_flowers):
        # TODO: Calculate cost of the flowers purchased
        self._number_of_flowers = number_of_flowers
        self._total_sale = number_of_flowers * FLOWER_COST

