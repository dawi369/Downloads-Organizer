import unittest

# from ..src.main import *
from ..src.classes import *


# from ..src.file_classifier import *
# from ..src.organizer import *


class TestAddFunction(unittest.TestCase):

	def test_download_path(self):
		downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
		DownloadsFolder = DownloadsFolderClass()
		self.assertEqual(downloads_path, DownloadsFolder.downloads_path)

	def test_adding_file(self):
		DownloadsFolder = DownloadsFolderClass()
		my_file = FileMetadata("text.exe", 1000, "21-03-24 11:11", "txt")
		DownloadsFolder.add_file(my_file)
		self.assertEqual(DownloadsFolder.files[0], my_file)


if __name__ == '__main__':
	unittest.main()
