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

from model.dcmotor import dcmotor
from estimation.EKF import dEKF
import pylab
"""
@summary:     A simple test of the  Extended Kalman Filter
"""

if __name__ == "__main__":
    dc2      = dcmotor()
    Ts = 0.001
    ekf =   dEKF(x0 = zeros((3,1)))
    
    mtime = arange( 0, 0.1, Ts )
    
    yo = zeros( ( len( mtime ), 3 ) )
    ( A, B, C, D ) = dc2.dss( Ts )
    
    
    
    for i in range( len( mtime ) ):
        u = array( [1.] )        
        yo[i, :] = dc2.dlsim( u, Ts = Ts );
        #ekf.update( Zk, u, A, B, H, Gk )    
        
    pylab.plot( yo[:, 0] )    
    pylab.show()
    
