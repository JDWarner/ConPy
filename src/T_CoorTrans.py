from numpy import array, arange, zeros
from tools.signalgenerator import threephase
from coordinate_transformations.CT import CT
import pylab

if __name__ == "__main__":
    
    Ts = 0.001
    mtime = 0.1
    
    three_phase = threephase(amp = 220, freq = 50, Ts = Ts, mtime = mtime)
    signal = three_phase.signal()
    
    transf = CT()
    
    atime = arange( 0, mtime, Ts )
    a_alpha_beta = zeros((3,  len( atime ) ))
    a_a_b_c = zeros((3,  len( atime ) ))
    
    for i in range( len( atime ) ):        
        alpha_beta = transf.clarke_i0(signal[0][i], signal[1][i], signal[2][i])
        a_b_c = transf.inv_clarke_i0(alpha_beta[0][0], alpha_beta[1][0], alpha_beta[2][0])
        
        a_alpha_beta[0][i] = alpha_beta[0][0] 
        a_alpha_beta[1][i] = alpha_beta[1][0]
        a_alpha_beta[2][i] = alpha_beta[2][0]
        
        a_a_b_c[0][i] = a_b_c[0][0]
        a_a_b_c[1][i] = a_b_c[1][0]
        a_a_b_c[2][i] = a_b_c[2][0] 
    
    pylab.figure( 1 )
    pylab.subplot(3,1,1, title="Three phase signal")
        
    pylab.plot(signal[0])
    pylab.plot(signal[1])
    pylab.plot(signal[2])
    
    pylab.subplot(3,1,2, title='Alpha,Beta transformation')
    pylab.plot(a_alpha_beta[0])
    pylab.plot(a_alpha_beta[1])
    pylab.plot(a_alpha_beta[2])
       
    pylab.subplot(3,1,3, title="Alpha,Beta inverse transformation")
    pylab.plot(a_a_b_c[0])
    pylab.plot(a_a_b_c[1])
    pylab.plot(a_a_b_c[2])
    
    
    for i in range( len( atime ) ):        
        alpha_beta = transf.clarke(signal[0][i], signal[1][i])
        a_b_c = transf.inv_clarke(alpha_beta[0][0], alpha_beta[1][0])
        
        a_alpha_beta[0][i] = alpha_beta[0][0] 
        a_alpha_beta[1][i] = alpha_beta[1][0]        
        
        a_a_b_c[0][i] = a_b_c[0][0]
        a_a_b_c[1][i] = a_b_c[1][0]
        a_a_b_c[2][i] = a_b_c[2][0] 
    
    pylab.figure( 2 )
    pylab.subplot(3,1,1, title="Three phase signal")
        
    pylab.plot(signal[0])
    pylab.plot(signal[1])
    pylab.plot(signal[2])
    
    pylab.subplot(3,1,2, title='Alpha,Beta transformation')
    pylab.plot(a_alpha_beta[0])
    pylab.plot(a_alpha_beta[1])    
       
    pylab.subplot(3,1,3, title="Alpha,Beta inverse transformation")
    pylab.plot(a_a_b_c[0])
    pylab.plot(a_a_b_c[1])
    pylab.plot(a_a_b_c[2])
    pylab.show()
    
    pylab.show()
    
    
    
    