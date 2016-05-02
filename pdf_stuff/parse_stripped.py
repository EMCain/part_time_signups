import re

#  change + to * to allow for a single house being named

f = open("fileout.txt", "r")
fulltext = f.read() # eventually process out irrelevant parts of file
f.close()
out_dict = {}
vals = re.split('\n[\w,\s]+\w:', fulltext)[1:] # 0 index will be before first occurance
print "vals are", vals
keys = re.findall('\n[\w,?\s]+\w:', fulltext)
print "keys are", keys

for i in range(len(keys)):
	vals_array = re.split('[\n]+', vals[i])[1:] # first value is empty string
	ages = ['adults', 'youth', 'children']
	inner_dict = {'adults': [], 'youth': [], 'children': []}
	
	counter = 0 
	for val in vals_array:
		if counter == 3:
			counter = 0
		inner_dict[ages[counter]].append(val)
		counter +=1
	out_dict[keys[i].split("\n")[-1]] =  inner_dict # splitting on \n avoids a bunch of junk before the house names

for key in out_dict:
	print "------------------"
	print "key is", key
	print "value is", out_dict[key]
	print "~~~~~~~~~~~~~~~~~~"
# next step: filter stuff like "day use" and "additional meals" out


print "bye!"	