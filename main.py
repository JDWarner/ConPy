#!/usr/bin/env python
__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"

from tools.transformation import *
from tools.signalgenerator import *
from controller.PID.PID import *
from numpy import pi, insert, array, arange
import pylab, random


import time

if __name__ == "__main__":
	pid = PID(P=0.0001, I= 100, D = 0.0001)
	pidc = array([0])
	error= array([0])
	for i in arange(100):
		r = random.uniform(-10,10) 
		pidc	=	insert(pidc, len(pidc), pid.run(r))
		error	=	insert(error, len(error), r)
	
	pylab.plot(error)	
	pylab.figure(2)
	pylab.plot(pidc)
	pylab.show()
	"""T = transformation()
	ph = T.abc2albe0(4,5,60)
	print ph
	
	print T.albe02abc(ph)
	
	print T.albe2dq(2, ph[0,0], ph[1,0])
	
	print T.abc2dq0(2,4,5,60)"""
	
	
	"""start = time.time()
	tp = sinwave(freq=1, phase = -(2./3.)*pi, mtime=40)
	signal=	tp.signal()	
	
	pylab.plot(tp.stime, signal)
	
	trw	=	trianglewave(freq=1, phase = -(2./3.)*pi, mtime=30)
	signal=	trw.signal()		
	pylab.plot(trw.stime, signal)
	
	trw	=	sawtoothwave(freq=1, phase = -(2./3.)*pi, mtime=20)
	signal=	trw.signal()		
	
	end = time.time()
	print end - start
	pylab.show()
	#pylab.plot(trw.stime, signal)
	#pylab.plot(tp.stime, signal[1])
	#pylab.plot(tp.stime, signal[2])"""
	
	
	
	

