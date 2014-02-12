#!/usr/bin/env python3

import math, json

def netflix_solve(r, w):
	"""
	netflix_solve
	r is a reader, w is a writer

	loads caches, predicts ratings, calcs RMSE, and prints results
	"""
	with open('/u/thunt/cs373-netflix-tests/irvin-user_avg.json') as user_avg_file, open('/u/thunt/cs373-netflix-tests/irvin-movie_avg.json') as movie_avg_file, open('/u/thunt/cs373-netflix-tests/timsim-probe_ans.json') as probe_ratings_file:
		user_avgs, movie_avgs, probe_ratings = json.load(user_avg_file), json.load(movie_avg_file), json.load(probe_ratings_file)
	a, p = [], []
	for line in r:
		if ':' in line:
			movie_id = int(line[:-2])
			netflix_print(w, line[:-1])
		else:
			customer_id = int(line)
			rating = netflix_eval(user_avgs, movie_avgs, movie_id, customer_id)
			p.append(rating)
			a.append(probe_ratings[str(movie_id)][str(customer_id)])
			netflix_print(w, rating)
	netflix_print(w, "\nRMSE:" + str(netflix_rmse(a, p)))

def netflix_eval(user_avgs, movie_avgs, movie_id, customer_id):
	"""
	netflix_eval
	user_avgs is a dictionary of (customer id: customer avg rating for all movies)
	movie_avgs is a dictionary of (movie id: movie avg rating for all users)
	movie_id is a movie id, customer_id is a customer id

	returns the predicted rating for a particular movie id and customer id
	"""
	user_avg = user_avgs[str(customer_id)] - 3.6
	movie_avg = movie_avgs[str(movie_id)] - 3.6
	return 3.6 + user_avg + movie_avg # 3.6 is (avg overall rating - .1)

def netflix_print(w, num):
	"""
	netflix_print
	w is a writer, num is the object to be printed

	prints num and a newline
	"""
	w.write(str(num) + "\n")

def netflix_rmse(a, p) :
    """
	netflix_rmse
	a and p are iterables

	returns the RMSE between a and p
	"""
    v = sum(map(lambda x, y : (x - y) ** 2, a, p), 0.0)
    return math.sqrt(v / len(a))