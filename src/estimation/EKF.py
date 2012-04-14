__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"

from numpy import identity, shape, dot
from conerrors.errors import InputArgumentError
class EKF:
	def __init__(self, x0, A0, B0, G0, H, Q = '', R = '',  PP = '', Ts = 0.001):
		self.n = x0.shape[0]
		
		#error covariance matrix
		if PP == '':
			self.PP =	1e-4 * 	identity(self.n)
		else:
			self.PP	=	PP
		#noise covariance matrice
		if Q == '':
			self.Q 	=	1e-4 * 	identity(self.n)
		else:
			self.Q	=	Q
		#noise covariance matrice	
		if R == '':
			self.R 	=	1e-4 * 	identity(self.n)
		else:
			self.R	=	R
		
		self.Ak = 	A0
		self.Bk	=	B0
		self.Gk	=	G0
		self.H	=	H	
		
		self.xk = x0
		
	def update(self, Zk, U, Ak = '', Bk = '', Gk = ''):
		"""
		Predict the next states
		"""
		if not Ak == '':
			self.Ak =	Ak
		if not Bk == '':
			self.Bk =	Bk
		if not Gk == '':
			self.Gk =	Gk		
		
		#Predicted (a priori) state estimate
		self.xk = 	dot(self.Ak, self.xk) + dot(self.Bk, U);
		
		#Predicted (a priori) estimate covariance
		self.PP	=	dot( dot( self.Gk, self.PP), self.Gk.conj().T) + self.Q;
		
		#Optimal Kalman gain
		KalG	=	dot( dot( self.PP, self.H.conj().T), linalg.inv( dot( dot( self.H, self.PP), self.H.conj().T ) + self.R ) );
		
		#Innovation or measurement residual
		error 	= 	Zk - dot(self.H, self.xk);
		
		#Updated (a posteriori) state estimate
		self.xk	=	self.xk	+ dot(KalG, error);
		
		#Updated (a posteriori) estimate covariance
		self.PP	=	dot( ( eye ( self.n ) - dot(KalG, self.H)), self.PP);
		
		return self.xk
