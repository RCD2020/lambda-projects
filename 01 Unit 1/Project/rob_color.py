'''
Robert Davis
2021/07/27
'''

class styles:
    '''
    Stores several useful ANSI escape codes to format your terminal output. Attach values to print statements to change following text.
    '''
    reset = '\033[00m'

    class style:
        'Contains styles of the text such as bold and italic.'
        bold = '\033[01m'
        dim = '\033[02m'
        italic = '\033[03m'
        underline = '\033[04m'
        swapgrounds = '\033[07m'
        hide = '\033[08m'

    class remove:
        'Use this to remove styles.'
        styles = '\033[00m'
        bold = '\033[22m'
        dim = '\033[22m'
        italic = '\033[23m'
        underline = '\033[24m'
        swapgrounds = '\033[27m'
        hide = '\033[28m'

    class fg:
        'Changes color of text.'
        default = '\033[39m'

        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        yellow = '\033[33m'
        blue = '\033[34m'
        magenta = '\033[35m'
        cyan = '\033[36m'
        white = '\033[37m'
        gray = '\033[90m'
        
        red_bright = '\033[91m'
        green_bright = '\033[92m'
        yellow_bright = '\033[93m'
        blue_bright = '\033[94m'
        magenta_bright = '\033[95m'
        cyan_bright = '\033[96m'
        white_bright = '\033[97m'
        
        color256 = lambda num : f"\033[38;5;{num}m"

        rgb = lambda r, g, b : f"\033[38;2;{r};{g};{b}m"

    class bg:
        'Changes color of the background of the text.'
        default = '\033[49m'

        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        yellow = '\033[43m'
        blue = '\033[44m'
        magenta = '\033[45m'
        cyan = '\033[46m'
        white = '\033[47m'
        gray = '\033[100m'
        
        red_bright = '\033[101m'
        green_bright = '\033[102m'
        yellow_bright = '\033[103m'
        blue_bright = '\033[104m'
        magenta_bright = '\033[105m'
        cyan_bright = '\033[106m'
        white_bright = '\033[107m'

        color256 = lambda num : f"\033[48;5;{num}m"

        rgb = lambda r, g, b : f"\033[48;2;{r};{g};{b}m"