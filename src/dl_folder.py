import os
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


# TODO function to run a check for every subdirectory, return the metadata of files in the wrong place

@dataclass
class DownloadsFolderClass:
	"""
	This is a Singleton class. The custom __new__ method ensures there will only ever be one instance of this class,
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
