import os
import shutil
from classes import *
from organizer import organize_files


# TODO check on every downloads folder update/1h time period


def main():
	"""Setup"""

	DownloadsFolder = DownloadsFolderClass()

	FileHandler.gather_files(DownloadsFolder)

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
