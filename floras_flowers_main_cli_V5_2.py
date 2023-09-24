    # Flora's Flower Farm
    # Filename: floras_flowers_main.py
    # Version: 5
    # Description: Flower sale with options

import floras_flowers_class_V5_2 as flower

def display_receipt():
    # TODO: Display_receipt transaction for customer
    number_of_flowers = floras_flowers.get_number_flowers()
    total_sale = floras_flowers.get_total_sale()
    
    print(f"Number of flowers: {number_of_flowers}")
    print(f"Your total was: ${total_sale:,.2f}")



floras_flowers = flower.FlorasFlowers()
floras_flowers.display_menu()
#floras_flowers.get_input()
#floras_flowers.calculate()

#display_receipt()