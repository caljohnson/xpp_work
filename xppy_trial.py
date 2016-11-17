'''
 Attempt to use Nowacki's XPP Python shell 
 '''
import numpy as np
import xppy
from xppy.utils.diagram import read_diagram
from xppy.utils import plot
from xppy.utils import solution

#File to open
tmp_name = 'test'
tmp_ode  = tmp_name+'.ode'
tmp_set  = tmp_name+'.set'

#want to see xpp output words
verbose= False

#run using default settings specified in test.ode
output = xppy.parser.run(tmp_ode, tmp_set, verbose)
#run from last output as initial conditions
output = xppy.parser.runLast(output, 'test.ode', 'temp_set.set', verbose)
#run Last function does not work as described

#try to change r,K,gamma and run again
	#make list of parameters to change (list of lists)
	#format for each list in the list:
		#['tp', 'name', val]
		#where 'tp' = 'par', 'init', or '@'
pars = [['par', 'r', 0.6], ['par', 'gamma', 0.6], ['par', 'K', 1], ['init', 'X', 0.6]]
#physically changes the text of the ode file
#xppy.parser.changeOde(pars, tmp_ode)
#runs xppaut again using the new edited ode file
#output = xppy.parser.run(tmp_ode, tmp_set, verbose)


#figure out how to get plots
# plot.plotDiag('output.dat', axes=None, tr_file = '', tr_cols=[], xlabel='t', ylabel='X',img_dir='', img_ext='png')
# plot.plotLC('output.dat', cols=[0,1], axes=None, colormap=None)

#print(output)
# bifdiag = solution.parseBifDiag('test_bifd.auto')
# bifdiag = read_diagram('diagram_pts.dat')
plot.plotDiag('diagram_pts.dat')