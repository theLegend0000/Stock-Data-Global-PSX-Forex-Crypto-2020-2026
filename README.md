# Crypto OHLCV Dataset (15 Coins)

This repository contains scripts and datasets for collecting **OHLCV (Open, High, Low, Close, Volume)** data for multiple cryptocurrency pairs using the `pricehub` Python library.

The data was collected from exchanges such as **Binance Spot** using the PriceHub package.

---

# Important Requirement

The scripts in this repository will **ONLY run if the `pricehub` library is installed**.

You must install the library from the official repository:

https://github.com/eslazarev/pricehub

## Installation

Install the library using pip:

```bash
pip install pricehub
```

After installing the library, the scripts in this repository will work correctly.
# 15CoinsData

This folder contains **separate OHLCV datasets for each cryptocurrency pair**.

Each file contains approximately **5 years of historical OHLCV data**.

## Example Files

```
BTCUSDT_OHLCV_5years.csv
ETHUSDT_OHLCV_5years.csv
BNBUSDT_OHLCV_5years.csv
SOLUSDT_OHLCV_5years.csv
...
```
# Combined15CoinsData

This folder contains **a combined dataset containing all 15 coins in one file**.

## File

```
combined_15coins_OHLCV.csv
```

This dataset merges the OHLCV data from all coins into one dataset.
# Dataset Details

- Exchange: Binance Spot
- Data type: OHLCV
- Time range: ~5 years
- Coins: 15 cryptocurrency pairs
- File format: CSV

---

# Acknowledgment

Market data collection is powered by the **PriceHub** library.

Official repository:

https://github.com/eslazarev/pricehub

---

# License

This repository is intended for **learning, research, and data analysis purposes**.
