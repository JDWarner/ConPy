from tools.transformation import  *
from tools.signalgenerator import  *
import matplotlib.pyplot as plt
from numpy import insert, zeros, eye, array, ones
from estimation.EKF import *

def main():
	
	ekf	=	EKF(x0 = zeros((5,1)), A0 = eye(5), B0=array([[1,2],[1,2],[1,2],[1,2],[1,2]]), G0 = eye(5), H = ones((5,2)) );
	ekf.update(Zk = ones((5,1)),  U = ones((5,1)))
	print ekf.PP
	print ekf.Q
	print ekf.R
	"""tr = transformation()
	print tr.abc2dq0(2,3,4,5)
	
	pr = tr.abc2albe0(3,4,5)
	print tr.albe02abc(pr);
	
	print tr.albe2dq(2, pr[0,0],pr[1,0])"""
	"""cs = sinwave(freq=50, samplingT = 0.001, mtime=0)
	#plt.plot(cs.signal())
	at = array([]);
	ad = array([]);
	for t in arange(0, 1, 0.001):	
		at = insert(at,0, t)
		ad = insert(ad,0, cs.signal(stime=t))
	
	
	plt.plot(at, ad)
	
	plt.show()
	
	
	#signal= tp.signal()
	#plt.plot(tp.stime, signal)"""
	

if __name__ == "__main__":
    main()
