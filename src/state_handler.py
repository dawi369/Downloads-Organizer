import inquirer
from dl_folder import DownloadsFolderClass
from file_handler import FileHandler
from organizer import JsonHelper
from gui import GUI


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

	def view_hierarchy_of_ADP(self):
		print(f"Temp: {self.active_profile}")

	def edit_directory_profile(self):
		pass

	def set_up_directories_according_to_active(self):
		self.fh.make_missing_dirs(self.df)
		self.fh.update_files(self.df)
		print("Directories successfully created!")
		self.home_screen()
