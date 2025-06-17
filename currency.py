from currency_converter import CurrencyConverter

def currency_converter():
    c = CurrencyConverter()
    print("Welcome to Currency Converter (Offline Support)")

    try:
        amount = float(input("Enter amount to convert: "))
        from_currency = input("From currency (e.g., USD, INR, EUR): ").upper()
        to_currency = input("To currency (e.g., USD, INR, EUR): ").upper()

        result = c.convert(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

    except Exception as e:
        print("Error:", str(e))

currency_converter()
