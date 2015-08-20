import webbrowser
import urllib
import re

index = []
temp = []

a = ['a','b','c','d','e','f','g','h','i','j','k']
b = ['1','2','3','4','5','6','7','8','9','10','11']


i = 0
while i < len(a):
	temp = []
	temp.append(a[i]) 
	temp.append(b[i])
	index.append(temp)
	print temp
	print index
	i+=1
	
#temp.append(a[0])
print temp[0]

index.append(temp[0])

print temp
print index

