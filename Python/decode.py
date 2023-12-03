class Decode:

    def __init__(self, decode_char, data) -> None:
        self.encode_value = data 
        self.decode_char = decode_char
        self.formatForDecode()

    def formatForDecode(self, string = "", format_result = []):
        self.encode_value = self.encode_value.split()
        for i in self.encode_value:
            for j, v in enumerate(i, start = 1):
                string += v
                if j % 3 == 0:
                    format_result.append(string)
                    string = ""
        self.encode_value = format_result

    def formatDecode(self, decode_value, decode_result = ""):
        for i in decode_value:
            decode_result += i
        return decode_result

    def decode(self, decode_value = []):
        for i in self.encode_value:
            decode_value.append(self.decode_char[i])
        return self.formatDecode(decode_value)