import os
from text_synthesizer import TextSynthesizer

# Parameters
FILENAME_TEXT = './text_files/example.txt'			# File with text that will be transformed to speech
FILENAME_AUDIO_OUT = './audio_files/example_audio'	# Outputfile

# Voice parameters
# For reference see: 
#	https://cloud.google.com/text-to-speech/docs/voices
#	https://cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize#audioconfig
VOICE_LANGUAGE_CODE = 'en-US'
VOICE_NAME = 'en-US-Wavenet-D'
VOICE_GENDER = 'male'
VOICE_SPEAKING_RATE = 0.95

# Text parameters
SPLIT_CHAR = '\n\n'		#Character by which the Text is plit when calling the Method TextSynthesizer.synthesize_split_text

# Set credentials for google api
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ''

# Creat object
text_syn = TextSynthesizer(VOICE_LANGUAGE_CODE, VOICE_NAME, VOICE_GENDER, VOICE_SPEAKING_RATE)

# Synthesize text - complete textfile to one audio file
text_syn.synthesize_text(FILENAME_TEXT, FILENAME_AUDIO_OUT)

# Synthesize text - split textfile by SPLIT_CHAR and synthesize parts
text_syn.synthesize_split_text(FILENAME_TEXT, FILENAME_AUDIO_OUT, SPLIT_CHAR)


