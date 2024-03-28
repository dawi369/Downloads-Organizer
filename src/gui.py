import time
import inquirer
from organizer import JsonHelper


class GUI:
	def __init__(self):
		GUI.print_ascii_art()

		self.active_profile = JsonHelper.current_active_profile()

		print(f"Active directory profile: {self.active_profile}\n")

		questions = [
			inquirer.List('home_command',
			              message="Would you like to: ",
			              choices=['View hierarchy of active directory profile',
			                       'Change directory profile',
			                       'Set up active profile directories',
			                       'Set up and organize files for active profile',
			                       'Settings'],
			              ),
		]
		self.home_screen_answer = inquirer.prompt(questions)

		#print(self.home_screen_answer)

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
		about = (
			"Here, you can edit how you would like your downloads folder customized (Option 1). "
			"To mkdir the directories currently set in the active profile, use (Option 2). "
			"If you want option 2 and you downloads folder organized as specified in the profile, use (Option 3). "
			"Or more indepth settings, use (Option 4).\n"
			"Thank you for using my app! I highly appreciate any github issues or pull request!"
		)

		print(art1)
		time.sleep(0.5)
		print(art2)
		time.sleep(0.5)
		print(name)
		time.sleep(0.5)
		print(about)
		time.sleep(0.2)
