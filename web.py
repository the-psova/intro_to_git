from bs4 import BeautifulSoup
from requests import get

from crypto_currency import Crypto


def get_5_crypto() -> list[Crypto]:
    URL = "https://coinmarketcap.com/"
    response = get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    pass
