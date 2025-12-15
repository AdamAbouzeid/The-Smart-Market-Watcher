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
    for stock in stock_names_list:  
        stock_prices.append(stock_client.fetch_price(stock))

    return stock_prices

def main():
    stock_names = read_stock_names()
    stock_data = get_all_stock_prices(stock_names)
    print(stock_data)


if __name__ == "__main__":
    main()
