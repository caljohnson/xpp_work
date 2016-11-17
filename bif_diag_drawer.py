
'''
My own bifurcation diagram parser/drawer for Auto generated "write pts" bif diagrams

Carter Johnson
'''

import numpy as np
import matplotlib.pyplot as plt

def parser(file_name=''):
	#reads the "write pts" bif diag file gen by Auto
	print 'Parsing bifurcation diagram file:', file_name
	#open file
	f = open(file_name, 'r')
	#create empty lists to hold stable vs unstable data
	d_stable_y = []
	d_stable_x = []
	d_unstable_y = []
	d_unstable_x = []

	#create empty lists to hold branch data
	branch_1_y = []
	branch_1_x = []
	branch_2_y = []
	branch_2_x = []

	#loop through lines in file
	for l in f:
		#split each line into strings by a space separator
		ll = l.split()
		#check whether the point is stable or unstable
		if ll[3] == '1' :
			#add the x, y coords of the unstable point
			d_unstable_y.append(np.float(ll[1]))
			d_unstable_x.append(np.float(ll[0]))
		if ll[3] == '2' :
			#add the x, y coords of the stable point
			d_stable_y.append(np.float(ll[1]))
			d_stable_x.append(np.float(ll[0]))
		#check which branch the point is on
		if ll[4] == '1' :
			#add the x, y coords of the point to branch 1
			branch_1_y.append(np.float(ll[1]))
			branch_1_x.append(np.float(ll[0]))
		if ll[4] == '2' :
			#add the x, y coords of the point to branch 2
			branch_2_y.append(np.float(ll[1]))
			branch_2_x.append(np.float(ll[0]))
		else:
			print 'neither stable nor unstable, or this metric is not the right one'
	
	#close file		
	f.close()	

	#return data
	return d_stable_x, d_unstable_x, branch_1_x, branch_2_x, d_stable_y, d_unstable_y, branch_1_y, branch_2_y
	
def two_branch_bif_diag(file_name = ' ', style = True):	
	#plot 2-branch bif diag

	#get data from auto bif diag write pts file
	[d_stable_x, d_unstable_x, branch_1_x, branch_2_x, d_stable_y, d_unstable_y, branch_1_y, branch_2_y] = parser(file_name)

	#plot
	plt.figure()
	plt.plot(d_stable_x, d_stable_y, 'r.', label="unstable")
	#plt.plot(d_unstable_x, d_unstable_y, 'k.')
	plt.plot(branch_1_x, branch_1_y, 'k', label="stable")
	plt.plot(branch_2_x, branch_2_y, 'k')
	plt.title(r"$\dot{X} = X (K - (X-1)^2)$")
	plt.legend(loc=0)
	plt.ylabel(r"$X^*$")
	plt.xlabel(r"$K$")
	plt.xlim((-1,2.5))
	plt.ylim((-0.1, 2.5))
	plt.show()
	plt.close()			

def main():
	two_branch_bif_diag('diagram_pts4.dat')


main()	