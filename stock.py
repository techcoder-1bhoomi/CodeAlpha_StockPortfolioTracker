stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300,
    "AMZN": 200
}

total_investment = 0

print("==== STOCK PORTFOLIO TRACKER ====")

while True:

    stock = input("\nEnter stock name (AAPL, TSLA, GOOG, MSFT, AMZN): ").upper()

    if stock not in stock_prices:
        print("Invalid stock name!")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock] * quantity

    print("Investment Value =", investment)

    total_investment += investment

    choice = input("Do you want to add another stock? (yes/no): ").lower()

    if choice == "no":
        break

print("\n==== PORTFOLIO SUMMARY ====")
print("Total Investment Value =", total_investment)

with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value = " + str(total_investment))

print("Portfolio saved successfully in portfolio.txt")
 
