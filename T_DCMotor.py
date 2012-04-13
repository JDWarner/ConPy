__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"

from model.dcmotor import *
#from tools.tools import c2d

from control.matlab import * 
from numpy import *
from scipy import *
from scipy.signal import *
import pylab, random
import time


if __name__ == "__main__":
	dc 	= dcmotor()
	mtime  =  arange(0, 2, 0.001)
	u = ones(len(mtime));
	print dc.A
	print dc.B
	print dc.C
	print dc.D
	
	print tf2ss(dc.num, dc.den)
	(t,x)= step((dc.A, dc.B, dc.C, dc.D))
	pylab.plot(t,x)
	pylab.figure(2)
	(t,x) = step(tf2ss(dc.num, dc.den))
	
	pylab.plot(t,x)
	pylab.show()
	
	

