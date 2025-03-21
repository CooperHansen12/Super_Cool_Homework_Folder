import numpy as np  # Import Numpy

# Open stock price file
with open("/home/ubuntu/Super_Cool_Homework_Folder/HW4/TSLA.txt") as file:
    lines = file.readlines()

lines = lines[::-1]  # Reverse to correct order

prices = np.zeros(len(lines))

for i in range(len(lines)):
    prices[i] = round(float(lines[i]), 2)  # Round prices to 2 decimal places

def rollingaverage(prices):
    buy = None  # Current buy price
    first_buy_price = None  # First buy price to calculate percentage profit
    total_profit = 0  # Running total of profit
    rolling_averages = []  # Store 5-day moving averages

    for i in range(len(prices)):
        current_price = prices[i]

        if i >= 4:
            avg_5_day = round(sum(prices[i-4:i+1]) / 5, 2)  # Round 5-day moving average
            rolling_averages.append(avg_5_day)

            # Buy condition
            if current_price < round(avg_5_day * 0.98, 2):
                buy = current_price
                if first_buy_price is None:
                    first_buy_price = buy  # Store the first buy price
                print(f"Buy at ${buy:.2f} on day {i+1}")

            # Sell condition
            elif buy is not None and current_price > round(avg_5_day * 1.02, 2):
                profit = round(current_price - buy, 2)
                total_profit += profit
                print(f"Sell at ${current_price:.2f} on day {i+1} | Profit: ${profit:.2f}")
                buy = None  # Reset buy after selling
            
            # Hold condition
            else:
                print(f"Hold on day {i+1} (Price: ${current_price:.2f}, 5-day MA: ${avg_5_day:.2f})")

    # Calculate and print final profit percentage
    if first_buy_price is not None:
        final_profit_percentage = round((total_profit / first_buy_price) * 100, 2)
        print(f"\nFirst Buy Price: ${first_buy_price:.2f}")
        print(f"Total Profit from Trades: ${total_profit:.2f}")
        print(f"Final Profit Percentage: {final_profit_percentage:.2f}%")
    else:
        print("\nNo trades were made.")

rollingaverage(prices)
