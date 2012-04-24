from tools.signalgenerator import *

from numpy import *
from scipy import *
from scipy.signal import *
import pylab, random
import time


"""
@summary:     This is a simple example. Testing the DC motor model response 
            and a simple PID controller
"""
if __name__ == "__main__":
    Ts = 0.001
    sinW = sinwave( Ts = Ts, mtime = 1, freq = 5, amp = 60 )   
    pw = sinW.signal()    
    
    squareW =   squarewave( Ts = Ts, mtime = 1, freq = 5, amp = 60 ) 
    sw  = squareW.signal()
    
    sawtoothW =   sawtoothwave( Ts = Ts, mtime = 1, freq = 5, amp = 60 ) 
    stw  = sawtoothW.signal()
    
    triangleW =   trianglewave( Ts = Ts, mtime = 1, freq = 5, amp = 60 ) 
    tw  = triangleW.signal()   
    
    pylab.figure( 1 )
    pylab.plot( pw )
    pylab.plot( sw )
    pylab.plot( stw )
    pylab.plot( tw )
    
    pylab.show()