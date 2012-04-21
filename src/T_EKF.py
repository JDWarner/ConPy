__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"


from numpy import *
from scipy import *
from scipy.signal import *
from tools.signalgenerator import sinwave
import random

from model.dcmotor import dcmotor
from estimation.KalmanFilter import dKF 
import pylab
"""
@summary:     A simple test of the  Extended Kalman Filter
"""

if __name__ == "__main__":
    dc2      = dcmotor()
    Ts = 0.001
    ekf =   dKF(x0 = zeros((3,1)))
    
    mtime = arange( 0, 0.1, Ts )
    
    yo = zeros( ( len( mtime ), 1 ) )
    xk = zeros( ( len( mtime ), 3 ) )
    xe = zeros( ( len( mtime ), 3 ) )
    noise = zeros( ( len( mtime ), 3 ) )
    error = zeros( ( len( mtime ), 3 ) )
    ( A, B, C, D ) = dc2.dss( Ts )
    
    sinW = sinwave( Ts = Ts, mtime = 0.1, freq = 50, amp = 20 )
    pw = sinW.signal()     
    
    H   = array([[0, 0, 0],[0, 1, 0],[0, 0, 0]])
    for i in range( len( mtime ) ):    
        #u = pw[i]    
        u = array([[1.]])
        y_k, x_k = dc2.dlsim( u, Ts = Ts);
        
        yo[i,:] = y_k
        xk[i,:] = x_k.conj().T
        
        
        z_K = copy(x_k)
        z_K[0] = 0  
        z_K[1] = z_K[1] + random.uniform(-0.5, 0.5) 
        noise[i,:] =  z_K[1]
        x_k_e, PP, err = ekf.update( z_K, u, A, B, H )
        
        xe[i,:] = x_k_e.conj().T  
        
        
        print "meas"
        print xk[i,:]
        print "es"
        print xe[i,:]
        
    pylab.plot( xk[:, 1])        
    pylab.plot( xe[:, 1])
    pylab.plot(noise)
    
    pylab.figure(2)
    pylab.plot( xk[:, 0])        
    pylab.plot( xe[:, 0])
    #pylab.plot( error)
    #pylab.figure(2)
    #pylab.plot( xk[:,1])    
    #pylab.plot( xe[:, 1])    
    pylab.show()
    
