import re

Test_Script = 'Woot'

tq1 = [2,['name','Name','NAME']]
tq2 = [3,['face','Face','FACE']]

tQ = []
tQ.append(tq1)
tQ.append(tq2)

dQ_limit = 0
dQ_Count = 0

#pattern = ' '
#patternz = re.compile(pattern)

for t in tQ:
	dQ_Count = 0
	dQ_limit = t[0]
	for word in t[1]:
		match = re.findall(word,Test_Script)
		dQ_Count += len(match)
	if dQ_Count >= dQ_limit:
		print "DQ'ed"
	else:
		print "Pass"