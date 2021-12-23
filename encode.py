from pydub import AudioSegment
from pydub import generators
from random import randint

ascii_dict = {"A": ".-", "B": "-...", "C": "-.-.", 
              "D": "-..", "E": ".", "F": "..-.", 
              "G": "--.", "H": "....", "I": "..", 
              "J": ".---", "K": "-.-", "L": ".-..", 
              "M": "--", "N": "-.", "O": "---", 
              "P": ".--.", "Q": "--.-", "R": ".-.", 
              "S": "...", "T": "-", "U": "..-", 
              "V": "...-", "W": ".--", "X": "-..-", 
              "Y": "-.--", "Z": "--..", "1": ".----", 
              "2": "..---", "3": "...--", "4": "....-", 
              "5": ".....", "6": "-....", "7": "--...", 
              "8": "---..", "9": "----.", "0": "-----", 
              ", ": "--..--", ".": ".-.-.-", "?": "..--..", 
              "/": "-..-.", "-": "-....-", "(": "-.--.", ")": "-.--.-"}

class Encode:
    def __init__(self, path, format, message, wpm):
        self.tone = generators.Sine(freq=641)
        self.dit = int(1000*(60/(wpm*50)))
        print(self.dit)

        self.path = path
        self.format = format
        self.message = message.upper()

    def ascii_to_morse(self):
        morse = []
        for char in self.message:
            if char == " ":
                morse.append("/")
            else:
                morse.append(ascii_dict[char])
        return morse

    def morse_to_audio(self, morse):
        audio = AudioSegment.empty()
        for letter in morse:
            if letter != "/":
                for char in letter:
                    if char == ".":
                        audio += self.tone.to_audio_segment(duration=self.dit)
                    elif char == "-":
                        audio += self.tone.to_audio_segment(duration=self.dit*3)
                    audio += AudioSegment.silent(duration=self.dit)
                audio += AudioSegment.silent(duration=self.dit*3)
            else:
                audio += AudioSegment.silent(duration=self.dit*7)

        return audio

    def audio_to_file(self, audio):
        audio.export(self.path, format=self.format)

    def encode(self):
        morse = self.ascii_to_morse()
        audio = self.morse_to_audio(morse)
        self.audio_to_file(audio)