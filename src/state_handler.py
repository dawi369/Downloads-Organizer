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
			                       '2. Change to a different directory profile',
			                       '3. Edit directory profiles',
			                       '4. Set up directories according to active profile',
			                       '5. Set up directories and organize files according to active profile',
			                       '6. Settings',
			                       '7. Exit'],
			              ),
		]

		self.df: DownloadsFolderClass = DownloadsFolderClass()
		self.fh: FileHandler = FileHandler()
		self.fh.gather_files_from_dl_folder(self.df)

		self.active_profile: str = JsonHelper.current_active_profile()

	def home_screen(self) -> None:

		print()
		print(f"\nActive directory profile: {self.active_profile}\n")
		print()
		answer = inquirer.prompt(self.home_questions)
		match answer:
			case {'home_command': '1. View hierarchy of active directory profile'}:
				self.view_hierarchy_of_ADP()
			case {'home_command': '2. Change to a different directory profile'}:
				self.change_to_different_profile()
			case {'home_command': '3. Edit directory profiles'}:
				self.edit_directory_profile()
			case {'home_command': '4. Set up directories according to active profile'}:
				self.set_up_directories_according_to_active()
			case {'home_command': '5. Set up directories and organize files according to active profile'}:
				self.set_up_and_organize()
			case {'home_command': '6. Settings'}:
				self.settings()
			case {'home_command': '7. Exit'}:
				print("\nExiting application... Goodbye!")
				exit(0)

	# Make sure to update dl_folder after changes

	# 1
	def view_hierarchy_of_ADP(self) -> None:
		with open("../data/profiles.json", 'r') as f:
			profiles = json.load(f)

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
				case 1:
					print('|' + "--" * indent + name + '/')
				case _ if indent > 1:
					print('|  ' + " ^- " * (indent - 1) + name + '/')

			if isinstance(directory, list):
				for item in directory:
					print('   ' + '|' + "--" * (indent + 1) + item)
			else:
				for subdirectory in directory:
					print_directory(subdirectory, directory[subdirectory], indent + 1)

		os.system('cls' if os.name == 'nt' else 'clear')
		print_directory('Downloads', downloads)
		self.home_screen()

	# 2
	def change_to_different_profile(self) -> None:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("change_to_different_profile not yet implemented")
		self.home_screen()

	# 3
	def edit_directory_profile(self) -> None:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("edit_directory_profile not yet implemented")
		self.home_screen()

	# 4
	def set_up_directories_according_to_active(self) -> None:
		os.system('cls' if os.name == 'nt' else 'clear')
		self.fh.make_missing_dirs(self.df)
		self.fh.update_files_in_dl_folder(self.df)
		print("Directories successfully created!")
		self.home_screen()

	# 5
	def set_up_and_organize(self) -> None:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("set_up_and_organize not yet implemented")
		self.home_screen()

	# 6
	def settings(self) -> None:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("settings not yet implemented")
		self.home_screen()
