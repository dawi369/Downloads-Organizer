import json


class JsonHelper:
	@staticmethod
	def current_active_profile() -> str:
		current_active: list[str | None] = JsonHelper.get_active_profiles()
		if len(current_active) != 1:
			JsonHelper.set_only_default_profile_to_current()
			return "default"
		else:
			return current_active[0]

	@staticmethod
	def set_only_default_profile_to_current() -> None:
		with open("../data/profiles.json", 'r') as f:
			data = json.load(f)

		for profile in data:
			if profile['name'] != 'default':
				profile['current'] = "false"
			else:
				profile['current'] = "true"

		with open("../data/profiles.json", 'w') as f:
			json.dump(data, f, indent=4)

	@staticmethod
	def get_active_profiles() -> list[str | None]:
		active_profiles: list[str | None] = []
		with open("../data/profiles.json", 'r') as f:
			data = json.load(f)
			for profile in data:
				if profile["current"] == "true":
					active_profiles.append(profile["name"])
		return active_profiles

	@staticmethod
	def reset_and_delete_profiles() -> None:
		# Open the source file and load its contents
		with open("../data/default_state.json", 'r') as f:
			data = json.load(f)

		# Open the target file and write the contents of the source file
		with open("../data/profiles.json", 'w') as f:
			json.dump(data, f, indent=4)
