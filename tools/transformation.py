from numpy import array, sqrt, dot, sin, cos, pi
from conerrors.errors import InputArgumentError

class transformation:
	__T_abc2ab 		= 	array([])
						
	_T_abc2ab0 		= 	2./3. * __T_abc2ab
							
	_T_ab02abc		=	__T_abc2ab.conj().T
	
	def abc2ab0(self, *args):		
		if(len(args) == 3):
			return dot(self._T_abc2ab0, array([ [args[0]],[args[1]],[args[2]] ]))
		elif(len(args) == 1):
			return dot(self._T_abc2ab0, args[0])
		else:
			raise InputArgumentError('The argument have to be the tree current component or' \
			' an array with the tree current component!')
		
		
	def ab02abc(self, *args):
		if(len(args) == 3):
			return dot(self._T_ab02abc, array([ [args[0]],[args[1]],[args[2]] ]))
		elif(len(args) == 1):
			return dot(self._T_ab02abc, args[0])
		else:
			raise InputArgumentError('The argument have to be the tree current component or' \
			' an array with the tree current component!')
			
	def ab02dq0(self, ohmega, *args):
		pass
	
	def dq02ab0(self, ohmega, *args):
		pass
			
	def abc2dq0(self, ohmega = 0, *args):
		"""
		The dqo transformation can be thought of in geometric terms as the projection of the three 
		separate sinusoidal phase quantities onto two axes rotating with the same angular velocity 
		as the sinusoidal phase quantities. The two axes are called the direct, or d, axis and the 
		quadrature, or q, axis. Not surprisingly the q-axis is at an angle of 90 degrees to 
		(in quadrature with) the direct axis.
		Since actual stator variables either to be generated or to be measured are all in stationary a-b-c
		frame, frame transform should be executed in the control.  
		The most popular transform is between stationary a-b-c frame quantities to synchronously 
		rotating d-q quantities
		The ohmega(rad/s) is the rotation speed of the rotating frame. 		
		"""
		_T_abc2dq0		=	2./3. * array([	[cos(ohmega), 	cos(ohmega - 2.*pi / 3.), 	cos(ohmega + 2.*pi / 3.)],
											[sin(ohmega), 	sin(ohmega - 2.*pi / 3.), 	sin(ohmega + 2.*pi / 3.)],
											[1./2.,			1./2.,						1./2.					]])
		
		if(len(args) == 3):
			return dot(_T_abc2dq0, array([ [args[0]],[args[1]],[args[2]] ]))
		elif(len(args) == 1):
			return dot(_T_abc2dq0, args[0])
		else:
			raise InputArgumentError('The argument have to be the tree current component or' \
			' an array with the tree current component!')
			
	def dq02abc(self, ohmega = 0, *args):
		"""
		The dqo transformation can be thought of in geometric terms as the projection of the three 
		separate sinusoidal phase quantities onto two axes rotating with the same angular velocity 
		as the sinusoidal phase quantities. The two axes are called the direct, or d, axis and the 
		quadrature, or q, axis. Not surprisingly the q-axis is at an angle of 90 degrees to 
		(in quadrature with) the direct axis.
		Inverse Park's transformation.
		The ohmega(rad/s) is the rotation speed of the rotating frame. 
		"""
		_T_dq02abc		=	array([	[cos(ohmega), 				sin(ohmega), 				1],
									[cos(ohmega - 2.*pi / 3.), 	sin(ohmega - 2.*pi / 3.),	1],
									[cos(ohmega + 2.*pi / 3.), 	sin(ohmega + 2.*pi / 3.),	1]])
		if(len(args) == 3):
			return dot(_T_dq02abc, array([ [args[0]],[args[1]],[args[2]] ]))
		elif(len(args) == 1):
			return dot(_T_dq02abc, args[0])
		else:
			raise InputArgumentError('The argument have to be the tree current component or' \
			' an array with the tree current component!')
	
