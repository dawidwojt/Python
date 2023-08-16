import yfinance as yf
import pandas as pd
from datetime import datetime
import time
#from kafka import KafkaProducer, KafkaConsumer



# Lista interesujących nas krypto.
# Na ten moment wybrałem kilka popularnych i najbardziej aktywnych krypto żeby mieć dane a nie nulle
symbols = [  'BTC-USD', 'ETH-USD', 'USDT-USD', 'BNB-USD', 'USDC-USD', 'XRP-USD'
            , 'ADA-USD', 'STETH-USD', 'DOGE-USD', 'SOL-USD', 'MATIC-USD', 'WTRX-USD'
            , 'DOT-USD', 'TRX-USD', 'LTC-USD', 'BUSD-USD', 'HEX-USD', 'SHIB-USD'
            , 'AVAX-USD', 'DAI-USD', 'WBTC-USD', 'LINK-USD', 'LEO-USD', 'ATOM-USD'
            ,'UNI7083-USD', 'TON-USD', 'FLM-USD', 'DIP-USD', 'STRONG-USD', 'ALBT-USD']
# sortuje zeby ceny wrzucaly sie w dobre kolumny w pozniejszym loopie
symbols.sort()
temp_list = ['DateTime']
temp_list = temp_list + symbols

# tworzenie df i zapisanie do pliku csv
df = pd.DataFrame(columns=temp_list)
df.to_csv('output.csv', encoding='utf-8',index=False)