__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"


from estimation.KalmanFilter import dEKF
from model.acim import acim
from coordinate_transformations.CT import CT

import random
from scipy import array, identity, io, zeros
from numpy import abs
import pylab


if __name__ == "__main__":
    has_break = True
    k = 0;
    Ts = 2e-06;
    #Inport mat file
    mat = io.loadmat( 'WithoutTorq.mat' )
    speed = mat['Speed']['signals'][0][0][0][0][0] 
    time = mat['Speed']['time'][0][0]    
    voltage = mat['Voltage']['signals'][0][0][0][0][0]
    current = mat['Current']['signals'][0][0][0][0][0]
    teta = mat['Teta']['signals'][0][0][0][0][0]
    
    acim = acim( Rr = 9.295e-3, Rs = 14.85e-3, Lr = 0.3027e-3, \
                 Ls = 0.3027e-3, Lm = 10.46e-3, J = 0.01, p = 2 )
    
    coord_trans = CT()
    
    k += 1;
        
    #Initialization        
    xk = array( [[0], [0], [0], [0], [0]] )
    PP = 1e-3 * identity( 5 )
    Q = identity( 5 )    
    
    """ri = random.uniform( 1e-7, 1e-2, )
    fi = random.uniform( 1e-7, 1e-2 )
    wi = random.uniform( 1e-7, 1e-2 )"""
    Q[0][0] = 1e-4
    Q[1][1] = 1e-4
    Q[2][2] = 3e-2
    Q[3][3] = 3e-2
    Q[4][4] = 1e-8
    
    #
    R = 1e-7 * identity( 2 )        
    #Classes        
    ekf = dEKF( xk, PP, Q, R )
    
    w_r = zeros( ( len( time ), 3 ) )       
    
    for i in range( 0, int( len( time ) / 5 ) ):                   
        ( Ak, Bk, H, D ) = acim.dss_statorreferenceframe1( xk[4], Ts )
        Ulb = coord_trans.clarke_m_i( voltage[i][0], voltage[i][1], voltage[i][2] )
        Ilb = coord_trans.clarke_m_i( current[i][0], current[i][1], current[i][2] )       
        Udq = coord_trans.stator_coordinate( Ulb, teta[i][0] )
        Idq = coord_trans.stator_coordinate( Ilb, teta[i][0] )
        xk = ekf.update_state( Udq, Ak, Bk );
        Gk = acim.dss_Gk_stator1( xk[2], xk[3], xk[4], Ts )
        ( xk, PP, error ) = ekf.update( Idq, Udq, Gk, Ak, Bk, H )        
        w_r[i][0] = xk[ 4 ][0]
        w_r[i][1] = speed[i][0]
        w_r[i][2] = speed[i][1]     
        print w_r[i][0] - w_r[i][1]       
        if( abs( w_r[i][0] - w_r[i][1] ) > 50 ):                
            break
            

    pylab.figure( 1 )        
    pylab.plot( time[:i, :], w_r[:i, :] )
    #pylab.title( "ri=%f, fi=%f, wi=%f, Rri=%f" % ( ri, fi, wi, Rri ) )
    #pylab.figure( 3 )
    #pylab.plot( time, current )
    pylab.show()
    """if( has_break ):
        pylab.savefig( "result" + str( i ) + ".png" )
    else:
        pylab.savefig( "good_result" + str( i ) + ".png" )
    pylab.clf()"""


