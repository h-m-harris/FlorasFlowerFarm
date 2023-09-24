    # Flora's Flower Farm
    # Filename: floras_flowers_class.py
    # Version: 5.1
    # Description: 

# Cost of flower for the customer
FLOWER_COST = 3.99
DAISY_COST = 1.00
LILY_COST = 1.50
SUNFLOWER_COST = 1.99


class FlorasFlowers:
    def __init__(self) -> list:
        self.menu_items = ["Daisy", "Lily", "Sun Flower"]
        self.menu_prices = [3.99, 1.00, 1.50]
        # Initialize an empty cart
        self.cart = []

    def get_menu_items(self):
        return self.menu_items
    
    def get_menu_prices(self):
        return self.menu_prices

    def display_flower_options(self):
        """display menu items and prices"""
        # Import rich to make it fancy
        from rich.table import Table
        from rich.console import Console
        from rich import box
        console = Console()
        table = Table(title="Flora's Flower Farm", title_justify="center",box=box.DOUBLE_EDGE)
        table.add_column("Flower", justify="left", no_wrap=True)
        table.add_column("Cost", justify="left", style="green", no_wrap=True)
        for x in range(3):
            table.add_row(self.menu_items[x], str(self.menu_prices[x]))
        console.print(table)

        """ Not so fancy option"""
        #for x in range(3):
        #    print(f"{self.menu_items[x]} {self.menu_prices[x]}")


    def get_number_flowers(self):
        # validation
        if self.number_of_flowers > 0:
            return self.number_of_flowers
        else:
            return "You must order at least one flower."

    def get_total_sale(self):
        return self._total_sale
    
    def get_input(self):
        # TODO: Get int input from user how many flowers sold
        self.number_of_daisies = int(input("Enter number of Daisies: "))
        self.number_of_lilies = int(input("Enter number of Lilies: "))
        self.number_of_sunflower = int(input("Enter number of Sunflower: "))
        self.number_of_flowers = self.number_of_daisies + self.number_of_lilies + self.number_of_sunflower


    def calculate(self):
        # TODO: Calculate cost of the flowers purchased
        self.total_daisies = self.number_of_daisies * DAISY_COST
        self.total_daisy = self.number_of_lilies * LILY_COST
        self.total_sunflower = self.number_of_sunflower * SUNFLOWER_COST
        self._total_sale = self.total_daisies + self.total_daisy + self.total_sunflower
"""
# Use for testing of the program
floras_flowers = FlorasFlowers()
floras_flowers.display_flower_options()
floras_flowers.get_input()
floras_flowers.calculate()"""