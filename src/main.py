from gui import GUI
from state_handler import StateHandler


def main():
	"""Setup"""
	state = StateHandler()
	GUI.print_art_with_act_dir()

	try:
		while True:
			state.home_screen()

			break



	except KeyboardInterrupt:
		print("\nExiting application... Goodbye!")
		exit(0)


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
