import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ccxt

def trade():

    client = ccxt.binance({'enableRateLimit': True, 'timeout': 30000 })
    
    btc_quote = client.fetch_ohlcv("BTCUSDT", timeframe='1d', limit=730)
    btc_quote_df = pd.DataFrame(btc_quote, dtype=float)
    
    btc_quote_df['time'] = pd.to_datetime(btc_quote_df[0], unit='ms')
    btc_quote_df['ma7'] = btc_quote_df[4].rolling(window=7).mean()
    btc_quote_df['ma25'] = btc_quote_df[4].rolling(window=25).mean()
    btc_quote_df['ma50'] = btc_quote_df[4].rolling(window=50).mean()
    
    fig, ax = plt.subplots(figsize=(20, 5), layout='constrained')
    ax.plot(btc_quote_df['time'], btc_quote_df.values[:,4], label='Close')
    ax.plot(btc_quote_df['time'], btc_quote_df['ma7'], label='MA7')
    ax.plot(btc_quote_df['time'], btc_quote_df['ma25'], label='MA25')
    ax.plot(btc_quote_df['time'], btc_quote_df['ma50'], label='MA50')
    ax.legend()
    plt.show()

trade()
