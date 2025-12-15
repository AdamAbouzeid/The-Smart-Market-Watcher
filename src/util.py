import datetime
def execution_logger(func):
    def wrapper(self, symbol, *args, **kwargs):
            now = datetime.datetime.now().strftime("%X")
            print(f"[{now}] Fetching data for: {symbol}...")
            return func(self, symbol, *args, **kwargs)
    return wrapper
