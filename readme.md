# Estarta Stock Smart Watcher Task
## Task Description
- Fetch the real-time price and previous close of the stocks for Apple, Microsoft, Tesla and Nvidia, and then creates an Excel report listing those numbers.
- The numbers are colour-coded to differentiate between percentage increases and decreases.

## Libraries Used
- opepyxl
- pandas
- requests
- datetime

## Instructions to Run the Code
1. Ensure you have Python installed on your machine.
2. Install the required libraries using pip:
```pip install openpyxl pandas requests```

    Or you can use the provided **requirements.txt** file:
    ``` bash
    pip install -r requirements.txt
    ```
3. Just do 
    ```python main.py```
    to run the code.

## Output
- An Excel file named `stock_report-{timestamp}.xlsx` will be generated in the same directory as the script.
- The Excel file will contain the stock prices and percentage changes, with appropriate color coding for increases and decreases.
