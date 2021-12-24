from encode import Encode
from decode import Decode

def main():
    print("[E]ncode a plaintext message into a Morse audio file")
    print("[D]ecode a Morse audio file into a plaintext message")
    choice = input("Choose an option: ").lower()

    while not(choice == "e" or choice == "d"): # Force user to pick valid option
        choice = input("Please choose a valid option: ").lower()

    while True:
        try:
            # Ask for encode parameters
            if choice == "e":
                path = input("Enter the filename to save to: ")
                format = input("Enter the file's format (.ext): ")
                message = input("Enter the message to encode: ")
                wpm = input("Enter the wpm to encode at: ")

                enc_instance = Encode(path, format, message, wpm)
                enc_instance.encode()
                print("Message successfully encoded!")
            # Ask for decode parameters
            else:
                path = input("Enter the file's path: ")
                format = input("Enter the file's format (.ext): ")

                dec_instance = Decode(path, format)
                decoded = dec_instance.decode()
                print(f"Decoded message: '{decoded}'")
            break # Quit program if successful
        # Loop if error
        except KeyboardInterrupt:
            quit()
        except Exception as e:
            print("An error ocurred, please enter valid parameters")

if __name__ == '__main__':
    main()
