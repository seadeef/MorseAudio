# MorseAudio
A Python tool to create and decode audio files of Morse Code

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `pydub` and make sure all source files are in the same directory before running. If you plan to use non-WAV files also make sure [ffmpeg](https://ffmpeg.org/) is installed on your system.

## Usage
Run `python3 main.py` to use MorseAudio. You can choose to either [E]ncode or [D]ecode an audio file. Each option requires the target file's path and format (enter as "mp3", "wav, etc.). For encoding you also must supply a message and wpm (based on "PARIS").

## Limitations
MorseAudio should generally be pretty tolerant of imperfections, but I have not been able to get my hand on some human-generated samples for testing. Sometimes spaces may be incorrect in the generated message, but for the most part individual letters are correct. Signal detection is based on loudness, and a sharp beep may not be able to overcome background noise within the audio (planning to fix).