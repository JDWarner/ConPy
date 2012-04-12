__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"

from numpy import identity, shape
from conerrors.errors import InputArgumentError
class EKF:
	def __init__(self, x0, Q = '', R = '',  PP = '', Ts = 0.001):
		n = x0.shape[0]
		if PP == '':
			self.PP 	=	1e-4 * 	identity(n)
		else:
			self.PP	=	PP
			
		if Q == '':
			self.Q 	=	1e-4 * 	identity(n)
		else:
			self.Q	=	Q
			
		if R == '':
			self.R 	=	1e-4 * 	identity(n)
		else:
			self.R	=	R
			
		self.I	=	identity(n)

