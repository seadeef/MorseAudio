from pydub import AudioSegment

morse_dict = {".-": "A", "-...": "B", "-.-.": "C", 
              "-..": "D", ".": "E", "..-.": "F", 
              "--.": "G", "....": "H", "..": "I", 
              ".---": "J", "-.-": "K", ".-..": "L", 
              "--": "M", "-.": "N", "---": "O", 
              ".--.": "P", "--.-": "Q", ".-.": "R", 
              "...": "S", "-": "T", "..-": "U", 
              "...-": "V", ".--": "W", "-..-": "X", 
              "-.--": "Y", "--..": "Z", ".----": "1", 
              "..---": "2", "...--": "3", "....-": "4", 
              ".....": "5", "-....": "6", "--...": "7", 
              "---..": "8", "----.": "9", "-----": "0", 
              "--..--": ", ", ".-.-.-": ".", "..--..": "?", 
              "-..-.": "/", "-....-": "-", "-.--.": "(", "-.--.-": ")"}

class Decode:
    def __init__(self, path, format):
        self.audio = AudioSegment.from_file(path, format=format)   
        self.baseline = self.audio.dBFS # Gets average loudness of audio
        self.segments = []
        self.pauses = []

    def process_segments(self):
        # Splits audio into a stream of "loud" and "quiet" chunks compared to baseline
        for end in range(0, len(self.audio), 5):
            segment = self.audio[end-10:end]
            if segment.dBFS > self.baseline:
                self.segments.append(True)
            else:
                self.segments.append(False)

    def process_pauses(self):
        pauses = {}
        counter = 0

        # Counts how many times each length of "pause" occurs
        # 3 most common lengths should be manifested as dit length, dash length, and space length
        for segment in self.segments:
            if not segment:
                counter += 1
            elif counter != 0:
                # Chunks lengths +/- 2 occurrences together
                for pause in pauses:
                    if -2 < (pause-counter) < 2:
                        counter = pause
                try:
                    pauses[counter] += 1
                except KeyError:
                    pauses[counter] = 1
                counter = 0

        # Extracts 3 most common keys
        self.pauses = sorted(pauses.keys(), key=lambda key: pauses[key], reverse=True)[:3]

    def segments_to_morse(self):
        morse = []
        counter = 0
        switch = True
        
        # Alternates between counting 1s and 0s in self.segments
        # Uses self.pauses to decide what type of beep/pause there was
        for segment in self.segments:
            if segment:
                if switch:
                    counter += 1 # Count 1s
                elif counter != 0: # Runs when a chain of 0s switches to 1
                    if (self.pauses[0]+self.pauses[1])/2 < counter < (self.pauses[1]+self.pauses[2])/2:
                        morse.append(" ")
                    elif (self.pauses[1]+self.pauses[2])/2 < counter:
                        morse.append(" / ")
                    switch = not(switch)
                    counter = 0
                    
            else:
                if not switch:
                    counter += 1 # Count 0s
                elif counter != 0: # Runs when a chain of 1s switches to 0
                    if 0 < counter < (self.pauses[0]+self.pauses[1])/2:
                        morse.append(".")
                    else:
                        morse.append("-")
                    switch = not(switch)
                    counter = 0

        return "".join(morse)

    def morse_to_ascii(self, morse):
        text = []
        words = morse.split()

        #Finally just convert morse to plaintext
        for word in words:
            if word == "/":
                text.append(" ")
            else:
                try:
                    text.append(morse_dict[word])
                except KeyError:
                    text.append("�")
        return "".join(text)

    def decode(self):
        self.process_segments()
        self.process_pauses()
        morse = self.segments_to_morse()
        return self.morse_to_ascii(morse)