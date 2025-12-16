import requests
from ..util import execution_logger

class StockClient:
    def __init__(self, url="https://query1.finance.yahoo.com/v8/finance/chart/"):
        self.url = url

    @execution_logger 
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
            return None, None
        except requests.exceptions.ConnectionError:
            print("Failed to connect to the server.")
            return None, None
        except requests.exceptions.Timeout:
            print("The request timed out.")
            return None, None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None, None

        price = data['chart']['result'][0]['meta']['regularMarketPrice']
        previous_close = data['chart']['result'][0]['meta']['chartPreviousClose']

        return price, previous_close
