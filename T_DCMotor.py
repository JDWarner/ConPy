__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"

from model.dcmotor import *

from numpy import *
from scipy.signal import lsim, lsim2, step
import pylab, random
import time

if __name__ == "__main__":
	dc 	= dcmotor()
	mtime  =  arange(0, 2, 0.001)
	u = ones(len(mtime));
	
	
	(t,x) = step((dc.A,dc.B, dc.C, dc.D))
	
	pylab.plot(t,x)
	pylab.show()
	
	
