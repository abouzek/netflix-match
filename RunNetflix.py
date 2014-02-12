#!/usr/bin/env python3

import sys
from Netflix import netflix_solve

# ----
# main
# ----
with open('/u/thunt/cs373-netflix-tests/irvin-user_avg.json') as user_avgs, open('/u/thunt/cs373-netflix-tests/irvin-movie_avg.json') as movie_avgs, open('/u/thunt/cs373-netflix-tests/timsim-probe_ans.json') as probe_ratings:
	user_avg_str, movie_avg_str, probe_ratings_str = user_avgs.read(), movie_avgs.read(), probe_ratings.read()
netflix_solve(sys.stdin, sys.stdout, user_avg_str, movie_avg_str, probe_ratings_str)