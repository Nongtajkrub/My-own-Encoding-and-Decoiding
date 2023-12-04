import functionfile as fu
import encode, decode
import json, tkinter as tk

class Ui:

    def __init__(self) -> None:
        self.app = tk.Tk()
        with open("decodeandencode.json", "r") as file: data = json.load(file)
        self.encode_decode_char = data
        self.result = ""

    def getUserInputText(self):
        self.user_input_text = self.enter_text_entry.get()

    def getUserInputChoice(self):
        self.user_input_choice = self.enter_choice_entry.get()

    def processing(self): 
        if self.user_input_choice == "encode":
            encoding = encode.Encode(encode_char = self.encode_decode_char["encode"], data = self.user_input_text)
            self.result = encoding.encode()
        if self.user_input_choice == "decode":
            decoding = decode.Decode(decode_char = self.encode_decode_char["decode"], data = self.user_input_text)
            self.result = decoding.decode()        
        self.result_text.config(text = self.result)

    def configure(self):
        self.app.title("EncodeAndDecodePython")
        self.app.geometry("500x500")
        
        self.ui_info_text = tk.Label(self.app, text = "This is the version 0.1 of the ui")
        self.ui_info_text.pack()
        self.code_info_text = tk.Label(self.app, text = "Current code version 0.3 alpha")
        self.code_info_text.pack()
        self.how_to_use = tk.Label(self.app, text = "If you have trouble using this UI, you can refer to the instruction.txt file\n or visit the GitHub download page (the download page for this source code)\n for more information.")
        self.how_to_use.pack()

        self.enter_text_text = tk.Label(self.app, text = "Enter your text here")
        self.enter_text_text.place(x = 250, y = 150, anchor = tk.CENTER)
        self.enter_text_entry = tk.Entry(self.app, width = 30)
        self.enter_text_entry.place(x = 250, y = 170, anchor = tk.CENTER)
        self.get_text_entry = tk.Button(self.app, text = "Enter", command = self.getUserInputText)
        self.get_text_entry.place(x = 250, y = 200, anchor = tk.CENTER)
        
        self.choice_text_text = tk.Label(self.app, text = "Enter your choice here")
        self.choice_text_text.place(x = 250, y = 280, anchor = tk.CENTER)
        self.enter_choice_entry = tk.Entry(self.app, width = 30)
        self.enter_choice_entry.place(x = 250, y = 300, anchor = tk.CENTER)     
        self.get_choice_entry = tk.Button(self.app, text = "Enter", command = self.getUserInputChoice)
        self.get_choice_entry.place(x = 250, y = 330, anchor = tk.CENTER)

        self.done_button = tk.Button(self.app, text = "Done", command = self.processing)
        self.done_button.place(x = 250, y = 450, anchor = tk.CENTER)

        #self.help_button = tk.Button(self.app, text = "Help")
        #self.help_button.place(x = 30, y = 30, anchor = tk.CENTER)

        self.result_text = tk.Label(self.app, text = "")
        self.result_text.place(x = 250, y = 400, anchor = tk.CENTER)

    def main(self):
        self.configure()
        self.app.mainloop()

ui = Ui()