__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"

import time, sys
class PID:
	def __init__(self, KP=2.0, KI=10.0, KD=0.001, I_max=1000, I_min=-1000, U_max=500, U_min=-500):
		"""
		@summary: Initializing the PID controller parameters
		Discrete implementation of the PID controller. If you want a P or PI controller 
		just set the I,D to 0
		
		@param KP: Proportional gain
		@param KI: Integral gain
		@param KD: Derivative gain
		@param U_max: The maximum output signal 
		@param U_min: The minimum output signal
		@param I_max: The maximum integral value 
		@param I_min: The minimal integral value
		
		@return: The control signal 
		"""
		self.Kp	=	KP
		self.Ki	=	KI
		self.Kd	=	KD
		
		self.I_max	=	I_max
		self.I_min	=	I_min
		
		self.U_max	=	U_max
		self.U_min	=	U_min
		
		self.__error		=	0.0
		
		self.__integral 	= 0
		self.__derivative	= 0
		
		self.__dt = 0;
		
	def run(self, error, Ts = None):
		"""
		@summary: Updating the PID controller parameters
		
		@param error: The error between the predefined value and the measured value
		@param Ts: Sampling time.
		
		@return: The control signal  
		"""	
		#The sampling time
		if not self.__dt:
			self.__dt = self.__gettime();
		
		if(Ts is None):
			dt = self.__gettime() - self.__dt
		else:
			dt = Ts
		#Storing the time in seconds
		self.__dt = self.__gettime()
		
		#Calculate the integral
		self.__integral		= 	self.__integral + (error * dt)
		#Upper limit
		if(self.__integral > self.I_max):
			self.__integral = self.I_max
		#Down limit
		if(self.__integral < self.I_min):
			self.__integral = self.I_min
			
		#Calculate the derivate
		self.__derivative	= 	self.Kd * ( error - self.__error ) / dt
		
		#Storing the error
		self.__error 		= 	error
		
		#Sum
		U =  self.Kp * error +  self.Ki * self.__integral + self.__derivative
		
		#Signal limitation
		if(U > self.U_max):
			U = self.U_max
		if(U < self.U_min):
			U = self.U_min
			
		return U
	
	def __gettime(self):
		"""
		@summary : On the Windows OS and the Linux OS has a different function to
		get the precious time, this function will handle this and according the OS returns the
		precious time.   
		"""
		if sys.platform == "win32":
			# On Windows, the best timer is time.clock()
			default_timer = time.clock
		else:
			# On most other platforms the best timer is time.time()
			default_timer = time.time
		return default_timer()
