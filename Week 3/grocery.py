def main():
    get_item()

def get_item():
    items = {}
    while True:
        try:
            item = str(input()).upper()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
        except EOFError:
            break
    for item in sorted(items):
        print(items[item], item)
main()
