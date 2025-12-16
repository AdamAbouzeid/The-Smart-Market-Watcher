from .StockClient import StockClient

def read_stock_names(file_name="watchlist.txt"):
    stock_names = []
    with open(file_name, "r") as file:
        for line in file:
            stock_names.append(line.strip())

    return stock_names

def get_all_stock_prices(stock_names_list):
    stock_client = StockClient()
    stock_prices = []
    stock_previous_close = []
    for stock in stock_names_list:  
        current_price, previous_price = stock_client.fetch_price(stock)
        if current_price is not None:
            stock_prices.append(current_price)
            stock_previous_close.append(previous_price)

    return stock_prices, stock_previous_close
