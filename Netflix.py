#!/usr/bin/env python3

import math, json

def netflix_load_cache(user_avg_file, movie_avg_file):
	with open(user_avg_file) as ua, open (movie_avg_file) as ma:
		return json.load(ua), json.load(ma)

def netflix_solve(r, w, user_avg_file, movie_avg_file, probe_ratings_file):
	user_avgs, movie_avgs = netflix_load_cache(user_avg_file, movie_avg_file)

	a = []
	p = []
	movie_id = 0
	customer_id = 0
	# Make our predictions for customers
	for line in r:
		if ':' in line:
			movie_id = int(line[:-2])
			netflix_print(w, line[:-1])
		else:
			customer_id = int(line)
			rating = netflix_eval(user_avgs, movie_avgs, movie_id, customer_id)
			p.append(rating)
			netflix_print(w, rating)

	# Gather Netflix predicted ratings for comparison
	with open(probe_ratings_file) as f:
		for line in f:
			if ':' not in line:
				a.append(float(line))

	netflix_print(w, "\nRMSE:" + str(rmse(a, p)))

def netflix_eval(user_avgs, movie_avgs, movie_id, customer_id):
	user_avg = user_avgs[str(customer_id)]
	movie_avg = movie_avgs[str(movie_id)]
	# Average of all ratings = 3.7
	return (user_avg + movie_avg) / 2

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