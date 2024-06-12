from bs4 import BeautifulSoup
from requests import get
from tabulate import tabulate


def main():
    """
    Main function to initiate the script and print the cryptocurrency table.

    This function calls `print_crypto_table` with a predefined number of rows to display.
    """
    print_crypto_table(5)


def get_values(column_name: str) -> tuple[str]:
    """
    Fetches values for a given column from the CoinMarketCap website.

    Args:
        column_name (str): The name of the column to fetch data for. Valid names are:
            "position", "name", "price", "pct_1h", "pct_24h", "pct_7d", "cap",
            "volume_24h", and "supply".

    Returns:
        tuple[str]: A tuple containing the values for the specified column.

    Raises:
        ValueError: If the provided column_name is not valid.
    """

    # Dictionary mapping column names to their respective CSS selectors
    css_selectors = {
        "position": "table > tbody > tr > td:nth-child(2) > p",
        "name": 'table tbody tr td p[font-weight="semibold"]',
        "price": "table > tbody > tr > td:nth-child(4) > div > span",
        "pct_1h": "table > tbody > tr > td:nth-child(5) > span",
        "pct_24h": "table > tbody > tr > td:nth-child(6) > span",
        "pct_7d": "table > tbody > tr > td:nth-child(7) > span",
        "cap": 'table tbody tr td p span[data-nosnippet="true"]',
        "volume_24h": "table > tbody > tr > td:nth-child(9) > div > a > p",
        "supply": "table > tbody > tr > td:nth-child(10) > div > div > p",
    }

    # Check if the provided column_name is valid
    if column_name not in css_selectors.keys():
        raise ValueError(f"Invalid column name.")

    # URL of the website to scrape
    URL = "https://coinmarketcap.com/"
    # Make a request to the website
    response = get(URL)
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, "html.parser")

    # List to store the fetched data
    data = []
    # Select the cells containing the data using the CSS selector
    cells = soup.select(css_selectors[column_name])
    # Extract the text from each cell and add it to the data list
    for cell in cells:
        data.append(cell.text)

    # Return the data as a tuple
    return tuple(data)


def get_rows(num_rows: int) -> tuple[tuple]:
    """
    Constructs rows of cryptocurrency data.

    Args:
        num_rows (int): The number of rows to fetch and construct.

    Returns:
        tuple[tuple]: A tuple of tuples, where each inner tuple represents a row of data
                      with values for position, name, price, 1h %, 24h %, 7d %, market cap,
                      volume (24h), and circulating supply.
    """

    # Column names to fetch
    column_names = (
        "position",
        "name",
        "price",
        "pct_1h",
        "pct_24h",
        "pct_7d",
        "cap",
        "volume_24h",
        "supply",
    )

    # List to store the columns of data
    columns = []
    # Fetch data for each column
    for column_name in column_names:
        columns.append(get_values(column_name))

    # List to store the rows of data
    rows = []
    # Construct each row by taking the corresponding element from each column
    for i in range(num_rows):
        row = []
        for column in columns:
            row.append(column[i])
        row = tuple(row)
        rows.append(row)

    # Return the rows as a tuple
    return tuple(rows)


def print_crypto_table(num_rows: int) -> None:
    """
    Prints a table of cryptocurrency data.

    Args:
        num_rows (int): The number of rows to print.

    Returns:
        None
    """

    # Get the rows of cryptocurrency data
    crypto_rows = get_rows(num_rows)

    # Create a table with headers using the tabulate library
    table = tabulate(
        crypto_rows,
        headers=(
            "#",
            "Name",
            "Price",
            "1h %",
            "24h %",
            "7d %",
            "Market Cap",
            "Volume(24h)",
            "Circulating Supply",
        ),
        tablefmt="grid",
    )

    # Print the table
    print(table)


if __name__ == "__main__":
    main()
