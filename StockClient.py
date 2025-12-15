import requests
import util

class StockClient:
    def __init__(self, url="https://query1.finance.yahoo.com/v8/finance/chart/"):
        self.url = url

    @util.execution_logger 
    def fetch_price(self, symbol):
        required_headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        try:
            response = requests.get(
                url=f"{self.url}{symbol}?interval=1d&range=1d",
                headers=required_headers
            )
            data = response.json()
        except (KeyError, IndexError, TypeError):
            print("Could not fetch price for the given symbol.")
            return None
        except requests.exceptions.ConnectionError:
            print("Failed to connect to the server.")
            return None

        price = data['chart']['result'][0]['meta']['regularMarketPrice']
        return price