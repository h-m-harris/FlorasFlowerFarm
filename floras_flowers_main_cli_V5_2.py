    # Flora's Flower Farm
    # Filename: floras_flowers_main.py
    # Version: 5
    # Description: Flower sale with options

import floras_flowers_class_V5_2 as flower
SALES_TAX = .07

def display_receipt():
    """Display_receipt transaction for customer"""
    subtotal = flowers.calculate()
    print("╔══════════════════════════════════════════════╗")
    for item, price, quantity in flowers.shopping_cart:
        print(f"║{quantity}-{item} at ${price:.2f} = ${price * quantity:.2f}║")
    sales_tax = subtotal * SALES_TAX
    total = subtotal + sales_tax
    print(f"║Sales Tax: {sales_tax:.2f}║")
    print(f"║Subtotal: ${subtotal:.2f}║")
    print(f"║Total: ${total:.2f}║")
    print("║Thank you for shopping at Floras Flower Farm! ║")
    print("╚══════════════════════════════════════════════╝")

# Create FlorasFlowers object
flowers = flower.FlorasFlowers()
# Run program
flowers.get_input()
flowers.calculate()
display_receipt()