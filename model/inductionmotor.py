__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"


from numpy import array

class inductionmotor:
	def __init__(self, Lr = 0.0418, Ls = 0.0425, Lm = 0.0412, Rs = 0.288, Rr = 0.158, p = 6, J = 0.4, Jl = 0.38 ):
		"""Rotor Inductance"""
		self.Lr	=	Lr			
		"""Stator Inductance"""
		self.Ls	=	Ls		
		"""Mutual Inductance"""
		self.Lm	=	Lm		
		"""Stator resistance"""
		self.Rs	=	Rs	
		"""Rotor resistance"""
		self.Rr	=	Rr
		"""Pole number"""
		self.p	=	p
		"""Rotor inertia"""
		self.J	=	J	
		"""load inertia"""
		self.Jl	=	Jl
		
	
		
		
		
		
			
			
		
