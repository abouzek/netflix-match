#!/usr/bin/env python3

import sys
from Netflix import netflix_solve

# ----
# main
# ----
user_avg_file = '/u/thunt/cs373-netflix-tests/irvin-user_avg.json'
movie_avg_file = '/u/thunt/cs373-netflix-tests/irvin-movie_avg.json'
probe_ratings_file = '/u/thunt/cs373-netflix-tests/irvin-probe_ratings.txt'
netflix_solve(sys.stdin, sys.stdout, user_avg_file, movie_avg_file, probe_ratings_file)