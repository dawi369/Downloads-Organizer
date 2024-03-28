import inquirer
from organizer import JsonHelper


class StateHandler:
	def __init__(self):
		self.active_profile = JsonHelper.current_active_profile()

