import json

class JsonHelper:
	@staticmethod
	def current_active_profile() -> None:
		current_active = JsonHelper.get_active_profiles()
		print(len(current_active))
		if len(current_active) != 1:
			JsonHelper.set_only_default_profile_to_current()



	@staticmethod
	def set_only_default_profile_to_current() -> None:
		# Step 1: Read the JSON file
		with open("profiles.json", 'r') as f:
			data = json.load(f)
		# Step 2: Update the 'current' property
		for profile in data:
			if profile['name'] != 'default':
				profile['current'] = "false"
		# Step 3: Write the updated objects back to the file
		with open("profiles.json", 'w') as f:
			json.dump(data, f, indent=4)



	@staticmethod
	def get_active_profiles() -> list:
		active_profiles = []
		with open("profiles.json", 'r') as f:
			data = json.load(f)
			for profile in data:
				if profile["current"] == "true":
					active_profiles.append(profile["name"])
		return active_profiles

	@staticmethod #TODO test this
	def reset_and_delete_profiles() -> None:
		# Open the source file and load its contents
		with open("default_state.json", 'r') as f:
			data = json.load(f)

		# Open the target file and write the contents of the source file
		with open("profiles.json", 'w') as f:
			json.dump(data, f)



