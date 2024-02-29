import requests

def get_stock_price(ticker_symbol, api_key):
    url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = float(data.get('price', 0))
        return price
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the stock price: {e}")
        return None
    except (ValueError, KeyError) as e:
        print(f"Error parsing stock price data: {e}")
        return None

def get_stock_quote(ticker_symbol, api_key):
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching stock quote: {e}")
        return None
    except (ValueError, KeyError) as e:
        print(f"Error parsing stock quote data: {e}")
        return None

def main():
    # Ask the user to enter details
    ticker = input("Enter the stock ticker symbol: ")
    api_key = input("Enter the API key: ")

    stock_data = get_stock_quote(ticker, api_key)

    if stock_data:
        stock_price = get_stock_price(ticker, api_key)
        exchange = stock_data.get('exchange', '')
        currency = stock_data.get('currency', '')
        open_price = stock_data.get('open', '')
        high_price = stock_data.get('high', '')
        low_price = stock_data.get('low', '')
        close_price = stock_data.get('close', '')
        volume = stock_data.get('volume', '')
        name = stock_data.get('name', '')

        print(f"Stock: {name}, Price: {stock_price}")
        print(f"Exchange: {exchange}, Currency: {currency}")
        print(f"Open: {open_price}, High: {high_price}, Low: {low_price}, Close: {close_price}")
        print(f"Volume: {volume}")
    else:
        print("Unable to fetch stock data.")

if __name__ == '__main__':
    main()
