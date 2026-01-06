def main():
    camel = input("camelCase: ")
    print("snake_case:", to_snake(camel))

def to_snake(s):
    result = ""
    for ch in s:
        if "A" <= ch <= "Z":
            result += "_" + ch.lower()
        else:
            result += ch
    return result

main()
