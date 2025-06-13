binary = input("Enter binary number: ")
try:
    decimal = int(binary, 2)
    print("Decimal:", decimal)
except:
    print("Invalid binary number")
