import Integrate_modul
import Tabulate as tab
import DiffEq_modul as diff
import Interpolate_modul as interp
import betaSearch_modul
import input_output_modul as inout
import Quality_F as q
import Graph_modul as graph


def get_solution(auto,p_path, S_path, z_path,T,  f, y_0, beta, beta_or_x_0):

	if auto:
		beta_from = beta
		beta_to = beta_or_x_0
		x_0 = beta_or_x_0
	else:
		x_0 = beta_or_x_0
	
	p = inout.read_function(p_path)
	print("p",p_path, p)
	S = inout.read_function(S_path)
	print("S",S_path,  S)
	z = inout.read_function(z_path)
	print("Z",z_path, z)
	p_coef = interp.interpolate(p[0], p[1])
	S_coef = interp.interpolate(S[0], S[1])
	z_coef = interp.interpolate(z[0], z[1])
	
	inout.write_coeff(p_coef, "p_coef.txt")
	inout.write_coeff(S_coef, "S_coef.txt")
	inout.write_coeff(z_coef, "z_coef.txt")
    #численное дифф z

	U = tab.tabulate_integral(p_coef, [1,2,3,4,5,6,7,8,9,10])
	U_coef = interp.interpolate([1,2,3,4,5,6,7,8,9,10], U)


	if auto:
		count = 10
		beta_from = float(beta_from)
		step = (float(beta_to) - beta_from)/count
		beta_opt = beta_from
		x, y = [],[]
		F_min = q.F(beta_from, 1, 10, x, p, z,S, x_0, T, y)
		for i in range(10):
			x_i, y_i = diff.diff_system(U_coef,S_coef,z_coef, T, x_0,y_0, beta_from + step*i)
			x.append(x_i)
			y.append(y_i)

			inout.write_coeff(x_i, "x_coef"+str(i)+".txt")
			inout.write_coeff(y_i, "y_coef"+str(i)+".txt")
			if q.F(beta_from+step*i, 1, 10, x, p, z,S, x_0, T, y) < F_min:
				F_min = q.F(beta_from+step*i, 1, 10, x, p, z,S, x_0, T, y)
				beta_opt = beta_from+step*i
		inout.write_coeff([beta_opt], "beta_opt.txt")
		graph.create_graph(p_coef, x, S_coef, z_coef, y)

	else:
		x, y = diff.diff_system(U_coef,S_coef,z_coef, T, x_0,y_0,beta)
		inout.write_coeff(x, "x_coef.txt")
		inout.write_coeff(y, "y_coef.txt")
		C_1 = q.c_1(x, p_coef, z_coef, x_0, T, y, beta)
		C_2 = q.c_2(x, S_coef, beta)

		inout.write_coeff([C_1], "c_1.txt")
		inout.write_coeff([C_1], "c_2.txt")
		graph.create_graph(p_coef, x, S_coef, z_coef, y)

get_solution(True,"p_tab.txt", "S_tab.txt", "z_tab.txt", 1,[], 2, 2, 3)

