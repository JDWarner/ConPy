__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"

from numpy import eye

class c2d:
	"""
	This is an aproximation:
	Ad = e^(Ac*Ts) == 1 + ATs
	Bd == BT	
	"""
	def ssc2d(self, A, B, C, D, Ts= 0.001):
		I	=	eye(A.shape[0])
		
		Ad = I + A * Ts
		Bd = B * Ts
		Cd = C
		Dd = D
		
		return (Ad,Bd, Cd, Dd)
	
