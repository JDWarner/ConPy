__author__ = "Robert Unguran"
__copyright__ = "Copyright 2012"
__credits__ = ["Robert Unguran"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Robert Unguran"
__email__ = "unguranr@gmail.com"
__status__ = "Under Development"

from numpy import array, sqrt, dot, vstack, sin, cos

class CT:
    def __init__( self ):
        """"""
        
    def clarke_p_i_i0( self, a, b, c ):
        """Power Invariant"""
        T = sqrt( 2. / 3. ) * array( [
                              [1., -1. / 2., -1. / 2.],
                              [0., sqrt( 3. ) / 2., -sqrt( 3. ) / 2.],
                              [1. / sqrt( 2. ), 1. / sqrt( 2. ), 1. / sqrt( 2. )]
                              ] )
        return  dot( T, array( [[a], [b], [c]] ) );
        
    
    def inv_clarke_p_i_i0( self, alpha, beta, Io = 0 ):
        """Power Invariant"""
        T = sqrt( 2. / 3. ) * array( [
                              [1., 0., 1 / sqrt( 2. )],
                              [-1. / 2., sqrt( 3. ) / 2., 1. / sqrt( 2. )],
                              [-1. / 2., -sqrt( 3. ) / 2., 1. / sqrt( 2. )]
                              ] )
        
        return  dot( T, array( [[alpha], [beta], [Io]] ) );
    
    
    def clarke_p_i( self, a, b ):
        """Power Invariant"""
        T = array( [
                    [sqrt( 3. / 2. ), 0],
                    [1. / sqrt( 2. ), sqrt( 2. )]
                ] )
        return  dot( T, array( [[a], [b]] ) );
        
    
    def inv_clarke_p_i( self, alpha, beta ):
        """Power Invariant"""
        T = array( [
                    	[sqrt( 2. / 3. ), 0],
                    	[-1. / sqrt( 6. ), 1. / sqrt( 2. )],
			[-1. / sqrt( 6. ), -1. / sqrt( 2. )]
                ] )
        
        return dot( T, array( [[alpha], [beta]] ) )
        #return vstack((a_b, array([-a_b[0][0]-a_b[1][0]])))
     
    def clarke_m_i_io( self, a, b, c ): 
        """Magnitude invariant"""
        T = 2. / 3.* array( [
                              [1., -1. / 2., -1. / 2.],
                              [0., sqrt( 3. ) / 2., -sqrt( 3. ) / 2.],
                              [1. / 2., 1. / 2., 1. / 2.]
                              ] )
           
        return  dot( T, array( [[a], [b], [c]] ) );
        
    
    def inv_clarke_m_i_io( self, alpha, beta, Io ):
        T = 3. / 2.* array( [
                              [2. / 3., 0., 1. / 2.],
                              [-1. / 3., 1 / sqrt( 3. ), 1. / 2.],
                              [-1. / 3., -1 / sqrt( 3. ), 1. / 2.]
                              ] )
        
        return  dot( T, array( [[alpha], [beta], [Io]] ) );
        
    def clarke_m_i( self, a, b, c ): 
        """Magnitude invariant"""
        T = 2. / 3.* array( [
                              [1., -1. / 2., -1. / 2.],
                              [0., sqrt( 3. ) / 2., -sqrt( 3. ) / 2.],
                              ] )
           
        return  dot( T, array( [[a], [b], [c]] ) );
        
    
    def inv_clarke_m_i( self, alpha, beta ):
        T = 3. / 2.* array( [
                              [2. / 3., 0.],
                              [-1. / 3., 1 / sqrt( 3. )],
                              [-1. / 3., -1 / sqrt( 3. )]
                              ] )
        
        return  dot( T, array( [[alpha], [beta]] ) );
    
    
    def stator_coordinate( self, lb, teta ):
        
        T = array( [[cos( teta ), -sin( teta )],
                    [sin( teta ), cos( teta )]] )
        return dot( T, lb )
    
    def inv_stator_coordinate( self, lb, teta ):
        T = array( [[cos( teta ), sin( teta )],
                    [-sin( teta ), cos( teta )]] )
        
        return dot( T, lb )
    
    def rotor_coordinate( self, lb, teta ):             
        return self.inv_stator_coordinate( lb, teta )
    
    def inv_rotor_coordinate( self, lb, teta ):
        return self.stator_coordinate( lb, teta ) 
