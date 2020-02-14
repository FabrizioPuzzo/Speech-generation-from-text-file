import os
from google.cloud import texttospeech

"""
Class for synthesize text to natural sounding voice/speech using Google Cloud Text-to-Speech
"""


class TextSynthesizer():

	def __init__(self, voice_language_code='en-US', voice_name='en-US-Wavenet-B', gender='male', speaking_rate=1):
		
		# Instantiates a client
		self.client = texttospeech.TextToSpeechClient()
		self.voice_language_code = voice_language_code
		self.voice_name = voice_name
		self.voice_gender = gender
		self.speaking_rate = speaking_rate

	def synthesize_string(self, text_data, filename_audio):

		# Set the text input to be synthesized
		synthesis_input = texttospeech.types.SynthesisInput(text=text_data)

		# Select gender
		if self.voice_gender == 'male':
			voice_gender = texttospeech.enums.SsmlVoiceGender.MALE
		else:
			voice_gender = texttospeech.enums.SsmlVoiceGender.FEMALE

		# Build the voice request, select the language code ("en-US") and the ssml
		# voice gender ("neutral")
		# Available voices: https://cloud.google.com/text-to-speech/docs/voices
		voice = texttospeech.types.VoiceSelectionParams(
			language_code=self.voice_language_code,
        	name=self.voice_name,
			ssml_gender=voice_gender)

		# Select the type of audio file you want returned
		# Modify voice: https://cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize#audioconfig
		audio_config = texttospeech.types.AudioConfig(
			audio_encoding=texttospeech.enums.AudioEncoding.MP3,
			speaking_rate=self.speaking_rate)

		# Perform the text-to-speech request on the text input with the selected
		# voice parameters and audio file type
		response = self.client.synthesize_speech(synthesis_input, voice, audio_config)

		# The response's audio_content is binary.
		with open(filename_audio + '.mp3', 'wb') as out:
			# Write the response to the output file.
			out.write(response.audio_content)
			print('Audio content written to ' + filename_audio)

	def synthesize_text(self, filename_text, filename_audio):

		# Read textfile
		with open(filename_text, 'r') as file:
			text_data = file.read()

		# Synthesis text
		self.synthesize_string(text_data, filename_audio)


	def synthesize_split_text(self, filename_text, filename_audio, split_char):

		# Read textfile
		with open(filename_text, 'r') as file:
			text_data = file.read()

		# Split text
		split_text = text_data.split(split_char)

		part_id = 0
		for text_data in split_text:
			
			# Set filename for audio file
			filename_audio_part = filename_audio + '_part_' + str(part_id)

			# Synthesis text
			self.synthesize_string(text_data, filename_audio_part)

			# Increment part count
			part_id += 1
















