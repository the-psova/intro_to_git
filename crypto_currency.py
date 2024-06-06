class Crypto:
    def __init__(
        self, name, value, trend_24h, trend_24h_value, trend_7d, trend_7d_value
    ) -> None:
        self.name = name
        self.value = value
        self.trend_24h = trend_24h
        self.trend_24h_value = trend_24h_value
        self.trend_7d = trend_7d
        self.trend_7d_value = trend_7d_value

    def __str__(self) -> str:
        return f"{self.name}, {self.value}, 24H: {self.trend_24h} {self.trend_24h_value}, 7D: {self.trend_7d} {self.trend_7d_value}"
