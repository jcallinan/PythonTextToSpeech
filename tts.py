import pyttsx3

engine = pyttsx3.init()  # Object creation

""" RATE """
engine.setProperty('rate', 250)  # Setting up new voice rate
rate = engine.getProperty('rate')  # Getting details of current speaking rate
print(rate)  # Printing current voice rate


""" VOLUME """
volume = engine.getProperty('volume')  # Getting to know current volume level (min=0 and max=1)
print(volume)  # Printing current volume level
engine.setProperty('volume', 1.0)  # Setting up volume level between 0 and 1

""" VOICE """
voices = engine.getProperty('voices')  # Getting details of current voice

for i, voice in enumerate(voices):
    engine.setProperty('voice', voice.id)  # Change the voice
    """ RATE """
    engine.setProperty('rate', 250)  # Setting up new voice rate
    rate = engine.getProperty('rate')  # Getting details of current speaking rate
    print(rate)  # Printing current voice rate
    voice_info = f"Voice {i+1}: ID={voice.id}, Name={voice.name}, Languages={voice.languages}, Gender={voice.gender}"
    print(voice_info)  # Print information about the voice
    engine.say(f"This is voice number {i+1}.")  # Say something using the current voice
    engine.say('My current speaking rate is ' + str(rate))
    engine.runAndWait()
    # Saving voice to a file. Name the file according to the voice number for demonstration purposes.
    engine.save_to_file(f"This is voice number {i+1}. My current speaking rate is {rate}.", f'voice_{i+1}.mp3')

engine.stop()
