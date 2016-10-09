import Integrate_modul as integr

def tabulate_function(fun, x):
	print("Tabulate_function work:)")
	y = []
	for coord in x:
		y.append(fun(coord))
	return y

def tabulate_integral(p, y):
	print("Tabulate_integral work:)")
	U = []
	for y_i in y:
		U.append(integr.integrate(p,1, y_i))
	return U
