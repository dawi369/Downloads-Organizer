import time
from organizer import JsonHelper


class GUI:

	@staticmethod
	def print_art_with_act_dir() -> None:
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
		print(f"\nActive directory profile: {JsonHelper.current_active_profile()}")
