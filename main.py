from file_classifier import classify_file
from organizer import organize_files

#TODO check on every downloads folder update/1h time period

def main():
    # Assume we get a list of files from the Downloads folder
    files_to_organize = ["some_file.pdf", "another_file.mp4", ...]
    classified_files = classify_file(files_to_organize)
    organize_files(classified_files)

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