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
	def __init__(self, P=2.0, I=1.0, D=1.0, I_max=500, I_min=-500):
		"""
		Discrete implementation of the PID controller
		If you want a P or PI controller just set the I,D to 0
		"""
		self.Kp	=	P
		self.Ki	=	I
		self.Kd	=	D
		
		self.I_max	=	I_max
		self.I_min	=	I_min
		
		self.__error		=	0.0
		
		self.__integral 	= 0
		self.__derivative	= 0
		
		self.__dt = 0;
		
	def run(self, error):	
		#The sampling time
		if not self.__dt:
			self.__dt = self.__gettime();
			
		dt = self.__gettime() - self.__dt
		#Storing the time in seconds
		self.__dt = self.__gettime()
		
		#Calculate the integral
		self.__integral		+= 	self.Ki * error * dt
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
		return self.Kp * error +  self.__integral + self.__derivative
		
	
	def __gettime(self):
		if sys.platform == "win32":
			# On Windows, the best timer is time.clock()
			default_timer = time.clock
		else:
			# On most other platforms the best timer is time.time()
			default_timer = time.time
		return default_timer()
