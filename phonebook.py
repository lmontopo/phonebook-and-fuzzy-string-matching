import sys

# --------- FUNCTIONS ---------- #

def create_phonebook(phonebook_name):
	file_name = '%s' %phonebook_name + '.txt'
	pb_file = open('%s' %file_name, 'wb')
	pb_file.close()
	print 'Created a phonebook called %s' %phonebook_name

def add_entry(name, number, phonebook_name):
	file_name = '%s' %phonebook_name + '.txt'
	pb_file = open('%s' %file_name, 'ab')
	pb_file.write('%s:%s\n' %(name, number))
	pb_file.close()
	print 'added %s: %s to %s' %(name, number, phonebook_name)

def look_up(name, phonebook_name):
	file_name = '%s' %phonebook_name + '.txt'
	phonebook = create_dict(file_name)
	if name in phonebook.keys():
		print "%s's number is: %s" %(name, phonebook[name])
		return phonebook[name]
	else:
		fuzzy_match_func(name, list(phonebook.keys()))

def update(name, number, phonebook_name):
	file_name = '%s' %phonebook_name + '.txt'
	phonebook = create_dict(file_name)
	if name in phonebook.keys():
		phonebook[name] = number
	write_from_dict(phonebook, file_name)
	print "%s's new number is: %s" %(name, phonebook[name])
	

def delete(name, phonebook_name):
	file_name = '%s' %phonebook_name + '.txt'
	phonebook = create_dict(file_name)
	if name in phonebook.keys():
		del phonebook[name]
	write_from_dict(phonebook, file_name)
	print "%s's entry has been deleted from %s" %(name, phonebook_name)

def create_dict(file_name):
	phonebook = {}
	for line in open(file_name):
		line = str(line)
		colon_position = line.find(':')
		new_line_position = line.find('\n')
		read_name = line[: colon_position]
		read_number = line[colon_position + 1: new_line_position]
		phonebook.update({read_name: read_number})
	return phonebook

def write_from_dict(phonebook, file_name):
	with open(file_name, 'wb') as pb_file:
		for item in phonebook:
			pb_file.write('%s:%s\n' %(item, phonebook[item]))




# ------------- MAIN -------------- #

if __name__ == '__main__':	
	user_input = list(sys.argv)[1:]
	operator, args = user_input[0], user_input[1:]
	if operator == 'create':
		create_phonebook(*args)
	elif operator == 'add':
		add_entry(*args)
	elif operator == 'lookup':
		look_up(*args)
	elif operator == 'update':
		update(*args)
	elif operator == 'remove':
		delete(*args)
	else:
		pass


