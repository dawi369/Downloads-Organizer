from src import DownloadsFolderClass, FileHandler


# TODO check on every downloads folder update/1h time period


def main():
	"""Setup"""
	df = DownloadsFolderClass()
	fh = FileHandler()
	fh.gather_files(df)


	fh.make_missing_dirs(df)


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
