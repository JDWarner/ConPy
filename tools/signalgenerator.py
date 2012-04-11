__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"


from numpy import sin, cos, arange, array, pi, zeros

class threephase:
	"""
	Generating a threephase signal
	Ua	=	Umax * sin( 2 * pi * F * t) + bias
	Ub	=	Umax * sin( 2 * pi * F * t - 2/3 * pi ) + bias
	Uc	=	Umax * sin( 2 * pi * F * t - 4/3 * pi ) + bias
	"""
	def __init__(self, amp = 220, freq = 50, samplingT = 0.01, mtime = 0.5, bias = 0, phase = 0):
		self.amp	 	= 	amp
		self.freq		=	freq 
		self.samplingT	=	samplingT
		self.mtime		=	mtime
		self.bias		=	bias
		self.phase		=	phase
		self.stime		=	array([])			
		self.__init_signal()
		
	def signal(self, stime = 0):
		if(stime):
			self.__init_signal(stime)		
		return array([ 	self.phasea, self.phaseb, self.phasec ])
		
	def __init_signal(self, stime = 0):
		sinw	=	sinvawe(self.amp, self.freq, self.samplingT, self.mtime, self.bias, self.phase)
		if(stime):
			sinw.stime	=	stime;
					
		self.stime	=	sinw.stime;		
		self.phasea	=	sinw.signal( phase = 0 )
		self.phaseb	=	sinw.signal( phase =  -(2./3.)*pi )
		self.phasec	=	sinw.signal( phase =  -(4./3.)*pi )

class squarewave:	
	"""
	Generating a square signal using the signum of the sinus function. 
	x(t) = amp * sign( sin( 2 * pi * F * t + phase ) + bias )
	where 2*pi*f is the angular frequency
	"""
	def __init__(self, amp = 220, freq = 50, samplingT = 0.01, mtime = 0.5, bias = 0, phase = 0):		
		self.amp	 	= 	amp
		self.freq		=	freq 
		self.samplingT	=	samplingT
		self.mtime		=	mtime
		self.bias		=	bias
		self.phase		=	phase
		self.stime		=	arange(0, self.mtime - self.samplingT, self.samplingT)		
		
	def signal(self, stime = 0, phase = 0, freq = 0, bias = 0, amp = 0):		
		from numpy import sign		
		if not stime:
			stime 	= 	self.stime
		if not phase:
			phase 	= 	self.phase;
		if not freq:
			freq 	= 	self.freq;
		if not bias:
			bias 	= 	self.bias;
		if not amp:
			amp = self.amp;			
		x 	=	2 * pi * freq * stime 
		return amp * sign( sin( x + phase ) ) + bias;
		
					
class trianglewave:
	"""
	Generating a triangle vawe.
	x(t)= amp * 8 / pi^2 *sum(( -1 )^i * (sin((2 * i + 1) * 2 * pi * F * t + phase) + bias) / ( 2 * i + 1 )^2 )
	"""
	def __init__(self, amp = 220, freq = 50, samplingT = 0.01, mtime = 5, bias = 0, phase = 0, harmonic = 50):
		self.amp	 	= 	amp
		self.freq		=	freq 
		self.samplingT	=	samplingT
		self.mtime		=	mtime
		self.bias		=	bias
		self.phase		=	phase
		self.harmonic	=	harmonic
		self.stime 		= 	arange(0, self.mtime - self.samplingT, self.samplingT)			
		
	def signal(self, stime = 0, phase = 0, freq = 0, bias = 0, amp = 0, harmonic = 0):				
		if not stime:
			stime 	= 	self.stime
		if not phase:
			phase 	= 	self.phase;
		if not freq:
			freq 	= 	self.freq;
		if not bias:
			bias 	= 	self.bias;
		if not amp:
			amp 	= 	self.amp;	
		if not harmonic:
			harmonic= 	self.harmonic;
					
		x 	=	2 * pi * freq * stime 
		res = zeros(len(x))
		for i in range( 0, harmonic ):			
			res +=  pow( -1, i ) * sin(( 2 * i + 1 ) * (x + phase) ) / pow( ( 2. * i + 1.), 2 );			
			
		return amp * (8. / pow(pi,2)) * res + bias
	
class sawtoothwave:
	"""
	Generating a triangle vawe.
	x(t)= amp * 2 / pi *sum(( -1 )^i * (sin( 2 * i * pi * F * t + phase) + bias) / i )
	where 2*pi*f is the angular frequency
	"""
	def __init__(self, amp = 220, freq = 50, samplingT = 0.01, mtime = 5, bias = 0, phase = 0, harmonic = 50):
		self.amp	 	= 	amp
		self.freq		=	freq 
		self.samplingT	=	samplingT
		self.mtime		=	mtime
		self.bias		=	bias
		self.phase		=	phase
		self.harmonic	=	harmonic
		self.stime 		= 	arange(0, self.mtime - self.samplingT, self.samplingT)			
		
	def signal(self, stime = 0, phase = 0, freq = 0, bias = 0, amp = 0, harmonic = 0):				
		if not stime:
			stime 	= 	self.stime
		if not phase:
			phase 	= 	self.phase;
		if not freq:
			freq 	= 	self.freq;
		if not bias:
			bias 	= 	self.bias;
		if not amp:
			amp 	= 	self.amp;	
		if not harmonic:
			harmonic= 	self.harmonic;
					
		x 	=	2 * pi * freq * stime 
		res = zeros(len(x))
		for i in range( 1, harmonic + 1):			
			res +=  pow( -1, i+1 ) * sin( i * (x + phase) ) / i;			
			
		return amp * (2. / pi) * res + bias
		
class sinwave:
	"""	
	Generating a sinus vawe.
	x(t)= amp * sin(2 * pi * F * t + phase) + bias
	"""
	def __init__(self, amp = 220, freq = 50, samplingT = 0.01, mtime = 5, bias = 0, phase = 0):
		self.amp	 	= 	amp
		self.freq		=	freq 
		self.samplingT	=	samplingT
		self.mtime		=	mtime
		self.bias		=	bias
		self.phase		=	phase
		self.stime 		= 	arange(0, self.mtime - self.samplingT, self.samplingT)			
		
	def signal(self, stime = 0, phase = 0, freq = 0, bias = 0, amp = 0):				
		if not stime:
			stime 	= 	self.stime
		if not phase:
			phase 	= 	self.phase;
		if not freq:
			freq 	= 	self.freq;
		if not bias:
			bias 	= 	self.bias;
		if not amp:
			amp 	= 	self.amp;			
		x 	=	2 * pi * freq * stime 
		return amp * sin(x + phase) + bias;
		
class coswave:
	"""
	Generating a cosinus vawe
	x(t) = amp * cos(2 * pi * F * t + phase) + bias
	"""
	def __init__(self, amp = 220, freq = 50, samplingT = 0.01, mtime = 5, bias = 0, phase = 0):
		self.amp	 	= 	amp
		self.freq		=	freq 
		self.samplingT	=	samplingT
		self.mtime		=	mtime
		self.bias		=	bias
		self.phase		=	phase
		self.stime 		= 	arange(0, self.mtime - self.samplingT, self.samplingT)		
		
	def signal(self, stime = 0, phase = 0, freq = 0, bias = 0, amp = 0):		
		if not stime:
			stime 	= 	self.stime
		if not phase:
			phase 	= 	self.phase;
		if not freq:
			freq 	= 	self.freq;
		if not bias:
			bias 	= 	self.bias;
		if not amp:
			amp 	= 	self.amp;			
		
		x 	=	2 * pi * freq * stime 
		return amp * cos( x + phase) + bias;
		

