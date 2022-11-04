class Codec:
    def __init__(self):
        self.base = "https://www.tinyurl.com/"
        self.encodeMap, self.decodeMap = {}, {}

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodeMap:
            shortUrl = self.base + str(len(self.encodeMap) + 1)
            self.encodeMap[longUrl] = shortUrl
            self.decodeMap[shortUrl] = longUrl
        return self.encodeMap[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        return self.decodeMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))