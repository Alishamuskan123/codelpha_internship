# TASK 2: Stock Portfolio Tracker
# A simple program to calculate total investment value

# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,    # Apple stock price
    "TSLA": 250,    # Tesla stock price
    "GOOGL": 140,   # Google stock price
    "MSFT": 330,    # Microsoft stock price
    "AMZN": 130     # Amazon stock price
}

# Display available stocks
print("=" * 40)
print("STOCK PORTFOLIO TRACKER")
print("=" * 40)
print("\nAvailable stocks and their prices:")
for stock, price in stock_prices.items():
    print(f"  {stock}: ${price}")
print("\n" + "=" * 40)

# Lists to store user's stocks and quantities
user_stocks = []
user_quantities = []

# Get stock information from user
while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()
    
    if stock_name == 'DONE':
        break
    
    # Check if stock exists in our dictionary
    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        user_stocks.append(stock_name)
        user_quantities.append(quantity)
        print(f"✓ Added {quantity} shares of {stock_name}")
    else:
        print(f"✗ {stock_name} not found! Available stocks: {', '.join(stock_prices.keys())}")

# Calculate total investment
total_investment = 0
print("\n" + "=" * 40)
print("YOUR PORTFOLIO SUMMARY")
print("=" * 40)

for i in range(len(user_stocks)):
    stock = user_stocks[i]
    quantity = user_quantities[i]
    price = stock_prices[stock]
    value = quantity * price
    total_investment += value
    print(f"{stock}: {quantity} shares × ${price} = ${value}")

print("-" * 40)
print(f"TOTAL INVESTMENT: ${total_investment}")
print("=" * 40)

#Save to file
save_option = input("\nDo you want to save this report? (yes/no): ").lower()
if save_option == 'yes':
    filename = "portfolio_report.txt"
    with open(filename, 'w') as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 40 + "\n")
        for i in range(len(user_stocks)):
            stock = user_stocks[i]
            quantity = user_quantities[i]
            price = stock_prices[stock]
            value = quantity * price
            file.write(f"{stock}: {quantity} shares × ${price} = ${value}\n")
        file.write("-" * 40 + "\n")
        file.write(f"TOTAL INVESTMENT: ${total_investment}\n")
    print(f"✓ Report saved to '{filename}'")