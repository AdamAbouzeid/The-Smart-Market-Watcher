# Estarta Stock Smart Watcher

A Python application that fetches real-time stock prices and generates color-coded Excel reports for market analysis.

## Features

-  Real-time stock price fetching from Yahoo Finance API
-  Automatic Excel report generation with timestamp
-  Color-coded cells to visualize price changes (green for gains, red for losses)
-  Support for multiple stock symbols via watchlist
-  Error handling and connection management

## Project Structure

```
The-Smart-Market-Watcher/
├── src/
│   ├── Stock/
│   │   ├──  StockClient.py       # Yahoo Finance API client
│   │   └──  StockService.py      # Stock data processing logic
│   ├──  ExcelService.py          # Excel report generation
│   ├──  util.py                  # Utility functions and decorators
├──  watchlist.txt                # Stock symbols to monitor
├──  main.py                      # Application entry point
├──  requirements.txt             # Python dependencies
├──  .gitignore                   # Git ignore rules
└──  README.md                    # This file
```

## Task Description

The application fetches real-time prices and previous close values for selected stocks (Apple, Microsoft, Tesla, Nvidia) and generates comprehensive Excel reports with visual indicators for price movements.

## Technology Stack

| Library | Version | Purpose |
|---------|---------|---------|
|  **pandas** | 2.3.3 | Data manipulation and analysis |
|  **openpyxl** | 3.1.5 | Excel file creation and formatting |
|  **requests** | 2.32.5 | HTTP client for API calls |
|  **datetime** | Built-in | Timestamp generation |

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Internet connection for stock price fetching

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd The-Smart-Market-Watcher
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the application with a single command:

```bash
python src/main.py
```

Or if you're in the `src` directory:

```bash
python main.py
```

## 📊 Output

The application generates an Excel file with the following naming convention:
```
stock_watch-YYYY-MM-DD_HH-MM-SS.xlsx
```

**Report Features:**
- Stock symbols and current prices
- Previous close prices for comparison
- Automatic color coding:
  - **Green** cells for price increases
  - **Red** cells for price decreases
- ⏰ Timestamp in filename for version tracking

## ⚙️ Configuration

Edit the `watchlist.txt` file to monitor different stocks:

```
AAPL
MSFT
TSLA
NVDA
GOOGL
AMZN
```

