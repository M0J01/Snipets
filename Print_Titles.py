#import webbrowser
import urllib
import re

urls = ["http://google.com","http://nytimes.com","http://CNN.com"]
i = 0
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)


while i < len(urls):
	htmlfile = urllib.urlopen(urls[i])
	htmltext = htmlfile.read()
	titles = re.findall(pattern,htmltext)
	
	print titles
	i+=1

	
	
	
	# new=2

# url="http://google.com";

# webbrowser.open(url,new=new);

#Now we are going to try to a "pull" manoeuvre.

