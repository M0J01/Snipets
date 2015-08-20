import webbrowser
import urllib
import re

# urls = ["http://google.com","http://nytimes.com","http://CNN.com"]
# i = 0
# regex = '<title>(.+?)</title>'
# pattern = re.compile(regex)


# while i < len(urls):
	# htmlfile = urllib.urlopen(urls[i])
	# htmltext = htmlfile.read()
	# titles = re.findall(pattern,htmltext)
	
	# print titles
#	i+=1

#making changes like a fiddler	
	
url1="http://";
url2 = "google.com"
url = url1 + url2
webbrowser.open(url);

