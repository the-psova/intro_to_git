# Crypto Table Scraper

This project is a Python script that scrapes cryptocurrency data from the `CoinMarketCap` website and displays it in a formatted table. The script uses `BeautifulSoup` for web scraping, `Requests` for HTTP requests, and `Tabulate` for displaying the data in a table format.

## Features

- Scrapes cryptocurrency data from CoinMarketCap.
- Displays data in a tabulated format.
- Fetches data for position, name, price, 1-hour percentage change, 24-hour percentage change, 7-day percentage change, market cap, 24-hour volume, and circulating supply.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `tabulate` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/the-psova/intro_to_git.git
   cd intro_to_git
   ```

2. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4 tabulate
   ```

## Usage

Run the script using the following command:

```bash
python web.py
```
