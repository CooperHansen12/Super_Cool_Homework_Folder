# Import JSON
import json

# Create function for Mean Reversion Strategy
def meanreversionstrategy(prices,name):
    print(name, "Mean Reversion Strategy Output")
    i = 0 #initialize each variable
    buy = 0
    first_buy = 0
    total_profit = 0
    total_trades = 0
    MR_firstbuy = None

    for price in prices:
        if i >= 5:
            current_price = price
            average = sum(prices[i-5:i])/5
            # When to Buy
            if current_price < average * 0.98 and buy == 0:
                buy = current_price
                print("Buying at: ",price)
                if MR_firstbuy is None:
                    MR_firstbuy = price
            # When to sell
            elif current_price > average * 1.02 and buy != 0:
                print("Selling at: ", current_price)
                trade_profit = current_price - buy
                total_profit += trade_profit
                total_trades += 1
                print("Trade profit: ", current_price - buy)
                buy = 0
            else:
                pass
        i += 1
    return total_profit, round((total_profit/total_trades)*100,2) if total_trades else 0, MR_firstbuy
# Create function for Simple Moving Average Strategy
def simplemovingavg(prices, name):
    print(name, "Simple Moving Average Strategy Output")
    i = 0 #initialize the variables
    buy = 0
    total_profit = 0
    total_trades = 0
    SMA_firstbuy = None

    for price in prices:
        if i >= 5:
            average = sum(prices[i-5:i]) / 5
            # When to Buy
            if price > average and buy == 0:
                buy = price
                print("Buying at:", price)
                if SMA_firstbuy is None:
                    SMA_firstbuy = price
            # When to sell
            elif price < average and buy != 0:
                print("Selling at:", price)
                trade_profit = price - buy
                total_profit += trade_profit
                total_trades += 1
                print("Trade profit: ", price - buy)
                buy = 0
        i += 1

    return total_profit, round((total_profit / total_trades)*100,2) if total_trades else 0, SMA_firstbuy

# Create function to save results in JSON
def saveresults(results):
    with open("/home/ubuntu/Super_Cool_Homework_Folder/HW5/results.json", "w") as f: json.dump(results, f, indent=2)

# Create tickers to reference each txt file
tickers = ["AAPL","GOOGL","NKE","NVDA","HD","TSLA","BAC","CSCO","GME","JPM"]
# initialize results dictionary
results = {}

for ticker in tickers:
    try:
        with open(f"/home/ubuntu/Super_Cool_Homework_Folder/HW5/{ticker}.txt") as f: prices = [round(float(line.strip()), 2) for line in reversed(f.readlines())]

        MR_profit, MR_returns, MR_firstbuy = meanreversionstrategy(prices,ticker)
# print each statistic at after the buying and selling
        print("\nTotal Profit:",MR_profit)
        print("First Buy:",MR_firstbuy)
        print("Percent Return:",MR_returns,"%","\n")

        SMA_profit, SMA_returns, SMA_firstbuy = simplemovingavg(prices, ticker)
        print("\nTotal Profit:",SMA_profit)
        print("First Buy:",SMA_firstbuy)
        print("Percent Return:",SMA_returns,"%","\n")

# assign results in JSON file
        results[ticker+"_prices"] = prices
        results[ticker+"_MR_profit"] = MR_profit
        results[ticker+"_MR_returns"] = MR_returns
        results[ticker+"_SMA_profit"] = SMA_profit
        results[ticker+"_SMA_returns"] = SMA_returns
# exceptions for errors
    except FileNotFoundError:
        print(f"Error! File {ticker} not found.")
        continue
    except Exception as e:
        print(f"Unexpected error for {ticker}: {e}")
        continue
# Upload results to JSON
saveresults(results)