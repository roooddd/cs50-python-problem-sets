def main():
    insert()

def insert():
    coin_options = [5, 10, 25]
    price = 50
    print(f"Amount Due: {price}")
    while True:
        coins = int(input("Insert Coin: "))
        print(f"Amount Due: {price}")

        if coins in coin_options:
            price -= coins
            if coins > price:
                print(f"Change Owed: {abs(price)}")
                break
            print(f"Amount Due: {price}")
        else:
            continue

main()
