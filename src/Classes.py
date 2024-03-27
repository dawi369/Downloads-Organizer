import os
from dataclasses import dataclass, field


@dataclass
class FileMetadata:
	name: str  # include extension in name?
	size_kb: int
	creation_date: str  # maybe last edited
	file_type: str


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

	def list_files(self) -> None:
		"""Prints a summary of all files in the folder."""
		for file in self.files:
			print(f"{file.name}, {file.size_kb} kilobytes, Created on {file.creation_date}, Type: {file.file_type}")

	def find_file(self, name: str) -> FileMetadata | None:
		"""Finds and returns a file by name."""
		for file in self.files:
			if file.name == name:
				return file
		return None
