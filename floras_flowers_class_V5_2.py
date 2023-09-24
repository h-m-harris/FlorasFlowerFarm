    # Flora's Flower Farm
    # Filename: floras_flowers_class.py
    # Version: 5
    # Description: 

# Cost of flower for the customer
FLOWER_COST = 3.99
DAISY_COST = 1.00
LILY_COST = 1.50
SUNFLOWER_COST = 1.99


class FlorasFlowers:
    def __init__(self):
        # Initialize parallel lists for menu intems and prices
        self.menu_items = ["Daisy", "Lily", "Sunflower"]
        self.menu_prices = [3.99, 1.00, 1.50]
        # Initialize an empty cart
        self.cart = []

#-----------------------CLASS PROPERTIES----------------------#
    def get_menu_items(self) -> list:
        return self.menu_items
    
    def get_menu_prices(self) -> list:
        return self.menu_prices

#-----------------------DISPLAY MENU--------------------------#
    def display_menu(self) -> str:
        """Return menu items and prices as a string"""
        display = ""
        for n in range(len(self.menu_items)):
            # Increment for numbering of menu
            i = n + 1
            # Concatenate menu items for line by line display
            display += f"({i}) {self.menu_items[n]} {self.menu_prices[n]:.2f}\n"
        return display

    def get_number_flowers(self) -> int:
        # validation
        if self.number_of_flowers > 0:
            return self.number_of_flowers
        else:
            return "You must order at least one flower."

    def get_total_sale(self) -> float:
        return self._total_sale
    
    def get_input(self) -> int:
        # TODO: Get int input from user how many flowers sold
        self.number_of_daisies = int(input("Enter number of Daisies: "))
        self.number_of_lilies = int(input("Enter number of Lilies: "))
        self.number_of_sunflower = int(input("Enter number of Sunflower: "))
        self.number_of_flowers = self.number_of_daisies + self.number_of_lilies + self.number_of_sunflower


    def calculate(self) -> int:
        # TODO: Calculate cost of the flowers purchased
        self.total_daisies = self.number_of_daisies * DAISY_COST
        self.total_daisy = self.number_of_lilies * LILY_COST
        self.total_sunflower = self.number_of_sunflower * SUNFLOWER_COST
        self._total_sale = self.total_daisies + self.total_daisy + self.total_sunflower

