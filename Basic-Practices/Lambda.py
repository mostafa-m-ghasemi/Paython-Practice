
calculate_tax = lambda price: price * 1.09
while True:
    try:
        price = float(input("Enter the prduce price:  "))
        print(f"Final price including 9% tax is {calculate_tax(price):.2f}")
    except ValueError:
        print("The price is invalid")
