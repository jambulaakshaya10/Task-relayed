import yfinance as yf
import pandas as pd

class StockPortfolio:
    def __init__(self):
        self.portfolio = pd.DataFrame(columns=["Stock", "Shares", "Purchase Price"])
        
    def add_stock(self, ticker, shares, purchase_price):
        """ Add a stock to the portfolio. """
        stock_data = {'Stock': ticker, 'Shares': shares, 'Purchase Price': purchase_price}
        self.portfolio = self.portfolio.append(stock_data, ignore_index=True)
        print(f"Added {shares} shares of {ticker} at ${purchase_price} per share.")

    def remove_stock(self, ticker):
        """ Remove a stock from the portfolio. """
        if ticker in self.portfolio['Stock'].values:
            self.portfolio = self.portfolio[self.portfolio['Stock'] != ticker]
            print(f"Removed {ticker} from portfolio.")
        else:
            print(f"{ticker} not found in portfolio.")

    def update_portfolio(self):
        """ Get current stock prices and calculate portfolio performance. """
        current_prices = []
        for index, row in self.portfolio.iterrows():
            ticker = row['Stock']
            stock = yf.Ticker(ticker)
            current_price = stock.history(period="1d")['Close'].iloc[0]  # Get the most recent close price
            current_prices.append(current_price)

        self.portfolio['Current Price'] = current_prices
        self.portfolio['Current Value'] = self.portfolio['Shares'] * self.portfolio['Current Price']
        self.portfolio['Profit/Loss'] = (self.portfolio['Current Price'] - self.portfolio['Purchase Price']) * self.portfolio['Shares']

    def show_portfolio(self):
        """ Display the portfolio and the current status. """
        if self.portfolio.empty:
            print("Your portfolio is empty.")
        else:
            self.update_portfolio()
            print(self.portfolio)

# Example Usage

# Initialize the portfolio manager
portfolio_manager = StockPortfolio()

# Add some stocks
portfolio_manager.add_stock("AAPL", 10, 145.00)  # 10 shares of Apple at $145 each
portfolio_manager.add_stock("GOOGL", 5, 2800.00)  # 5 shares of Google at $2800 each

# Show the portfolio
portfolio_manager.show_portfolio()

# Remove a stock
portfolio_manager.remove_stock("AAPL")

# Show the portfolio after removal
portfolio_manager.show_portfolio()