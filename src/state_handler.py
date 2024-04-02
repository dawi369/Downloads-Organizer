import inquirer
import os
import json
from dl_folder import DownloadsFolderClass
from file_handler import FileHandler
from organizer import JsonHelper


class StateHandler:

	def __init__(self):
		self.home_questions = [
			inquirer.List('home_command',
			              message="-> Would you like to",
			              choices=['1. View hierarchy of active directory profile',
			                       '2. Edit directory profiles',
			                       '3. Set up directories according to active profile',
			                       '4. Set up directories and organize files according to active profile',
			                       '5. Settings',
			                       '6. Exit'],
			              ),
		]

		self.df = DownloadsFolderClass()
		self.fh = FileHandler()
		self.fh.gather_files(self.df)

		self.active_profile = JsonHelper.current_active_profile()

	def home_screen(self):

		print()
		answer = inquirer.prompt(self.home_questions)
		match answer:
			case {'home_command': '1. View hierarchy of active directory profile'}:
				self.view_hierarchy_of_ADP()
			case {'home_command': '2. Edit directory profiles'}:
				print(2)
			case {'home_command': '3. Set up directories according to active profile'}:
				self.set_up_directories_according_to_active()
			case {'home_command': '4. Set up directories and organize files according to active profile'}:
				print(4)
			case {'home_command': '5. Settings'}:
				print(5)
			case {'home_command': '6. Exit'}:
				print("\nExiting application... Goodbye!")
				exit(0)

	# 1
	def view_hierarchy_of_ADP(self) -> None:
		# Load the profiles from the JSON file
		with open("../data/profiles.json", 'r') as f:
			profiles = json.load(f)

		# Find the profile with the given name
		for profile in profiles:
			if profile['name'] == self.active_profile:
				downloads = profile['Downloads']
				break
		else:
			print(f"No profile found with the name {self.active_profile}")
			return

		# Helper for 1
		def print_directory(name, directory, indent=0):
			match indent:
				case 0:
					print('  ' * indent + name + '/')
				case _ if indent >= 1:
					print('|' + "--"* indent + name + '/')






			if isinstance(directory, list):
				for item in directory:
					print('|' + "-- "*(indent + 1) + item)
			else:
				for subdirectory in directory:
					print_directory(subdirectory, directory[subdirectory], indent + 1)

		# Print the Downloads directory
		print_directory('Downloads', downloads)

	# 2
	def edit_directory_profile(self) -> None:
		pass

	# 3
	def set_up_directories_according_to_active(self) -> None:
		self.fh.make_missing_dirs(self.df)
		self.fh.update_files(self.df)
		#os.system('cls' if os.name == 'nt' else 'clear')
		print("Directories successfully created!")
		self.home_screen()
