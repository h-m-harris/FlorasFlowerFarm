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
        pass

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

    def display_flower_options(self):

        from rich.table import Table
        from rich.console import Console
        from rich import box
        console = Console()
        
        table = Table(title="Flora's Flower Farm", title_justify="center",box=box.DOUBLE_EDGE)
        table.add_column("Flower", justify="left", no_wrap=True)
        table.add_column("Cost", justify="left", style="green", no_wrap=True)
        
        table.add_row("Daisy", "$1.00")
        table.add_row("Lily", "$1.50")
        table.add_row("Sunflower", "$1.99")
        console.print(table)