from dl_folder import DownloadsFolderClass
from file_handler import FileHandler
from gui import GUI
from organizer import JsonHelper


def main():
	"""Setup"""
	gui = GUI()
	df = DownloadsFolderClass()
	fh = FileHandler(gui)
	fh.gather_files(df)


	fh.make_missing_dirs(df)
	fh.update_files(df)



if __name__ == "__main__":
	main()

"""
Downloads/
    To_Review/
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
