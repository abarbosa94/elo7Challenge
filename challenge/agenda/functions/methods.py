import sys
class Methods():

	def calculate_lower_size(self, contacts):
		lowest_size = -1;
		lowest_name = '';
		for people in contacts:
			tmp = people.replace(" ","")
			current_size = len(tmp)
			if(lowest_size == -1):
				lowest_size = current_size
				lowest_name = people;
			else:
				if lowest_size>current_size:
					lowest_size = current_size
					lowest_name = people;
		return (lowest_size, str(lowest_name))

	def calculate_highest_size(self, contacts):
		highest_size = sys.maxint; 
		highest_name = '';
		for people in contacts:
			tmp = people.replace(" ","")
			current_size = len(tmp)
			if(highest_size == sys.maxint):
				highest_size = current_size
				highest_name = people;
			else:
				if highest_size<current_size:
					highest_size = current_size
					highest_name = people;
		return (highest_size, str(highest_name))

	def calculate_size_avg(self, contacts):
		#the average name is by people so the division should be by the total number of people
		total = 0.;
		for people in contacts:
			total = total + len(people.replace(" ",""))
		return total/len(contacts)

	def pick_first_names(self, names):
		sep = ' '
		first_names = []
		for name in names:
			name = name.split(sep, 1)[0]
			first_names.append(name)
		return first_names
