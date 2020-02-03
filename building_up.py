#You are given an input list of strings, ordered by ascending length.

# Write a function that returns True if, for each pair of consecutive strings, 
# the second string can be formed from the first by adding a single letter either at 
# the beginning or end.


def can_build(ll):
	ll_dup = ll.copy() # copy list
	
	ll_dup.reverse() # reverse list
	

	
	for i in range(0,len(ll)):
		word_1=ll_dup[0] # isolate first word (longest) 
		print(word_1)
		ll_dup.pop(0) # pop from list 
		print(ll_dup)
		
		for word in ll_dup:

			falsehood = 0

			if word_1[0:-1] == word or word_1[1:] == word: # if the start or the end of the longest string equals next String, ie one character change - True
				pass  # do nothing 
			else:
				falsehood += 1
				if falsehood > 0:
					break 
					return False # otherwise false 
	if falsehood == 0: # if there are no false instances - return True 
		return True

print(can_build(['a','at','ate','late','plate','plates']))