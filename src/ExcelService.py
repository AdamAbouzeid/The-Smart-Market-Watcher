import pandas as pd
from openpyxl.styles import Font

def create_data_frame(stock_names, stock_prices, stock_previous_close):
    stock_data = pd.DataFrame({
        "names": stock_names,
        "prices": stock_prices,
        "previous_close": stock_previous_close
    })

    stock_data["change %"] = (
        (stock_data.prices - stock_data.previous_close)
        / stock_data.previous_close * 100
    )

    return stock_data

def color_cell(sh):

    positive_font = Font(color="00FF00")
    negative_font = Font(color="FF0000")

    change_col = 4

    for row in range(2, sh.max_row + 1):
        cell = sh.cell(row=row, column=change_col)
        value = cell.value

        if value is None:
            continue

        if value > 0:
            cell.font = positive_font
        elif value < 0:
            cell.font = negative_font
