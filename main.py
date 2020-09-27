import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import json
import requests
http = httplib2.Http()


# Generated links are saved here
file_to_write = "links.txt"
json_file = "links.json"
json_data = []
directory_links = "lists.txt"

link = "https://avi-sayen.github.io/Anime/"
send = requests.get(link)
host = send.text


# Read file and save as list to a variable 
with open(directory_links, "r") as file:
	url = file.read().splitlines()


def clean_lists(file_name):
	with open(file_name, "r+") as file:
		current = file.readlines()
		file.seek(0)
		for i in current:
				for link in url:					
					if i == link:
						i = i.replace(link, "")
				file.write(i)
						
		file.truncate
		
		
# Save the links to the specified file
def write_to_file(data):
	with open(file_to_write, "a") as file:
		file.write(data)
		file.write("\n")

def create_json():
		with open(file_to_write, "r") as url:
			file = url.read().splitlines()
		for i in file:
			data = {}
			temp = i.split("/")
			data["name"] = temp[-1]
			data["url"] = i
			json_data.append(data)
		with open(json_file, "w") as url:
			json.dump(json_data, url)
		
# This function returns False if "http" is present in hyperlink
def check_link(link):
	x = re.findall("\Ahttp", link)
	if x:
		return False
	else:
		return True
		
	
def crawl_directory(directory):
	status, response = http.request(host + directory)
	# Check for hyperlinks
	for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
		if link.has_attr('href'):
			# Check if the hyperlink contains http
			if check_link(link['href']):
				# Save to file
				write_to_file(link['href'])
			
			
			

	
def main():
	for link in url:
		print("%s%s" %(host, link))
		crawl_directory(link)
		create_json()


main()
