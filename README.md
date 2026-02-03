# Binance Futures Trading Bot (Testnet)

A simplified Python trading bot built using Binance Futures Testnet (USDT-M).  
This project was developed as part of a Python Developer hiring assignment to demonstrate API integration, CLI input handling, logging, and clean code structure.

---

## Features

- Place MARKET and LIMIT orders on Binance Futures Testnet
- Supports BUY and SELL order sides
- Interactive CLI-based user input
- Input validation with clear error messages
- Structured and reusable codebase
- Logs API requests, responses, and errors
- Proper exception handling for API and validation errors

---

## Project Structure

final_trade/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── trading.log
├── requirements.txt
├── .gitignore
└── README.md

---

## Setup Instructions

1. Clone the repository

git clone https://github.com/Manasa164/binance-futures-trading-bot.git  
cd binance-futures-trading-bot

2. Create and activate virtual environment

python -m venv venv  
venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

---

## Environment Variables

Create a `.env` file in the project root and add:

API_KEY=your_testnet_api_key  
API_SECRET=your_testnet_api_secret

Note:
- The `.env` file is ignored using `.gitignore`
- API credentials are never committed to GitHub

---

## How to Run

Start the CLI application:

python cli.py

You will be prompted to enter:
- Symbol (example: BTCUSDT)
- Side (BUY / SELL)
- Order type (MARKET / LIMIT)
- Quantity
- Price (required only for LIMIT orders)

---

## Example Usage

LIMIT Order Example:

Symbol: BTCUSDT  
Side: SELL  
Order type: LIMIT  
Quantity: 0.001  
Price: 30000  

The CLI prints:
- Order request summary
- Order response details (orderId, status, executedQty, avgPrice if available)
- Success or failure message

---

## Logging

All API requests, responses, and errors are logged into:

trading.log

The log file contains:
- One MARKET order attempt
- One LIMIT order attempt

---

## Assumptions and Notes

- Uses Binance Futures Testnet (USDT-M) only
- System time must be synchronized to avoid timestamp errors
- Some orders may fail due to testnet limitations or API restrictions
- This project is intended for evaluation and learning purposes

---

## Requirements

- Python 3.x
- python-binance
- python-dotenv

---

## Author

Manasa Bandi  
Junior Python Developer Applicant

---

## License

This project is provided strictly for assignment evaluation purposes.
