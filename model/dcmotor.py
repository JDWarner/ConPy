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
from scipy import array, eye, sign, power
class dcmotor:
	"""
	The model is inaccurate
	"""
	def __init__(self, J = 3.2284e-6, b = 3.5077e-6, K_e = 0.0274, K_m = 0.0274, La = 2.75e-6, Ra = 4, Fc = 3.2284e-6 ):				
		self.num = K_e
		self.den =	array([(J*La), ((J*Ra)+(La*b)), ((b*Ra)+power(K_e,2))]);
		
		self.A = array([						
						[-b/J, K_m/J],
						[-K_e/La, -Ra/La]
						])
		self.B = array([						
						[0],
						[1/La]
						])
		self.C = array([[1, 0]])
		self.D = array([[0]])
		
		self.const = array([
							[0],
							[-Fc/J]
							])
		self.__dx_dt	=	array([[0], [0]])	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
