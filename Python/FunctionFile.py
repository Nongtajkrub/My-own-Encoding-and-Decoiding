def print_s(Print, Color):
    ColorDict = {"Yellow":"\033[93m", "Green":"\033[92m", "Blue":"\033[94m", "Green":"\033[92m", "Red":"\033[91m", "White":"\033[97m"}
    print(ColorDict[Color] + Print + "\033[0m")

def input_s(Print, Color):
        ColorDict = {"Yellow":"\033[93m", "Green":"\033[92m", "Blue":"\033[94m", "Green":"\033[92m", "Red":"\033[91m", "White":"\033[97m"}
        return str(ColorDict[Color] + Print + "\033[0m")