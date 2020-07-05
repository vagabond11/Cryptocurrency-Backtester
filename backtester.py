import matplotlib.pyplot as plt 
import requests, json 

"""
     we need inputs to the ticker ( to fetch the historical data ), initial investement and the strategy the user wants to test 
    
    """
def start():
   
    print( "Starting Crypto Backtester V1" )
    ticker = input("Enter ticker: ").upper()
    data_url = 'https://min-api.cryptocompare.com/data/histominute?fsym=' + ticker + '&tsym=USD&limit=2000&aggregate=1'
    response = requests.get(data_url)
    try:
        data = response.json()['Data']
    except:
        print( "Sorry, this crypto isn't supported!" )
        quit()
    historical_data = data
    print( "Fetched historical data for crypto: " + ticker )
    cash = input("Enter initial investment: ")
    strategy = input("Select (1) for the moving averages strategy: ")
    if strategy == "1":
        moving_averages(historical_data, ticker, cash)

