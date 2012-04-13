__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"

from tools.simulation import *
from tools.tools import c2d
from model.dcmotor import *

from numpy import pi, insert, array, arange
import pylab, random
import time

if __name__ == "__main__":
	dcmotor 	= dcmotor()
	
	sim = simulation()
	
	#print dcmotor.num
	#print dcmotor.den
	c2d	=	c2d()
	print dcmotor.A
	print dcmotor.B
	
	(Ad,Bd, Cd, Dd) = c2d.ssc2d(dcmotor.A, dcmotor.B, dcmotor.C, dcmotor.D)
	
	print Ad
	print Bd
	(ret, t, u) = sim.lsim(Ad,Bd, Cd, Dd)
	
	pylab.plot(ret[0,:])
	pylab.show()
