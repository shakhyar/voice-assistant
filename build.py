from TTS.inference import *
from chat_driver.main import *

class TaskManagement:
	"""
	
	We can add various tasks, like writing notes, remembering things that the user says,
	connecting automatically to wifi, turning lights on or off, and vice versa

	"""
	pass



uinp = input(">>> ")

while True:
	get_audio(chat(uinp))