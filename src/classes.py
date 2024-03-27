import os
import time
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class FileMetadata:
	name: str
	size_kb: int
	creation_date: str
	last_edited: str
	file_type: str
	full_path: Path


@dataclass
class DownloadsFolderClass:
	"""
	This is a Singleton class, the custom __new__ method ensures there will only ever be one instance of this class,
	as well as assigning the path of the downloads folder for the current user
	"""
	_instance = None
	downloads_path = None
	files: list[FileMetadata] = field(default_factory=list)

	def __new__(cls, *args, **kwargs):
		downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
		if not cls._instance:
			cls.downloads_path = downloads_path
			cls._instance = super(DownloadsFolderClass, cls).__new__(cls, *args, **kwargs)
		return cls._instance

	def add_file(self, file_metadata: FileMetadata) -> None:
		"""Adds a new file to the folder."""
		self.files.append(file_metadata)

	def list_files_big(self) -> None:
		"""Prints a summary of all files in the folder."""
		for file in self.files:
			print(
				f"{file.name}, {file.size_kb} kilobytes, Created on {file.creation_date}, Last modified on {file.last_edited}, Type: {file.file_type}, Located at {file.full_path}")

	def list_files_small(self) -> None:
		"""Prints a summary of all files in the folder."""
		for file in self.files:
			print(f"{file.name}")

	def list_directories(self) -> None:
		"""Prints a summary of all directories in the folder."""
		for file in self.files:
			if file.file_type == "":
				print(f"{file.name}")

	def find_file(self, name: str) -> FileMetadata | None:
		"""Finds and returns a file by name."""
		for file in self.files:
			if file.name == name:
				return file
		return None


# TODO function to run a check for every subdirectory, return the metadata of files in the wrong place

class FileHandler:

	def __init__(self):
		self.core_dirs: dict[str, list[str]] = {
			"To_Review": [""],
			"Programming": ["Python", "Rust", "Go", "Mojo", "C", "C++"],
			"Documents": ["PDFs", "Word_Documents", "Spreadsheets"],
			"Media": ["Images", "Videos", "Music"],
			"Software": ["Executables", "Installation_Packages"],
			"Archives": ["ZIP", "RAR"]
		}

	def make_missing_dirs(self, main: DownloadsFolderClass) -> None:
		# Look through downloads and make the core dirs, when cycle over them and use impl subdir

		file_metadata_list = [(file.name, file.file_type) for file in main.files]
		for core_dir in self.core_dirs.keys():
			dir_path = os.path.join(main.downloads_path, core_dir)
			if (core_dir, "") not in file_metadata_list:
				try:
					os.mkdir(dir_path)
					print(f"Directory created: {core_dir} in {dir_path}")
					try:
						self.implement_subdirs(dir_path)
					except OSError as e:
						print(f"Error implementing sub directories for {dir_path}: {e}")
				except OSError as e:
					print(f"Error creating directory {dir_path}: {e}")
			else:
				try:
					self.implement_subdirs(dir_path)
				except OSError as e:
					print(f"Error implementing sub directories for {dir_path}: {e}")

	def implement_subdirs(self, path_to_core_dir: str) -> None:
		for core_dir in self.core_dirs.keys():
			if core_dir in path_to_core_dir and core_dir != "To_Review":
				items = os.listdir(path_to_core_dir)
				subdirs = [item for item in items if os.path.isdir(os.path.join(path_to_core_dir, item))]
				self.impl_subdir_helper(core_dir, subdirs, path_to_core_dir)

				break

	def impl_subdir_helper(self, core_dir, subdirs, path_to_core_dir) -> None:
		for subdir_to_implement in self.core_dirs[core_dir]:
			if subdir_to_implement not in subdirs:
				subdir_path = os.path.join(path_to_core_dir, subdir_to_implement)
				try:
					os.mkdir(subdir_path)
					print(f"Sub Directory created: {subdir_to_implement} in {subdir_path}")
				except OSError as e:
					print(f"Error creating directory {subdir_to_implement}: {e}")

	@staticmethod
	def get_file_metadata(file_path: str) -> FileMetadata:
		stat_info = os.stat(file_path)
		file_name = os.path.basename(file_path)
		file_sizeKB = stat_info.st_size // 1024  # size in kilobytes
		creation_date = time.ctime(stat_info.st_ctime)
		modification_date = time.ctime(stat_info.st_mtime)
		file_type = os.path.splitext(file_path)[1][1:]  # get file extension without the dot
		full_path: Path = Path(file_path).resolve()

		return FileMetadata(file_name, file_sizeKB, creation_date, modification_date, file_type, full_path)

	@staticmethod
	def gather_files(main: DownloadsFolderClass) -> None:
		for entry in os.listdir(main.downloads_path):
			entry_path = os.path.join(main.downloads_path, entry)
			entry_metadata = FileHandler.get_file_metadata(entry_path)
			main.add_file(entry_metadata)

# C:\Users\Hocke\Downloads
