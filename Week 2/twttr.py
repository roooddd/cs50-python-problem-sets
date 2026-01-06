def main():
    text = str(input("Input: "))
    print(f"Output: {remove_vowels(text)}")

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

main()
