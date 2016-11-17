
'''
My own bifurcation diagram parser/drawer for Auto generated "write pts" bif diagrams

Carter Johnson
'''

import numpy as np
import matplotlib.pyplot as plt
from xppy.utils import plot

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
		# else:
		# 	print 'neither stable nor unstable, or this metric is not the right one'
	
	#close file		
	f.close()	

	#return data
	return d_stable_x, d_unstable_x, branch_1_x, branch_2_x, d_stable_y, d_unstable_y, branch_1_y, branch_2_y
	
def one_branch_bif_diag(file_name, title, ylab, xlab, xlim, ylim):	
	#plot 1-branch bif diag

	#get data from auto bif diag write pts file
	[d_stable_x, d_unstable_x, branch_1_x, branch_2_x, d_stable_y, d_unstable_y, branch_1_y, branch_2_y] = parser(file_name)

	#plot one branch figure
	plt.figure()
	plt.plot(d_stable_x, d_stable_y, 'r.', label="unstable")
	#plt.plot(d_unstable_x, d_unstable_y, 'k.')
	plt.plot(branch_1_x, branch_1_y, 'k', label="stable")
	plt.plot(branch_2_x, branch_2_y, 'k')
	plt.title(title)
	plt.legend(loc=0)
	plt.ylabel(ylab)
	plt.xlabel(xlab)
	plt.xlim(xlim)
	plt.ylim(ylim)
	plt.show()
	plt.close()			

def two_branch_bif_diag(file_name, title, ylab, xlab, xlim, ylim):	
	#plot 2-branch bif diag

	#get data from auto bif diag write pts file
	[d_stable_x, d_unstable_x, branch_1_x, branch_2_x, d_stable_y, d_unstable_y, branch_1_y, branch_2_y] = parser(file_name)

	#plot
	plt.figure()
	plt.plot(d_stable_x, d_stable_y, 'r.', label="unstable")
	#plt.plot(d_unstable_x, d_unstable_y, 'k.')
	plt.plot(branch_1_x, branch_1_y, 'k', label="stable")
	plt.plot(branch_2_x, branch_2_y, 'k')
	plt.title(title)
	plt.legend(loc=0)
	plt.ylabel(ylab)
	plt.xlabel(xlab)
	plt.xlim(xlim)
	plt.ylim(ylim)
	plt.show()
	plt.close()	

def stab_branch_parser(file_name=''):
	#reads the "write pts" stability diag file gen by Auto
	print 'Parsing stability diagram branch file:', file_name
	#open file
	f = open(file_name, 'r')

	#create empty lists to hold branch data
	# branch_1_y = []
	# branch_1_x = []
	# branch_2_y = []
	# branch_2_x = []
	# branch_3_x = []
	# branch_3_y = []
	all_data_y = []
	all_data_x = []

	#loop through lines in file
	for l in f:
		#split each line into strings by a space separator
		ll = l.split()
		#check where the point goes
		if ll[3] == '2' :
			#add the x, y coords of the point
			all_data_y.append(np.float(ll[1]))
			all_data_x.append(np.float(ll[0]))
		# if ll[4] == '3' :
		# 	#add the x, y coords of the point to branch 1
		# 	branch_1_y.append(np.float(ll[1]))
		# 	branch_1_x.append(np.float(ll[0]))
		# #check which branch the point is on
		# if ll[4] == '4' :
		# 	#add the x, y coords of the point to branch 2
		# 	branch_2_y.append(np.float(ll[1]))
		# 	branch_2_x.append(np.float(ll[0]))
		# if ll[4] == '5' :
		# 	#add the x, y coords of the point to branch 3
		# 	branch_3_y.append(np.float(ll[1]))
		# 	branch_3_x.append(np.float(ll[0]))
		# else:
		# 	print 'neither stable nor unstable, or this metric is not the right one'
	
	#close file		
	f.close()	

	#return data
	return all_data_x, all_data_y

def stability_diag(file_name1, file_name2, file_name3, title, ylab, xlab, xlim, ylim):	
	#plot stability diag

	#get data from auto bif diag write pts file
	[branch_1_x, branch_1_y] = stab_branch_parser(file_name1)
	[branch_2_x, branch_2_y] = stab_branch_parser(file_name2)
	[branch_3_x, branch_3_y] = stab_branch_parser(file_name3)

	#plot
	plt.figure()
	plt.plot(branch_1_x, branch_1_y, 'k-')
	plt.plot(branch_2_x, branch_2_y, 'k-')
	plt.plot(branch_3_x, branch_3_y, 'k-')
	plt.title(title)
	plt.legend(loc=0)
	plt.ylabel(ylab)
	plt.xlabel(xlab)
	plt.xlim(xlim)
	plt.ylim(ylim)
	plt.show()
	plt.close()	

def main():
	stability_diag('case1_stability_branch1.dat', 'case1_stability_branch2.dat','case1_stability_branch2_2.dat', "Stability Diagram", r"$D$", r"$K_2$", (0,0.5), (0,0.5))
	two_branch_bif_diag('diagram_pts4.dat', r"$\dot{X} = X (K - (X-1)^2)$", r"$X^*$",r"$K$",(-1,2.5),(-0.1, 2.5) )
	one_branch_bif_diag('case_1_x1_d_bifd_pts.dat', r"$\dot{X_1} = X (K_1 - (X-1)^2) + D(X_2 - X_1)$", r"$X_1^*$", r"$D$", (0,0.5), (0,1.5))

main()	