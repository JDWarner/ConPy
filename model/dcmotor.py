__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"


"""
This is a brushed DC motor model. 
A brushed DC motor is an internally commutated electric motor designed to be 
run from a direct current power source.

We can describe the motor modell with the following modell:

\dot{\i} = - \frac{R_{a}}{L_{a}}i_{a} - \frac{K_{e}}{L_{a}}\omega_{m} + \frac{1}{L_{a}}u
\dot{\omega_{m}}} = \frac{K_{m}}{J}i_{a} - \frac{K_{b}}{J}\omega_{m} - \frac{F_{c}}{J}T_{l}


where i_{a}, \omega_{m} the armature current and motor speed in rad/s, respectively; 
u is the voltage input applied to armature circuit, T_{l} is the load torque,
J is the combined moment of inertia of the load and the rotor; 
B is the equivalent viscous friction constant of the load and the motor, 
and K is the design constant depending on the construction of the motor
"""
from scipy import array, power, zeros, dot
from control.matlab import ss
class dcmotor:
	"""
	The model is inaccurate
	"""
	def __init__(self, J = 3.2284e-6, b = 3.5077e-6, K_e = 0.0274, K_m = 0.0274, La = 2.75e-6, Ra = 4, Fc = 3.2284e-6 ):				
		#self.num = K_e
		#self.den =	array([(J*La), ((J*Ra)+(La*b)), ((b*Ra)+power(K_e,2))]);
		
		self.J	=	J
		self.b	=	b
		self.K_e=	K_e
		self.K_m=	K_m
		self.La	=	La
		self.Ra	=	Ra
		self.Fc	=	Fc
		
		self.x0 = None
		
	def css(self):
		self.A = array([						
						[-self.b/self.J, self.K_m/self.J],
						[-self.K_e/self.La, -self.Ra/self.La]
						])
		self.B = array([						
						[0],
						[1/self.La]
						])
		self.C = array([[1, 0]])
		self.D = array([[0]])
		
		self.const = array([
							[0],
							[-self.Fc/self.J]
							])
							
		return ss(self.A, self.B, self.C, self.D)
		
	def dss(self, Ts):
		from tools.tools import c2d
		self.css();
		return c2d((self.A, self.B, self.C, self.D), Ts);
		
	def dlsim(self, u, Ts = 0.001, x0 = None):
		if self.x0 is None:
			if not x0 is None:
				self.x0	=	x0
			else:
				self.x0	=	zeros((2,1))
			dmodel	=	self.dss(Ts)
			
			self.Ad	=	dmodel.A
			self.Bd	=	dmodel.B
			self.Cd	=	dmodel.C
			self.Dd	=	dmodel.D
		xk_1 = dot(self.Ad, self.x0) + dot(self.Bd, u)
		y_out = dot(self.Cd, self.x0) + dot(self.Dd, u)
		self.x0	=	xk_1
		return y_out
			
		
			
		
		
							
		
	
