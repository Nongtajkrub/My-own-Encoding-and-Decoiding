import FunctionFile as fu
import encode, decode
import json

class Ui:

    def __init__(self) -> None:
        with open("decodeandencode.json", "r") as file: encode_char = json.load(file)
        self.encode_char = encode_char 
        with open("decodeandencode.json", "r") as file: decode_char = json.load(file)
        self.decode_char = decode_char

    def mainMenu(self):
        fu.print_s("Welcome to encode and decode", "Red")
        text = input(fu.input_s("Text: ", "Green"))
        fu.print_s("encode\ndecode", "Blue")
        choice = input(fu.input_s("Enter your choice: ", "Red"))
        if choice == "en":
            encoding = encode.Encode(encode_char = self.encode_char["encode"], data = text)
            print(encoding.encode())
        elif choice == "de":
            decoding = decode.Decode(decode_char = self.decode_char["decode"], data = text)
            print(decoding.decode())
        else: fu.print_s("Pls enter a valid choice\n", "Red"); self.mainMenu()
        text = ""; print('\n'); self.mainMenu()

ui = Ui()