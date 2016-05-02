nums = range(0, 50)


ages = ['adults', 'youth', 'children']
dict = {'adults': [], 'youth': [], 'children': []}



counter = 0
for i in range(50):
	if counter == 3:
		counter = 0
	dict[ages[counter]].append(i)
	counter += 1
	
print dict