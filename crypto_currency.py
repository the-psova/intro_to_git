class Crypto:
    def __init__(self, name, price, pct_1h, pct_24h, pct_7d) -> None:
        self.name = name
        self.price = price
        self.pct_1h = pct_1h
        self.pct_24h = pct_24h
        self.pct_7d = pct_7d

    def __str__(self) -> str:
        return (
            f"{self.name}, {self.price}, {self.pct_1h}, {self.pct_24h}, {self.pct_7d}"
        )
