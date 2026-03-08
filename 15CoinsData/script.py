from datetime import datetime, timedelta
from pricehub import get_ohlc

# time range
end_date = datetime.now()
start_date = end_date - timedelta(days=365*6)

# coin list
coins = [
    "BTCUSDT","ETHUSDT","BNBUSDT","SOLUSDT","XRPUSDT",
    "ADAUSDT","DOGEUSDT","MATICUSDT","DOTUSDT","LTCUSDT",
    "TRXUSDT","AVAXUSDT","LINKUSDT","ATOMUSDT","UNIUSDT"
]

for coin in coins:
    print(f"Downloading {coin}...")

    df = get_ohlc(
        broker="binance_spot",
        symbol=coin,
        interval="1d",
        start=start_date,
        end=end_date
    )

    # keep only OHLCV
    df = df[["Open","High","Low","Close","Volume"]]

    # save file
    df.to_csv(f"{coin}_OHLCV_5years.csv")