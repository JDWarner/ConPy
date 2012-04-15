__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"

from numpy import identity, shape, dot, linalg, eye
from conerrors.errors import InputArgumentError
from control.matlab import tf2ss, TransferFunction
class dEKF:
	def __init__(self,sys, x0, Q = None, R = None,  PP = None):
		self.n = x0.shape[0]
		
		#error covariance matrix
		if PP == None:
			self.PP =	1e-4 * 	identity(self.n)
		else:
			self.PP	=	PP
		#noise covariance matrice
		if Q == None:
			self.Q 	=	1e-4 * 	identity(self.n)
		else:
			self.Q	=	Q
		#noise covariance matrice	
		if R == None:
			self.R 	=	1e-4 * 	identity(self.n)
		else:
			self.R	=	R
		
		self.xk = x0
		
	def update(self, Zk, U, Ak, Bk, H, Gk):
		"""
		Predict the next states
		"""		
		
		#Predicted (a priori) state estimate
		self.xk = 	dot(Ak, self.xk) + dot(Bk, U);
		
		#Predicted (a priori) estimate covariance
		self.PP	=	dot( dot( Gk, self.PP), Gk.conj().T) + self.Q;
		
		#Optimal Kalman gain
		KalG	=	dot( dot( self.PP, H.conj().T), linalg.inv( dot( dot( H, self.PP), H.conj().T ) + self.R ) );
		
		#Innovation or measurement residual
		error 	= 	Zk - dot(H, self.xk);
		
		#Updated (a posteriori) state estimate
		self.xk	=	self.xk	+ dot(KalG, error);
		
		#Updated (a posteriori) estimate covariance
		self.PP	=	dot( ( eye ( self.n ) - dot(KalG, H)), self.PP);
		
		return self.xk
