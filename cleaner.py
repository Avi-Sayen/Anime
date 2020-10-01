
directory_links = "lists.txt"
with open(directory_links, "r") as file:
	url = file.read().splitlines()

def clean_lists(file_name):
	with open(file_name, "r+") as file:
		current = file.readlines()
		file.seek(0)
		for link in url:
			if link != i:
				file.write(i)
		file.truncate()
		
clean_lists("links.txt")