#!/usr/bin/env python3

import math

def netflix_solve(r, w):
	a = []
	p = []
	movie_id = 0
	customer_id = 0
	# G
	for line in r:
		if ':' in line:
			movie_id = int(line[:-2])
			netflix_print(w, line[:-1])
		else:
			customer_id = int(line)
			rating = netflix_eval(movie_id, customer_id)
			p.append(rating)
			netflix_print(w, rating)

	# Gather Netflix predicted ratings for comparison
	#probe_ratings = '/u/thunt/cs373-netflix-tests/irvin-probe_ratings.txt'
	probe_ratings = './TestRatings.in'
	with open(probe_ratings) as f:
		for line in f:
			if ':' not in line:
				a.append(float(line))

	netflix_print(w, "RMSE:" + str(rmse(a, p)))

def netflix_eval(movie_id, customer_id):
	return 3

def netflix_print(w, num):
	w.write(str(num) + "\n")

def rmse(a, p) :
    """
    O(1) in space
    O(n) in time
    """
    s = len(a)
    v = sum(map(lambda x, y : (x - y) ** 2, a, p), 0.0)
    return math.sqrt(v / s)