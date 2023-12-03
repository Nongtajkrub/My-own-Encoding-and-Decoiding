class Decode:

    def __init__(self, decode_char, data) -> None:
        self.encode_value = data 
        self.decode_char = decode_char

    def decode(self, string = "", result = ""):
        for i, v in enumerate(self.encode_value, start = 1):
            string += v
            if i % 3 == 0:
                result += self.decode_char[string]
                string = ""
        return result