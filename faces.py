def convert(x):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    return x

def main():
    x = str(input())
    x = convert(x)
    print(x)

main()
