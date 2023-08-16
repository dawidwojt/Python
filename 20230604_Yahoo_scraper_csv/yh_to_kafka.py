import yfinance as yf
import pandas as pd
from datetime import datetime
import time
from kafka import KafkaProducer

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers='broker:9092',
    value_serializer=lambda x: x.encode('utf-8')
)

# Lista interesujących nas krypto.
# Na ten moment wybrałem kilka popularnych i najbardziej aktywnych krypto żeby mieć dane a nie nulle
symbols = ['BTC-USD', 'ETH-USD', 'USDT-USD', 'BNB-USD', 'USDC-USD', 'XRP-USD',
           'ADA-USD', 'STETH-USD', 'DOGE-USD', 'SOL-USD', 'MATIC-USD', 'WTRX-USD',
           'DOT-USD', 'TRX-USD', 'LTC-USD', 'BUSD-USD', 'HEX-USD', 'SHIB-USD',
           'AVAX-USD', 'DAI-USD', 'WBTC-USD', 'LINK-USD', 'LEO-USD', 'ATOM-USD',
           'UNI7083-USD', 'TON-USD', 'FLM-USD', 'DIP-USD', 'STRONG-USD', 'ALBT-USD']

# sortuje zeby ceny wrzucaly sie w dobre kolumny w pozniejszym loopie
symbols.sort()
temp_list = ['DateTime']
temp_list = temp_list + symbols

# tworzenie df i zapisanie do pliku csv
df = pd.DataFrame(columns=temp_list)
df.to_csv('output.csv', encoding='utf-8', index=False)

def get_stock_prices(stocks):
    data = yf.download(stocks, period='1d', interval='1d')
    current_prices = data['Close'].iloc[-1]
    return current_prices

for i in range(2):  # range do ustalenia - ilość obserwacji
    df = pd.read_csv('output.csv')
    print(df)
    prices = get_stock_prices(symbols)
    list_now = []
    list_now.append(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
    for symbol, price in prices.items():
        list_now.append(price)
    df.loc[len(df)] = list_now
    time.sleep(1)  # czas do ustalenia - czas pomiędzy iteracjami odczytywania wyników
    df.to_csv('output.csv', encoding='utf-8', index=False)

with open("output.csv") as f:
    for i, line in enumerate(f):
        if i > 0:
            producer.send('my-topic', line.strip())  # Send each line as a message to Kafka
            producer.flush()