#!/usr/bin/env python3

import io, unittest

from Netflix import netflix_eval, netflix_solve, netflix_print, netflix_rmse

class TestNetflix(unittest.TestCase):
	def test_netflix_print_1(self):
		w = io.StringIO()
		netflix_print(w, "10:")
		self.assertTrue(w.getvalue() == "10:\n")
	def test_netflix_print_2(self):
		w = io.StringIO()
		netflix_print(w, 1)
		self.assertTrue(w.getvalue() == "1\n")
	def test_netflix_print_3(self):
		w = io.StringIO()
		netflix_print(w, "")
		self.assertTrue(w.getvalue() == "\n")
	def test_netflix_rmse1(self):
		a = [1, 1, 1]
		p = [1, 1, 1]
		self.assertTrue(netflix_rmse(a, p) == 0)
	def test_netflix_rmse2(self):
		a = [1, 1, 1]
		p = [2, 2, 2]
		self.assertTrue(netflix_rmse(a, p) == 1)
	def test_netflix_rmse3(self):
		a = [1, 2, 3]
		p = [1.5, 2.5, 2.5]
		self.assertTrue(netflix_rmse(a, p) == 0.5)
	def test_netflix_eval_1(self):
		user_avgs = {'111':3.6}
		movie_avgs = {'123456':3.6}
		self.assertTrue(netflix_eval(user_avgs, movie_avgs, '123456', '111') == 3.6)
	def test_netflix_eval_2(self):
		user_avgs = {'123456':3.5}
		movie_avgs = {'123456':3.5}
		self.assertTrue(netflix_eval(user_avgs, movie_avgs, '123456', '123456') == 3.4)
	def test_netflix_eval_3(self):
		user_avgs = {'12345678':3.0}
		movie_avgs = {'12345678':3.5}
		self.assertTrue(netflix_eval(user_avgs, movie_avgs, '12345678', '12345678') == 2.9)
	def test_netflix_solve_1(self):
		r = io.StringIO("1:\n30878")
		w = io.StringIO()
		netflix_solve(r, w)
		self.assertTrue(w.getvalue() == "1:\n3.7831603124995574\n\nRMSE:0.21683968750044258\n")
	def test_netflix_solve_2(self):
		r = io.StringIO("1:\n30878\n10:\n1952305")
		w = io.StringIO()
		netflix_solve(r, w)
		self.assertTrue(w.getvalue() == "1:\n3.7831603124995574\n10:\n2.990063550906924\n\nRMSE:0.15348971153772634\n")
	def test_netflix_solve_3(self):
		r = io.StringIO("10014:\n1626179\n10:\n1952305")
		w = io.StringIO()
		netflix_solve(r, w)
		self.assertTrue(w.getvalue() == "10014:\n3.126969638117434\n10:\n2.990063550906924\n\nRMSE:0.7969188472671227\n")
# ----
# main
# ----

print ("TestNetflix.py")
unittest.main()
print("Done.")