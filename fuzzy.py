def fuzzy_match_simple(name1, name2): 
	distance = 0 
	name2_copy = name2  
	name1_copy = name1
	
	while len(name1_copy) > 0 and len(name2_copy) > 0: 
		
		if name2_copy[0] == name1_copy[0]: #checks if first letter equal
			name2_copy, name1_copy = name2_copy[1:], name1_copy[1:]
		
		elif (name1_copy[1:] == name2_copy): #check if name1_copy has additional char
			distance += 1 
			name1_copy = name1_copy[1:]
			break
		
		elif (name1_copy == name2_copy[1:]): #checks if name2_copy has additional char
			distance += 1
			name2_copy = name2_copy[1:]
			break

		elif (name2_copy[1:]) == name1_copy[1:]: #checks for substitution
			distance += 1
			name2_copy, name1_copy = '', ''
		
		else: #in all other cases just get rid of that letter and continue
			distance += 1
			name2_copy, name1_copy = name2_copy[1:], name1_copy[1:]	

	distance += abs(len(name2_copy) - len(name1_copy)) #then we're adding another one here
	return distance	


def list_fuzzy_match(name, my_list):
	distances = {}
	for item in my_list:
		distances[item] = fuzzy_match_simple(name, item)
	return distances

if __name__ == '__main__': 
	print fuzzy_match_simple('letta', 'leta')


