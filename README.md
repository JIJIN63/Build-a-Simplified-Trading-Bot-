# Binance Futures Testnet Trading Bot

A simple Python CLI application for placing **Market** and **Limit** orders on **Binance USDⓈ-M Futures Testnet**.

## Features

* Place **MARKET** and **LIMIT** orders
* Supports both **BUY** and **SELL**
* CLI input via `argparse`
* Input validation for symbol, side, order type, quantity, and price
* Structured project layout:

  * `client.py` → Binance API client / signed requests
  * `orders.py` → order placement logic
  * `validators.py` → CLI input validation
  * `logging_config.py` → file + console logging
* Logs API requests, responses, and errors
* Handles:

  * invalid user input
  * Binance API errors
  * network/request failures

---

## Project Structure

```text
trading_bot/
│
├─ bot/
│  ├─ __init__.py
│  ├─ client.py
│  ├─ orders.py
│  ├─ validators.py
│  └─ logging_config.py
│
├─ logs/
│  └─ .gitkeep
│
├─ cli.py
├─ .env.example
├─ requirements.txt
└─ README.md
```

---

## Setup

### 1) Clone the repository

```bash
git clone <your-repo-url>
cd trading_bot
```

### 2) Create and activate a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure environment variables

Copy `.env.example` to `.env` and fill in your Binance Futures Testnet credentials:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
BINANCE_BASE_URL=https://testnet.binancefuture.com
```

---

## Usage

### MARKET order example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT order example

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

---

## Example Output

### Request summary

```text
=== ORDER REQUEST SUMMARY ===
symbol: BTCUSDT
side: BUY
type: MARKET
quantity: 0.001
```

### Response details

```text
=== ORDER RESPONSE DETAILS ===
orderId: 123456789
status: NEW
executedQty: 0.001
avgPrice: 0.0
symbol: BTCUSDT
side: BUY
type: MARKET
```

---

## Logging

Logs are written to:

```text
logs/trading_bot.log
```

The log file includes:

* API request details
* API response details
* validation errors
* network/API exceptions

---

## Assumptions

1. The bot is intended for **Binance USDⓈ-M Futures Testnet only**.
2. Only **MARKET** and **LIMIT** orders are implemented for the core task.
3. LIMIT orders use `timeInForce=GTC`.
4. The user provides a valid Binance Futures Testnet API key and secret.
5. Exchange-specific validations such as lot size / tick size are not fetched dynamically in this version; only general CLI validation is implemented.

---

## Notes

* This project uses **direct REST API calls** instead of `python-binance`.
* Signed requests are generated using **HMAC SHA256**.
* The order endpoint used is the Binance **USDⓈ-M Futures** testnet order endpoint.

---

## Deliverables included

* Source code
* README
* `requirements.txt`
* Log file(s) demonstrating:

  * one MARKET order
  * one LIMIT order
