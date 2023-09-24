    # Flora's Flower Farm
    # Filename: floras_flowers_main.py
    # Version: 5
    # Description: Flower sale with options

import floras_flowers_class_V5_2 as flower


def display_receipt():
    """Display_receipt transaction for customer"""
    total = flowers.calculate()
    print()
    for item, price, quantity in flowers.shopping_cart:
        print(f"{quantity} {item} @ ${price:.2f} = ${price * quantity:.2f}")
    print(f"Total: ${total:.2f}")
    print("Thank you for shopping at Floras Flower Farm!")

# Create FlorasFlowers object
flowers = flower.FlorasFlowers()
flowers.get_input()
flowers.calculate()
display_receipt()