# Write a function that moves all the zeroes to the end of a list. 
# Do this without returning a copy of the input list.


def zeroes_to_end(ll):
	zero_counter = 0
	
	for n in ll:
		if n == 0:
			zero_counter += 1 # number of zeroes in list

	while 0 in ll:
		ll.remove(0) # get rid of zeroes from list 

	for i in range(0,zero_counter):
		ll.append(0) # add the correct amount onto the end of the list

	return ll 

print(zeroes_to_end([1,2,0,0,4,0,5]))
