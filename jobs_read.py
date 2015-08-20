import urllib
import re

symbolfile = open("jobs.txt")
symbolslist = symbolfile.read()

writingfile = open("jorbs.txt","w")
writingfile.write(symbolslist)

print symbolslist.split("\n")

#Second Change made to file group since Git repository Snipets was formed.
