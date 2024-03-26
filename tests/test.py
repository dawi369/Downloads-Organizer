import unittest
from src.main import *
from src.Classes import *
from src.file_classifier import *
from src.organizer import *




class TestAddFunction(unittest.TestCase):

	def test(self):
		downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
		DownloadsFolder = DownloadsFolderClass()
		self.assertEquals(downloads_path, DownloadsFolder.downloads_path)

if __name__ == '__main__':
	unittest.main()
