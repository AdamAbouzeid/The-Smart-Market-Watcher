import datetime
from src.Stock.StockService import read_stock_names, get_all_stock_prices
from openpyxl import load_workbook
from src.ExcelService import create_data_frame, color_cell



def main():
    stock_names = read_stock_names()
    stock_prices, stock_previous_close = get_all_stock_prices(stock_names)

    print("Creating data frame...")
    stock_data = create_data_frame(stock_names, stock_prices, stock_previous_close)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    excel_file_name = f"stock_watch-{timestamp}.xlsx"

    print("Saving data to Excel...")
    stock_data.to_excel(excel_file_name, index=False)


    wb = load_workbook(excel_file_name)
    sh = wb.active

    print("Coloring cells...")
    color_cell(sh)

    wb.save(excel_file_name)



if __name__ == "__main__":
    main()
