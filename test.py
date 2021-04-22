import pandas as pd
from stoch_rsi import stoch_rsi_tradingview
from rsi import rsi_tradingview

if __name__ == '__main__':
    ohlc = pd.read_csv("EURUSD.csv", index_col="date")

    rsi = rsi_tradingview(ohlc)
    print("RSI: ")
    for i in range(len(rsi)):
        print(f"Date={ohlc.index[i]}\tRSI={rsi[i]}")

    rsi, stochrsi_K, stochrsi_D = stoch_rsi_tradingview(ohlc)
    print("\n\nSTOCH_RSI: ")
    for i, v in rsi.items():
        print(f"Date={ohlc.index[i]}\tRSI={rsi[i]}\tK={stochrsi_K[i]}\tD={stochrsi_D[i]}")
