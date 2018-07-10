"""Restaurant rating lister.

Tasks:
	Reads the ratings in from the file
	Stores them in a dictionary
	And finally, spits out the ratings in alphabetical order by restaurant.

Hint 1: Using .items() to get a list of your dictionary entries will help with sorting.

Hint 2: Refer to the Python docs on the sorted() function if you need a reminder of how to sort.
"""

import sys

def read_ratings(filename):
	""" """
	# init empty dict
	restaurant_ratings = {}

	# build dictionary using text file
	with open(filename, 'r') as file:
		for line in file:
			cleaned_line = line.rstrip()
			resturant_and_rating = cleaned_line.split(":")
			restaurant_ratings[resturant_and_rating[0]] = int(resturant_and_rating[1])

	return restaurant_ratings


def sort_ratings(dictionary):
	""" Sort restaurant ratings by restaurant name."""
	return sorted(dictionary.items())


def print_ratings(sorted_restaurant):
	""" """
	for restaurant, rating in sorted_restaurant:
		print("{} is rated at {}.".format(restaurant, rating))


def get_new_entry(restaurant_dict):
	""" Get a new entry (restaurant name and its rating) from the user."""
	# save user's response in variables
	restaurant = input("What restaurant would you like to rate? ")
	score = input("How would you rate this restaurant (from 0 to 5)? ")

	# add new entry from user
	restaurant_dict[restaurant] = score

	# return the dictionary
	return restaurant_dict


def write_new_file(new_file_name, restaurant_dict):
	""" Take dictionary with new entry from user and save to file."""
	# open a new file to write to
	with open(new_file_name, 'w') as new_file:
		# iter through (restaurant, rating) pairs, adding each pair to the file
		for restaurant, rating in restaurant_dict.items():
			new_file.write("{}:{}\n".format(restaurant, rating))

	# confirmation
	print("New file written!")


## TESTS
#print_ratings(sort_ratings(read_ratings(sys.argv[1])))

# load file then get new entry from user
new_entries = get_new_entry(read_ratings(sys.argv[1]))

# sort the dictionary and print
print_ratings(sort_ratings(new_entries))

# make a new file with the new entry included
write_new_file("new_restaurants.txt", new_entries)
