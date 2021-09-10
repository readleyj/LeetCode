class Codec:
    long_to_short_map = dict()
    short_to_long_map = dict()

    def encode(self, longUrl: str) -> str:
        short_url = str(len(self.long_to_short_map))
        self.long_to_short_map[longUrl] = short_url
        self.short_to_long_map[short_url] = longUrl
        return short_url

    def decode(self, shortUrl: str) -> str:
        return self.short_to_long_map[shortUrl]
