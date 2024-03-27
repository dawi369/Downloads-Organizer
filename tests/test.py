import unittest
import sys

# Adjusting sys.path to include the directory where the modules are located.
sys.path.insert(0, 'C:/Projects(Py)/downloads_organizer/src')

from src.main import *
from src.classes import *
from src.organizer import *


class TestAddFunction(unittest.TestCase):

	def test_download_path(self):
		downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
		DownloadsFolder = DownloadsFolderClass()
		self.assertEqual(downloads_path, DownloadsFolder.downloads_path)

	def test_adding_file(self):
		DownloadsFolder = DownloadsFolderClass()
		my_file = FileMetadata("text.exe", 1000, "21-03-24 11:11", "now ig", "txt")
		DownloadsFolder.add_file(my_file)
		self.assertEqual(DownloadsFolder.files[0], my_file)

	def test_file_metadata_name(self):
		file_path = __file__
		metadata = FileHandler.get_file_metadata(file_path)
		self.assertEqual(metadata.name, os.path.basename(__file__))



# self.assertEqual()


if __name__ == '__main__':
	unittest.main()
