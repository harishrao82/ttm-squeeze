import os
import yfinance as yf
file='allstock.csv'
with open(file) as f:
    lines = f.read().splitlines()
    for sym in lines:
        symbol=sym.upper()
        try:
            msft = yf.Ticker(symbol)
            avgvol10day=int(msft.info['averageDailyVolume10Day'])
            avgvol=int(msft.info['averageVolume'])
            vol=int(msft.info['volume'])
            mktcap=int(msft.info['marketCap'])
            mycap=4000000000
            print(symbol,avgvol,avgvol10day,vol,mktcap)
            if ( avgvol10day > avgvol ) and ( vol  > avgvol10day ) and ( mktcap < mycap ):
                print("Matched",symbol)
                data = yf.download(symbol, start="2020-09-01", end="2021-02-12")
                data.to_csv("datasets/{}.csv".format(symbol))
        except:
            pass