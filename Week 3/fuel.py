def main():
    while True:
        try:
            get_fuel()
            break
        except (ValueError, ZeroDivisionError):
            pass

def get_fuel():
    fraction = input("Fraction: ")
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    percentage = round(x / y * 100)
    if x > y or y <= 0 or x < 0:
        raise ValueError
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

main()
