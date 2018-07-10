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
	restaurant = input("What restaurant would you like to rate? ")
	score = input("How would you rate this restaurant (from 0 to 5? ")

	# add new entry from user
	restaurant_dict[restaurant] = score

	# return the dictionary
	return restaurant_dict


## TESTS
print_ratings(sort_ratings(read_ratings(sys.argv[1])))

#get_new_entry(read_ratings(sys.argv[1])