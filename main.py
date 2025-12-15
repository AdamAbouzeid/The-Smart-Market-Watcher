import StockClient

def read_stock_names(file_name="watchlist.txt"):
    stock_names = []
    with open(file_name, "r") as file:
        for line in file:
            stock_names.append(line.strip())
            
    return stock_names

def get_all_stock_prices(stock_names_list):
    stock_client = StockClient.StockClient()
    stock_prices = []
    stock_previous_close = []
    for stock in stock_names_list:  
        stock_data = stock_client.fetch_price(stock)
        stock_prices.append(stock_data[0])
        stock_previous_close.append(stock_data[1])

    return stock_prices, stock_previous_close

def main():
    stock_names = read_stock_names()
    stock_prices, stock_previous_close = get_all_stock_prices(stock_names)
    print(stock_prices, stock_previous_close)


if __name__ == "__main__":
    main()
