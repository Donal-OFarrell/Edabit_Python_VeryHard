
#The additive persistence of an integer, n, is the number of times you 
#have to replace n with the sum of its digits until n becomes a single digit integer.

#The multiplicative persistence of an integer, n, is the number of times you 
#have to replace n with the product of its digits until n becomes a single digit integer.

#Create two functions that take an integer as an argument and:

    #Return its additive persistence.
    #Return its multiplicative persistence.


def addPersist(n):
	count = 0
	while True:
		n_str = str(n)
		if len(n_str) == 1:
			# iteration reached 
			print("It takes ", count ,"iterations to reach a single digit number.")
			break
		else: 
			 # convert to sring to take individual characters or num
			num_list=[]
			for num in n_str: # add indiviual chars n_str = str(n)to list 
				num_list += num # add chars to list
				# convert list items to integers 

			tot=0
			for number in num_list:
				tot += int(number)
			n = tot # total = n 
			count += 1 # increment counter


addPersist(1679583)
addPersist(123456)


def mulitPersist(n):
	count = 0
	while True:
		n_str = str(n)
		if len(n_str) == 1:
			# iteration reached 
			print("It takes ", count ,"iterations to reach a single digit number.")
			break
		else: 
			num_list=[]
			for num in n_str: # add indiviual chars n_str = str(n)to list 
				num_list += num # add chars to list
				# convert list items to integers 
			tot = int(num_list[0])

			num_list.pop(0)
			for number in num_list:
				tot *= int(number)
			n = tot
			count += 1

mulitPersist(77)




