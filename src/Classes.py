import os
from dataclasses import dataclass, field


@dataclass
class FileMetadata:
	name: str
	sizeKB: int
	creation_date: str
	file_type: str


@dataclass
class DownloadsFolderClass:
	_instance = None
	files: list[FileMetadata] = field(default_factory=list)
	downloads_path = None

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
			print(f"{file.name}, {file.sizeKB} kilobytes, Created on {file.creation_date}, Type: {file.file_type}")

	def find_file(self, name: str) -> FileMetadata | None:
		"""Finds and returns a file by name."""
		for file in self.files:
			if file.name == name:
				return file
		return None
