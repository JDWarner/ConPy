__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"

from numpy import array, ones, arange, zeros, dot, append, empty

class simulation:
	def __init__(self, Ts = 0.001, startT = 0, endT = 2):
		self.mtime	=	arange(startT, endT, Ts)
		self.Ts	= Ts
		self.__dx_dt = ''
	
	
	def lsim(self, A ='', B = '', C = '', D = '', const = '', mtime = '', u = '', x0 = '', num ='', den = ''):		
		#Update the control signal		
		if not mtime == '':
			self.mtime	=	mtime;
		
			if len(mtime) > 2:
				self.Ts	= mtime[1] - mtime[0]
		
		if not (A == '' or B == '' or C == '' or D == ''):
			if const == '':
				const 	=	array([0])
			self.__dx_dt = x0	
				
			if self.__dx_dt == '':
				self.__dx_dt = zeros((A.shape[0], 1))				
			if u == '':
				self.u	=	ones((B.shape[1], len(self.mtime)));
				
			ret = empty((A.shape[0],1))
			
			for t in range(0,len(self.mtime)):			
				self.__dx_dt	=	dot(A, self.__dx_dt) + dot(B, array([self.u[:,t]]).conj().T) #+ const 				
				ret	=	append(ret, dot(C, self.__dx_dt) + D, 1)
				
		elif not (num == '' or den == ''):
			pass
		else:		
			from conerrors.errors import InputArgumentError
			raise InputArgumentError('Unable to define the model from the input')
			
		return (ret, t, u)
			
		
			
		
		
			
