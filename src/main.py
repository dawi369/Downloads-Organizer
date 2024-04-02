from gui import GUI
from state_handler import StateHandler


# cannot go deeper than 1 subdir from cores
def main():
	"""Setup"""
	state: StateHandler = StateHandler()
	GUI.print_art_with_act_dir()

	try:

		state.home_screen()

	except KeyboardInterrupt:
		print("\nExiting application... Goodbye!")
		exit(0)


if __name__ == "__main__":
	main()
