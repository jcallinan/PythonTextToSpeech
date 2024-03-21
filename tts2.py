import pyttsx3
import sys

# Check if the user has provided a file name as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py input.txt")
    sys.exit(1)

# The first command line argument is the input file name
input_file_name = sys.argv[1]

# Generate the output file name by replacing the input file extension with '.mp3'
output_file_name = input_file_name.rsplit('.', 1)[0] + '.mp3'

# Initialize the TTS engine
engine = pyttsx3.init()

# Set rate
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 125)

# Set volume
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume', 1.0)

# Set voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change the index for different voices

# Read text from the specified file
try:
    with open(input_file_name, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print(f"Error: The file {input_file_name} was not found.")
    sys.exit(1)

# Use the text from the file
engine.say(text)
engine.save_to_file(text, output_file_name)  # Saving voice to a file with modified file name
engine.runAndWait()  # Wait for the speech to finish
engine.stop()
