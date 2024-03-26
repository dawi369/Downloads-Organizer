import os
import shutil
from file_classifier import classify_file
from organizer import organize_files
from dataclasses import dataclass


# TODO check on every downloads folder update/1h time period


@dataclass
class FileMetadata:
	name: str
	size: int
	creation_date: str
	file_type: str


def main():
	# SETUP
	home_directory = os.path.expanduser('~')
	downloads_path = os.path.join(home_directory, 'Downloads')
	dynamic_file_array: [FileMetadata] = []


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
