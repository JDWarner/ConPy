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
from controller.PID import PID
from tools.signalgenerator import sinwave


from numpy import *
from scipy import *
from scipy.signal import *
import pylab, random
import time


"""
@summary: 	This is a simple example. Testing the DC motor model response 
			and a simple PID controller
"""
if __name__ == "__main__":
	dc2 	 = dcmotor()
	Ts = 0.001
	
	mtime = arange( 0, 0.1, Ts )
	
	yo = zeros( ( len( mtime ), 3 ) )
	( A, B, C, D ) = dc2.dss( Ts )
	
	for i in range( len( mtime ) ):
		u = array( [1.] )		
		yo[i, :] = dc2.dlsim( u, Ts = Ts );
		
		
	pylab.plot( yo[:, 0] )	
	
	#Clearing the previous position
	dc2.x0	 = 	None;
	#Creating and initializing the PID controller
	pid	 = 	PID( P = 0.25, I = 10, D = 0.0001 )
	
	pw	 = 	ones( 100 ) 
	y_out = zeros( ( len( pw ), 1 ) )
	sw = 0;
	for i in range( len( pw ) ):
		error = pw[i] - sw;
		u = pid.run( error, Ts = Ts )
		
		sw = dc2.dlsim( u );
		y_out[i, :] = sw
	
	pylab.figure( 2 )
	pylab.plot( pw )
	pylab.plot( y_out[:, 0] )
	
	
	#Clearing the previous states
	dc2.x0	 = 	None;	
	
	sinW = sinwave( Ts = Ts, mtime = 1, freq = 5, amp = 6000 )
	pw = sinW.signal()	 
	y_out = zeros( ( len( pw ), 1 ) )
	u_out = zeros( ( len( pw ), 1 ) )
	sw = 0;
	for i in range( len( pw ) ):
		error = pw[i] - sw;
		u = pid.run( error, Ts = Ts )
		
		sw = dc2.dlsim( u );
		y_out[i, :] = sw
		u_out[i, :] = u
		
	
	pylab.figure( 3 )
	pylab.plot( pw )
	pylab.plot( y_out[:, 0] )
	pylab.figure( 4 )
	pylab.plot( u_out[:, 0] )
	pylab.show()
	
	

