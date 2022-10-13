octal_number = str(input("Decimal number: "))
check = 0
for character in octal_number:
    check = int(int(character) > 7)

print(int(octal_number, 8) * int(check == 0) + "Not a valid number" * int(check == 1))