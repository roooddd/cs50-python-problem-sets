def main():
    get_item()

def get_item():
    total_price = 0
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    while True:
        try:
            item = str(input("Item: ")).title()
            if item in menu:
                total_price += menu[item]
                print(f"Total: ${total_price:.2f}")
        except EOFError:
            break

main()
