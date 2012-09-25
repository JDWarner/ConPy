__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"

"""
The  model of the three phase induction motor
"""
from scipy import array, power
class acim:
    """
    The model is inaccurate
    """
    def __init__( self, Rr = 9.295e-3, Rs = 14.85e-3, Lr = 0.3027e-3, Ls = 0.3027e-3, Lm = 10.46e-3, J = 0.01, p = 4 ):
        """        
        @summary: Initializing the AC induction motor's parameters       
        @param Rr: Rotor resistance 
        @param Rs: Stator resistance
        @param Lr: Rotor inductance
        @param Ls: Stator inductance
        @param Lm: Leakage inductance
        @param J: Motor inertia
        @param p: motor pole pairs                       
        @return: None
        """
        self.R_r = Rr
        self.R_s = Rs
        self.L_r = Lr
        self.L_s = Ls
        self.L_m = Lm
        self.J = J
        self.p = p
        
        self.tau_r = self.L_r / self.R_r
        self.gamma_r = 1. - ( power( self.L_m , 2 ) / ( self.L_s * self.L_r ) )
        self.T_r = self.R_s + ( power( self.L_m , 2 ) * self.R_r ) / power( self.L_r , 2 )
        
        
        
    def css( self ):
        """
        Returns the continuous model of the ACIM
        """  

    def dss_statorreferenceframe1( self, omega, Ts = 2e-06 ):
        """
        @summary: The discrete model of the three-phase AC induction motor
        @param omega: The rotor speed
        @param Ts: Sampling time 
        @return: Returns the motor model in stationary reference frame
        where the states are the followings (isd, isq, fird, firq, w). We assuming that 
        dw\dt=0, the changes of the rotor speed is zero.
        """
        
        
        Ak = array( [
                       [
                            1. - Ts * ( self.T_r / ( self.L_s * self.gamma_r ) ),
                            0.,
                            Ts * ( self.L_m / ( self.L_s * self.gamma_r * self.L_r * self.tau_r ) ),
                            Ts * ( ( omega * self.L_m ) / ( self.L_s * self.gamma_r * self.L_r ) ),
                            0.
                        ],
                        [
                            0.,
                            1. - Ts * ( self.T_r / ( self.L_s * self.gamma_r ) ),
                            - Ts * ( ( omega * self.L_m ) / ( self.L_s * self.gamma_r * self.L_r ) ),
                            Ts * ( self.L_m / ( self.L_s * self.gamma_r * self.L_r * self.tau_r ) ),
                            0.   
                        ],
                        [
                             self.L_m / self.tau_r,
                             0.,
                             1. - Ts * ( 1. / self.tau_r ),
                             - Ts * omega,
                             0.
                        ],
                        [
                             0.,
                             Ts * ( self.L_m / self.tau_r ),
                             Ts * omega,
                             1. - Ts * ( 1. / self.tau_r ),
                             0.   
                        ],
                        [   
                            0.,
                            0.,
                            0.,
                            0.,
                            1.
                         ]
                   ] )
        
        Bk = array( [
                   [Ts / ( self.L_s * self.gamma_r ), 0. ],
                   [0., Ts / ( self.L_s * self.gamma_r ) ],
                   [0., 0.],
                   [0., 0.],
                   [0., 0.]
                   ] )
        
        Ck = array( [[1., 0., 0., 0., 0.],
                    [0., 1., 0., 0., 0.]] )
        
        Dk = array( [[0.]] )
        
        return ( Ak, Bk, Ck, Dk )
    
    
    def dss_Gk_stator1( self, fird, firq, omega, Ts = 2e-06 ):
        """
        @summary: The discrete model 
        @param fird : The d part of the rotor flux  
        @param firq : The q part of the rotor flux
        @param omega: The rotor speed
        @param Ts: Sampling time
         
        @return: 
        """
        Gk = array( [
                        [ 
                             1. - Ts * ( self.T_r / ( self.L_s * self.gamma_r ) ),
                             0,
                             Ts * ( self.L_m / ( self.L_s * self.gamma_r * self.L_r * self.tau_r ) ),
                             Ts * ( ( omega * self.L_m ) / ( self.L_s * self.gamma_r * self.L_r ) ),
                             Ts * ( ( firq * self.L_m ) / ( self.L_s * self.gamma_r * self.L_r ) )
                        ],
                        [
                             0,
                             1. - Ts * ( self.T_r / ( self.L_s * self.gamma_r ) ),
                             - Ts * ( ( omega * self.L_m ) / ( self.L_s * self.gamma_r * self.L_r ) ),
                             Ts * ( self.L_m / ( self.L_s * self.gamma_r * self.L_r * self.tau_r ) ),
                             - Ts * ( ( fird * self.L_m ) / ( self.L_s * self.gamma_r * self.L_r ) )
                        ],
                        [
                            self.L_m / self.tau_r,
                            0,
                            1. - Ts * ( 1. / self.tau_r ),
                            - Ts * omega,
                            - Ts * firq
                        ],
                        [
                            0,
                            Ts * ( self.L_m / self.tau_r ),
                            Ts * omega,
                            1. - Ts * ( 1. / self.tau_r ),
                            Ts * fird
                        ],
                        [
                            0.,
                            0.,
                            0.,
                            0.,
                            1.
                        ]
                    ] )
        return Gk   
