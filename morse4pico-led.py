import time
from machine import Pin

# Set the GPIO number your LED is connector to
LED_PIN = 16

MORSE = {'A': '.-',    'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

MORSE_REVERSED = {value:key for key,value in MORSE.items()}

def banner():
    print("    __  ___                     __ __  ____  _           ")
    print("   /  |/  /___  _____________  / // / / __ \(_)________  ")
    print("  / /|_/ / __ \/ ___/ ___/ _ \/ // /_/ /_/ / / ___/ __ \ ")
    print(" / /  / / /_/ / /  (__  )  __/__  __/ ____/ / /__/ /_/ / ")
    print("/_/  /_/\____/_/  /____/\___/  /_/ /_/   /_/\___/\____/  ")
    print("======================================================== ")
    return None


# Does not follow Farnsworth timing exactly, oh well...
# Just trying to have fun!
def dot():
    led = Pin(LED_PIN, Pin.OUT)
    led.value(1)
    time.sleep(0.2)
    led.value(0)
    time.sleep(0.2)


def dash():
    led = Pin(LED_PIN, Pin.OUT)
    led.value(1)
    time.sleep(0.6)
    led.value(0)
    time.sleep(0.2)


def to_morse(string_arg):
    print(' '.join(MORSE.get(i.upper()) for i in string_arg))
    return None


def from_morse(string_arg):
    print(''.join(MORSE_REVERSED.get(i) for i in string_arg.split()))
    return None


# Would you like to translate or create Morse code
answer = None 
while answer not in ("1", "2"):
    banner()
    print("1) Morse code to text. For example: ... --- ... => SOS")
    print("2) Text to Morse code. For example: SOS => ... --- ...")
  
    answer = input("Enter '1' or '2': ") 
    if answer == "1":
        print()
        morse2text = input("Enter Morse code to translate to text: ")
        from_morse(morse2text)
    elif answer == "2":
        print()
        text2morse = input("Enter text to transform into Morse code: ")
        to_morse(text2morse)
        for letter in text2morse:
            for symbol in MORSE[letter.upper()]:
                if symbol == '-':
                    dash()
                elif symbol == '.':
                    dot()
                else:
                    time.sleep(1.4)
    else: 
        print("Please enter '1' or '2' from the menu.")
