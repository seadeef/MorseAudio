from pydub import AudioSegment

ascii_dict = {"A": ".-",     "B": "-...",   "C": "-.-.", 
              "D": "-..",    "E": ".",      "F": "..-.",
              "G": "--.",    "H": "....",   "I": "..",
              "J": ".---",   "K": "-.-",    "L": ".-..",
              "M": "--",     "N": "-.",     "O": "---",
              "P": ".--.",   "Q": "--.-",   "R": ".-.",
              "S": "...",    "T": "-",      "U": "..-",
              "V": "...-",   "W": ".--",    "X": "-..-",
              "Y": "-.--",   "Z": "--..",   "0": "-----",
              "1": ".----",  "2": "..---",  "3": "...--",
              "4": "....-",  "5": ".....",  "6": "-....",
              "7": "--...",  "8": "---..",  "9": "----."}

class Decode:
	def __init__(self, path, format):
		self.audio = AudioSegment.from_file(path, format=format)
		self.segments = []

	def process_segments(self):
		pass

	def get_dit(self):
		pass

	def segments_to_morse(self, dit):
		pass

	def morse_to_ascii(self, morse):
		pass

	def decode(self):
		self.process_segments()
		dit = self.get_dit()
		morse = self.segments_to_morse(dit)
		return self.morse_to_ascii(morse)