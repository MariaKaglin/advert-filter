import Integrate_modul as integr

def c_1(x, p, z, x_0, T, y, beta):
	c = 0
	print("C_1 calculation work:)")
	integr.integrate(p, 1, y)
	#something here
	return c

def c_2(x,S, beta):
	c = 0
	print("C_2 calculation work:)")
	return c

def F(beta, A, B, x, p, z,S, x_0, T, y):
    return A*c_1(x, p, z, x_0, T, y, beta)+B*c_2(x, S, beta)