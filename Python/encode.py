class Encode:

    def __init__(self, encode_char, data) -> None:
        self.encode_char = encode_char
        self.data = data

    def encode(self, result = ""):
        for i in self.data:
            result += self.encode_char[i]
        return result