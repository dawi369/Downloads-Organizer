import unittest
import os
from pathlib import Path
from src import *


class TestAddFunction(unittest.TestCase):

	def test_download_path(self):
		downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
		DownloadsFolder = DownloadsFolderClass()
		self.assertEqual(downloads_path, DownloadsFolder.downloads_path)

	def test_adding_file(self):
		DownloadsFolder = DownloadsFolderClass()
		my_file = FileMetadata("text.exe", 1000, "21-03-24 11:11", "now ig", "txt", Path("some path"))
		DownloadsFolder.add_file(my_file)
		self.assertEqual(DownloadsFolder.files[0], my_file)

	def test_file_metadata_name(self):
		file_path = __file__
		metadata = FileHandler.get_file_metadata(file_path)
		self.assertEqual(metadata.name, os.path.basename(__file__))

	def test_check_for_directory(self):
		DownloadsFolder = DownloadsFolderClass()
		FileHandler.gather_files(DownloadsFolder)
		my_dir = "To_Review"
		my_file_type = ""

		# Create a list of tuples containing the name and file type of each FileMetadata object
		file_metadata_list = [(file.name, file.file_type) for file in DownloadsFolder.files]

		# Check if a tuple containing the specific name and file type is in the list
		self.assertIn((my_dir, my_file_type), file_metadata_list)


# self.assertEqual()


if __name__ == '__main__':
	unittest.main()
