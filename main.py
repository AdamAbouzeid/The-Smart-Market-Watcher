import StockClient
import datetime
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill


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
        if stock_data is not None:
            stock_prices.append(stock_data[0])
            stock_previous_close.append(stock_data[1])

    return stock_prices, stock_previous_close
def main():
    stock_names = read_stock_names()
    stock_prices, stock_previous_close = get_all_stock_prices(stock_names)

    stock_data = pd.DataFrame({
        "names": stock_names,
        "prices": stock_prices,
        "previous_close": stock_previous_close
    })

    stock_data["change %"] = (
        (stock_data.prices - stock_data.previous_close)
        / stock_data.previous_close * 100
    )

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    excel_file_name = f"stock_watch-{timestamp}.xlsx"
    stock_data.to_excel(excel_file_name, index=False)


    wb = load_workbook(excel_file_name)
    sh = wb.active

    positive_fill = PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid")
    negative_fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")

    for i in range(2, sh.max_column + 1):
        if int(sh.cell(row=i, column=4).value) > 0:
            sh.cell(row=i, column=4).fill = positive_fill
        elif int(sh.cell(row=i, column=4).value) < 0:
            sh.cell(row=i, column=4).fill = negative_fill

if __name__ == "__main__":
    main()
