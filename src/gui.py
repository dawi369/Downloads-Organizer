import time
import inquirer
from organizer import JsonHelper


class GUI:
	def __init__(self):
		GUI.print_ascii_art()

		JsonHelper.set_only_default_profile_to_current()







		# questions = [
		# 	inquirer.List('size',
		# 	              message="What size do you need?",
		# 	              choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
		# 	              ),
		# ]
		# answers = inquirer.prompt(questions)
		#
		# print(answers)

	@staticmethod
	def print_ascii_art() -> None:
		art1 = r"""
 ________  ________  ___       __   ________   ___       ________  ________  ________  ________
|\   ___ \|\   __  \|\  \     |\  \|\   ___  \|\  \     |\   __  \|\   __  \|\   ___ \|\   ____\
\ \  \_|\ \ \  \|\  \ \  \    \ \  \ \  \\ \  \ \  \    \ \  \|\  \ \  \|\  \ \  \_|\ \ \  \___|_
 \ \  \ \\ \ \  \\\  \ \  \  __\ \  \ \  \\ \  \ \  \    \ \  \\\  \ \   __  \ \  \ \\ \ \_____  \  
  \ \  \_\\ \ \  \\\  \ \  \|\__\_\  \ \  \\ \  \ \  \____\ \  \\\  \ \  \ \  \ \  \_\\ \|____|\  \
   \ \_______\ \_______\ \____________\ \__\\ \__\ \_______\ \_______\ \__\ \__\ \_______\____\_\  \
    \|_______|\|_______|\|____________|\|__| \|__|\|_______|\|_______|\|__|\|__|\|_______|\_________\
	                                                                                 \|_________|
		"""  # For some reason?? the bottom of the S needs to be shifted to appear correct in the terminal
		art2 = r"""
 ________  ________  ________  ________  ________   ___  ________  _______   ________
|\   __  \|\   __  \|\   ____\|\   __  \|\   ___  \|\  \|\_____  \|\  ___ \ |\   __  \
\ \  \|\  \ \  \|\  \ \  \___|\ \  \|\  \ \  \\ \  \ \  \\|___/  /\ \   __/|\ \  \|\  \
 \ \  \\\  \ \   _  _\ \  \  __\ \   __  \ \  \\ \  \ \  \   /  / /\ \  \_|/_\ \   _  _\
  \ \  \\\  \ \  \\  \\ \  \|\  \ \  \ \  \ \  \\ \  \ \  \ /  /_/__\ \  \_|\ \ \  \\  \|
   \ \_______\ \__\\ _\\ \_______\ \__\ \__\ \__\\ \__\ \__\\________\ \_______\ \__\\ _\
    \|_______|\|__|\|__|\|_______|\|__|\|__|\|__| \|__|\|__|\|_______|\|_______|\|__|\|__|
		"""
		name = r"""
   _        _                 __            
  |_) \/   | \ _     o  _|   |_  __    o __ 
  |_) /    |_/(_|\_/ | (_|   |__ | \^/ | | |
		"""
		about = r"""
  This app blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah
  blah blah blah blah blah blah blah blah blah blah blah 
		"""

		print(art1)
		time.sleep(0.5)
		print(art2)
		time.sleep(0.5)
		print(about)
		print(name)
