__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"

from numpy import array, sqrt, dot, vstack

class CT:
    def __init__(self):
        """"""
        
    def clarke_i0(self,a,b,c):
        """"""
        T = sqrt(2./3.)* array([
                              [1., -1./2., -1./2.],
                              [0., sqrt(3.)/2., -sqrt(3.)/2.],
                              [1./sqrt(2.), 1./sqrt(2.), 1./sqrt(2.)]
                              ])
        return  dot(T, array([[a],[b],[c]]));
        
    
    def inv_clarke_i0(self,alpha, beta, Io=0):
        T = sqrt(2./3.)* array([
                              [1., 0., 1/sqrt(2.)], 
                              [-1./2.,  sqrt(3.)/2., 1./sqrt(2.)], 
                              [-1./2.,  -sqrt(3.)/2., 1./sqrt(2.)]
                              ])
        
        return  dot(T, array([[alpha],[beta],[Io]]));
    
    
    def clarke(self,a,b):
        """"""
        T = array([
                    [sqrt(3./2.), 0],                              
                    [1./sqrt(2.), sqrt(2.)]
                ])
        return  dot(T, array([[a],[b]]));
        
    
    def inv_clarke(self,alpha, beta):
        T = array([
                    [sqrt(2./3.), 0],                              
                    [-1./sqrt(6.), 1./sqrt(2.)]
                ])
        
        a_b = dot(T, array([[alpha],[beta]]))
        return vstack((a_b, array([-a_b[0][0]-a_b[1][0]])))