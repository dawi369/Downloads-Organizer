import os
import shutil
from Classes import *
from file_classifier import classify_file
from organizer import organize_files


# tod0 check on every downloads folder update/1h time period


def main():
	"""Setup"""

	DownloadsFolder = DownloadsFolderClass()
	my_file = FileMetadata("text.txt", 1000, "21-03-24 11:11", "txt")
	DownloadsFolder.add_file(my_file)
	DownloadsFolder.list_files()





if __name__ == "__main__":
	main()

"""
Downloads/
    To_Review/
        Misc/
    Programming/
        Python/
        Rust/
        Go/
        Mojo/
        C/
        C++/
    Documents/
        PDFs/
        Word Documents/
        Spreadsheets/
    Media/
        Images/
        Videos/
        Music/
    Software/
        Executables/
        Installation Packages/
    Archives/
        ZIP/
        RAR/
"""
