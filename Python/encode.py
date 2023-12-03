class Encode:

    def __init__(self, encode_char, data) -> None:
        self.encode_char = encode_char
        self.data = data
        self.encode_value = []

    def formathEncode(self, encode_value, result = ""):
        for i in encode_value:
            result += i
        return result

    def encode(self):
        for i in self.data:
            self.encode_value.append(self.encode_char[i])
        return self.formathEncode(self.encode_value)