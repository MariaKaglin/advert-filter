import os

def read_function(file_path):
	print("Read_function work:)")
	if not os.path.exists(file_path):
		return 1
	f = open(file_path, 'r')
	x, y = [], []
	for line in f:
		x_coord, y_coord = line.split()
		x.append(x_coord)
		y.append(y_coord)
	f.close()
	return x, y

def write_function(x, y, file_path):
	print("Write_function work:)")
	f = open(file_path, 'w')
	for i in range(len(x)):
		f.write(str(x[i])+" "+str(y[i])+"\n")
	f.close()
	return 0
def write_coeff(coef, file_path):
	print("Write_coeff work:)")
	f = open(file_path, 'w')
	for i in range(len(coef)):
		f.write(str(coef[i])+"\n")
	f.close()
	return 0