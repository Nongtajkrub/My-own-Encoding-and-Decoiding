import encode, decode
import json, tkinter as tk, pyperclip

class Ui:

    def __init__(self) -> None:
        self.app = tk.Tk()
        with open("decodeandencode.json", "r") as file: en_de_data = json.load(file)
        self.encode_decode_char = en_de_data
        with open("uiconfig.json", "r") as file: config_data = json.load(file)
        self.HEIGHT = config_data["config"]["HEIGHT"]
        self.WIDTH = config_data["config"]["WIDTH"]

    def encode(self):
        user_input_text = self.enter_text_entry.get()
        encoding = encode.Encode(encode_char = self.encode_decode_char["encode"], data = user_input_text)
        self.result = encoding.encode()
        self.result_text.config(text = self.result)

    def decode(self): 
        user_input_text = self.enter_text_entry.get()
        decoding = decode.Decode(decode_char = self.encode_decode_char["decode"], data = user_input_text)
        self.result = decoding.decode()        
        self.result_text.config(text = self.result)

    def copy_text(self):
        pyperclip.copy(self.result)

    def configure(self):
        self.app.title("EncodeAndDecodePython")
        self.app.resizable(width = False, height = False)
        self.app.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.center = {"x": self.WIDTH / 2, "y": self.HEIGHT / 2}

        if self.WIDTH >= 350 and self.HEIGHT >= 350:
            self.ui_info_text = tk.Label(self.app, text = "This is the version 0.2 of the ui")
            self.ui_info_text.pack()
            self.code_info_text = tk.Label(self.app, text = "Current code version 0.3 alpha")
            self.code_info_text.pack()
            self.how_to_use = tk.Label(self.app, text = "If you have trouble using this UI, you can refer to the instruction.txt file or visit the GitHub download page (the download page for this source code) for more information.", wraplength = self.WIDTH - 100)
            self.how_to_use.pack()

            self.enter_text_text = tk.Label(self.app, text = "Enter your text here")
            self.enter_text_text.place(x = self.center["x"], y = self.center["y"] - 50, anchor = tk.CENTER)
            self.enter_text_entry = tk.Entry(self.app, width = 30)
            self.enter_text_entry.place(x = self.center["x"], y = self.center["y"] - 30, anchor = tk.CENTER)
            
            self.choice_encode_button = tk.Button(self.app, text = "Encode", command = self.encode)
            self.choice_encode_button.place(x = self.center["x"] - 30, y = self.center["y"] - 5, anchor = tk.CENTER) 

            self.choice_decode_button = tk.Button(self.app, text = "Decode", command = self.decode)
            self.choice_decode_button.place(x = self.center["x"] + 30, y = self.center["y"] - 5, anchor = tk.CENTER)

            self.result_text = tk.Label(self.app, text = "", wraplength = self.WIDTH - 50)
            self.result_text.place(x = self.center["x"], y = self.center["y"] + 100, anchor = tk.CENTER)

            self.copy_button = tk.Button(self.app, text = "Copy", command = self.copy_text)
            self.copy_button.place(x = self.center["x"], y = self.center["y"] + 50, anchor = tk.CENTER)
        else:
            self.warning_text = tk.Label(self.app, text = "WIDTH AND HEIGHT NEED TO BE MORE THAN 500", wraplength = self.WIDTH - 10)
            self.warning_text.pack()

    def main(self):
        self.configure()
        self.app.mainloop()

ui = Ui()