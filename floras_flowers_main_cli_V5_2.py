    # Flora's Flower Farm
    # Filename: floras_flowers_main.py
    # Version: 5
    # Description: Flower sale with options

import floras_flowers_class_V5_2 as flower
SALES_TAX = .07

def display_receipt():
    """Display_receipt transaction for customer"""
    subtotal = flowers.calculate()
    print("╔═══════════════════════════════════════════════╗")
    for item, price, quantity in flowers.shopping_cart:
        print(f"║{quantity}-{item} at ${price:.2f}\t\t\t${price * quantity:.2f}\t║")
    sales_tax = subtotal * SALES_TAX
    total = subtotal + sales_tax
    print(f"║\t\t\t     Sales Tax:\t${sales_tax:.2f}\t║")
    print(f"║\t\t\t      Subtotal:\t${subtotal:.2f}\t║")
    print(f"║\t\t\t\t Total:\t${total:.2f}\t║")
    print("║ Thank you for shopping at Floras Flower Farm! ║")
    print("╚═══════════════════════════════════════════════╝")

# Create FlorasFlowers object
flowers = flower.FlorasFlowers()
# Run program
flowers.get_input()
flowers.calculate()
display_receipt()