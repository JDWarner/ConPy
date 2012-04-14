__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"

from model.dcmotor import *
from tools.tools import c2d

from numpy import *
from scipy import *
from scipy.signal import *
import pylab, random
import time


if __name__ == "__main__":
	dc2 	= dcmotor()
	mtime  =  arange(0, 5, 0.001)
	
	yo = array([[0, 0]])
	for i in range(len(mtime)-1):
		u = array([1])		
		yo = insert(yo, len(yo), asarray(dc2.dlsim(u)), 0);
		
	pylab.plot(mtime,yo[:,0])
	pylab.show()
	
	
	#dc = c2d((dc.A,dc.B,dc.C, dc.D), 0.001)	
	
	#(A,B,C,D) = tf2ss(dc.num, dc.den)
	#print tf2ss(dc.num, dc.den)
	#print ss2tf(A,B,C,D)
	#(t,x)= dstep((dc.A, dc.B, dc.C, dc.D, 0.001))
	#(t,y)= dstep((dc.A, dc.B, dc.C, dc.D, 0.001))
	##pylab.plot(t,y[0])
	#pylab.show()
	"""(t,x) = step(ss2tf(A,B,C,D))
	
	pylab.plot(t,x)
	pylab.show()
	"""
	

