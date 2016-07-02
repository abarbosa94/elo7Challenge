import sys
class Methods():

	def calculate_lower_full_name_size(self, contacts):
		lowest_name_size = -1;
		lowest_name = '';
		for people in contacts:
			tmp = people.name.replace(" ","")
			current_size = len(tmp)
			if(lowest_name_size == -1):
				lowest_name_size = current_size
				lowest_name = people;
			else:
				if lowest_name_size>current_size:
					lowest_name_size = current_size
					lowest_name = people;
		return (lowest_name_size, str(lowest_name.name))

	def calculate_highest_full_name_size(self, contacts):
		highest_name_size = sys.maxint; #impossible to reach
		highest_name = '';
		for people in contacts:
			tmp = people.name.replace(" ","")
			current_size = len(tmp)
			if(highest_name_size == sys.maxint):
				highest_name_size = current_size
				highest_name = people;
			else:
				if highest_name_size<current_size:
					highest_name_size = current_size
					highest_name = people;
		return (highest_name_size, str(highest_name.name))

	def calculate_full_name_size_avg(self, contacts):
		#the average name is by people so the division should be by people, not the total of names
		highest_name_size = 340; #impossible to reach
		highest_name = '';
		for people in contacts:
			tmp = people.name.replace(" ","")
			current_size = len(tmp)
			if(highest_name_size == 340):
				highest_name_size = current_size
				highest_name = people;
			else:
				if highest_name_size<current_size:
					highest_name_size = current_size
					highest_name = people;
		return (highest_name_size, str(highest_name.name))