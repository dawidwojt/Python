import yfinance as yf
import pandas as pd
from datetime import datetime
import time
#from kafka import KafkaProducer, KafkaConsumer

symbols = [  'BTC-USD', 'ETH-USD', 'USDT-USD', 'BNB-USD', 'USDC-USD', 'XRP-USD'
            , 'ADA-USD', 'STETH-USD', 'DOGE-USD', 'SOL-USD', 'MATIC-USD', 'WTRX-USD'
            , 'DOT-USD', 'TRX-USD', 'LTC-USD', 'BUSD-USD', 'HEX-USD', 'SHIB-USD'
            , 'AVAX-USD', 'DAI-USD', 'WBTC-USD', 'LINK-USD', 'LEO-USD', 'ATOM-USD'
            ,'UNI7083-USD', 'TON-USD', 'FLM-USD', 'DIP-USD', 'STRONG-USD', 'ALBT-USD']
symbols.sort()

def get_stock_prices(stocks):
    data = yf.download(stocks, period='1d', interval='1d')
    current_prices = data['Close'].iloc[-1]
    return current_prices

for i in range(3):
    df = pd.read_csv('output.csv')
    print(df)
    prices = get_stock_prices(symbols)
    list_now = []
    list_now.append(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
    for symbol, price in prices.items():
        list_now.append(price)
    df.loc[len(df)] = list_now
    time.sleep(1)
    df.to_csv('output.csv', encoding='utf-8',index=False)

