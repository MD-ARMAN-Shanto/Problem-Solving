class Codec:

    def encode(self, longUrl: str) -> str:
        a = longUrl.encode("ascii", "replace")
        return a

    def decode(self, shortUrl: str) -> str:
        b = shortUrl.decode()
        return b
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))