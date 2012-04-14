__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"

from numpy import hstack , vstack, zeros
from scipy.linalg import expm
from control.matlab import tf2ss, ss2tf

def c2d ( sys , Ts, method = 'ZOH' ) :
	"""
	@summary: From continuous time convert discrete time
	
	@param sys:  an instance of the LTI class or a tuple describing the system.
        The following gives the number of elements in the tuple and
        the interpretation:

         2: (num, den)        
         4: (A, B, C, D)
    @param Ts: Sampling time
    @param method: The name of the discretization method
    
    @return: The discrete system    
	"""
	if(len(sys) == 2):
		(A, B, C, D)	=	tf2ss( sys )
	else:
		(A, B, C, D)	=	sys
	
	n	=	A.shape[ 0 ]
	nb	=	B.shape[ 1 ]
	if(method == 'ZOH'):
		ztmp=	zeros ( ( nb , n + nb ) )	
		tmp	=	hstack ( ( A , B ) )	
		tmp	=	vstack ( ( tmp , ztmp ) )	
		tmp	=	expm( tmp * Ts )
	
		A	=	tmp [ 0 : n , 0 : n ]
		B	=	tmp [ 0 : n , n : n+nb ]
		
		
	sysd = ( A , B , C , D  )	
	if(len(sys) == 2):
		return ss2tf ( sysd )
	return sysd