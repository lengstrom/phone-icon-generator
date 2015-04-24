import json, os, optparse

current_directory = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(current_directory, "icon_sets.json")) as f:
	json_as_string = f.read()
	file_sizes = json.loads(json_as_string)

