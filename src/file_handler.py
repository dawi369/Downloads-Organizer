import json
import os
import time
from pathlib import Path
from dl_folder import DownloadsFolderClass, FileMetadata
from organizer import JsonHelper


class FileHandler:

	def __init__(self):
		with open("../data/profiles.json", 'r') as f:
			data = json.load(f)
			for profile in data:
				if profile["name"] == JsonHelper.current_active_profile():
					self.core_dirs: dict[str, list[str | None]] = profile["Downloads"]

	def make_missing_dirs(self, main: DownloadsFolderClass) -> None:
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

	@staticmethod
	def update_files(main: DownloadsFolderClass) -> None:
		for entry in os.listdir(main.downloads_path):
			entry_path = os.path.join(main.downloads_path, entry)
			entry_metadata = FileHandler.get_file_metadata(entry_path)
			if entry_metadata not in main.files:
				main.add_file(entry_metadata)
