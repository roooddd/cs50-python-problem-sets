# plates.py

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"

    if not (2 <= len(s) <= 6):
        return False

    if s[0] not in letters or s[1] not in letters:
        return False

    for ch in s:
        if ch not in letters and ch not in digits:
            return False

    for i in range(len(s)):
        if s[i] in digits:

            if s[i] == "0":
                return False

            for j in range(i, len(s)):
                if s[j] not in digits:
                    return False
            break

    return True

main()
