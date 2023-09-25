    # Flora's Flower Farm
    # Filename: floras_flowers_class.py
    # Version: 5
    # Description: 

class FlorasFlowers:
    def __init__(self):
        # Initialize parallel lists for menu intems and prices
        self.menu_items = ["Daisy", "Lily", "Rose", "Sunflower", "Tulip"]
        self.menu_prices = [3.99, 1.99, 1.49, 2.99, 1.49]
        # Initialize an empty shopping cart
        self.shopping_cart = []

#-----------------------DISPLAY FLOWER MENU--------------------------#
    def display_menu(self) -> str:
        """Return menu items and prices"""
        # Option A
        """display = ""
        for n in range(len(self.menu_items)):
            # Increment for numbering of menu
            i = n + 1
            # Concatenate menu items for line by line display
            display += f"{i}. {self.menu_items[n]} ${self.menu_prices[n]:.2f}\n"
        return display"""

        # Option B Import rich to make it fancy
        from rich.table import Table
        from rich.console import Console
        from rich import box
        console = Console()
        table = Table(title="Flora's Flower Farm", title_justify="center",box=box.DOUBLE_EDGE)
        table.add_column("Number", justify="left", no_wrap=True)
        table.add_column("Flower", justify="left", no_wrap=True)
        table.add_column("Cost", justify="left", style="green", no_wrap=True)
        for x in range(len(self.menu_items)):
            # Increment for numbering of menu
            i = x + 1
            table.add_row(str(i), str(self.menu_items[x]), str(self.menu_prices[x]))
        console.print(table)

#----------------------ADD ITEMS TO SHOPPING CART-------------------#
    def add_shopping_cart(self, user_choice: int, quantity: int) -> str:
        """ Add the item, price, quantity to the shopping cart"""
        if 0 <= int(user_choice)-1 <= len(self.menu_items):
            item = self.menu_items[int(user_choice)-1]
            price = self.menu_prices[int(user_choice)-1]
            self.shopping_cart.append((item, price, quantity))
        # Prevent negative amount entry
        else:
            print("Please select a flower to purchase.")

#---------------------------GET USER INPUT--------------------------#
    def get_input(self) -> str:
        """Get input from user on flower and quantity"""
        while True:
            FlorasFlowers.display_menu(self)
            # Get number of items available
            options = len(self.menu_items)
            user_choice = input("Enter an item to order or press (e) to exit: ").lower()
            # press e to exit program
            if user_choice == 'e':
                break
            # Prevent entering a menu option that isn't available
            elif user_choice > str(options):
                print("Please select a flower to purchase.")
                continue
            quantity = int(input("Enter the quantity: "))
            # Prevent negative quantity
            if quantity <= 0:
                print("Please enter a quantity.")
                continue
            FlorasFlowers.add_shopping_cart(self,user_choice, quantity)

#-------------------------CALCULATE THE TOTAL----------------------#
    def calculate(self) -> int:
        """Calculate cost of the flowers purchased"""
        total = sum(price * quantity for x, price, quantity in self.shopping_cart)
        return total