print("Please enter the prices with a space between them! ")
prices = list(map(int, input("prices = ").split()))
prices_with_tax = list(map(lambda x: x + x * 0.09, prices))
print(prices_with_tax)

price_taxed = list(map(lambda x: int(x) + int(x) * .09, input("Enter prices:  ").split()))
print(price_taxed)

side1, side2, side3 = map(lambda x: float(x) ** 2, (input("enter 3 sides").split()))
print(side1, side2, side3)


