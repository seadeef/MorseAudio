from pydub import generators

morse_dict = {".-": "A",   "-...": "B",   "-.-.": "C",
              "-..": "D",      ".": "E",   "..-.": "F",
              "--.": "G",   "....": "H",     "..": "I",  
              ".---": "J",    "-.-": "K",   ".-..": "L",
              "--": "M",     "-.": "N",    "---": "O", 
              ".--.": "P",   "--.-": "Q",    ".-.": "R",
              "...": "S",      "-": "T",    "..-": "U", 
              "...-": "V",    ".--": "W",   "-..-": "X",
              "-.--": "Y",   "--..": "Z",  "-----": "0", 
              ".----": "1",  "..---": "2",  "...--": "3",
              "....-": "4",  ".....": "5",  "-....": "6", 
              "--...": "7",  "---..": "8",  "----.": "9"}

class Encode:
    def __init__(self, path, format, message, wpm):
        self.tone = generators.Sine(freq=641)

        self.path = path
        self.format = format
        self.message = message
        self.wpm = wpm

    def ascii_to_morse(self):
        pass

    def morse_to_audio(self, morse):
        pass

    def audio_to_file(self):
        pass

    def encode(self):
        morse = self.ascii_to_morse()
        self.morse_to_audio(morse)
        self.audio_to_file()