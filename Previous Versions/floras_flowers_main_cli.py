    # Flora's Flower Farm
    # Filename: floras_flowers_main.py
    # Version: 3
    # Description: flower shop

import floras_flowers_class as flower

def get_input():
    # TODO: Get int input from user how many flowers sold
    number_of_flowers = int(input("Enter number of flowers: "))
    return number_of_flowers


def display():
    # TODO: Display transaction for customer
    number_of_flowers = floras_flowers.get_number_flowers()
    total_sale = floras_flowers.get_total_sale()
    
    print(f"Number of flowers: {number_of_flowers}")
    print(f"Your total was: ${total_sale:,.2f}")


number_of_flowers = get_input()

floras_flowers = flower.FlorasFlowers()

floras_flowers.calculate(number_of_flowers)

display()