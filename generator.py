import json, os, optparse, wand

def get_sizes(cat):
	current_directory = os.path.dirname(os.path.realpath(__file__))
	with open(os.path.join(current_directory, "icon_sets.json")) as f:
		json_as_string = f.read()
		file_sizes_tree = json.loads(json_as_string)
	size_cats = []
	if cat in file_sizes_tree.bundles:
		for i in file_sizes_tree.bundles[cat]:
			size_cats.append(i)
	else if cat in file_sizes_tree and cat != 'bundles':
		size_cats = [cat]
	else:
		print "No defined category for [[" + cat + "]]"
		# throw error: no defined category

	sizes = {
		"required":[],
		"optional":[]
	}

	for i in size_cats:
		for device in i:
			sizes.required = sizes.required + device.required
			sizes.optional = sizes.optional + device.optional

	sizes.required = set(sizes.required)
	sizes.optional = set(sizes.optional)

	for i in sizes.required:
		if i in sizes.optional:
			sizes.optional.remove(i)

	return sizes

def resize_image_for_cat(sizes, img_src):
	try:
		with wand.image.Image(filename=img_src) as img:
			if img.size[0] != img.size[1]:
				print "Warning - x and y dimensions of image not equal!"
			for i in sizes:

	else:
		print "Error processing image!"
		# throw error: error processing image

if __name__ == "__main__":
	parser = optparse.OptionParser()
	# options
	# --in-file
	# --out-directory
	# --resize-algorithm
	# --device-family
	# defulat: do everything