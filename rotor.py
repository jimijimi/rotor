# rotor - rotation module v1.0
#         2D/3D rotation of arbitrary point in the space.
#         version 1.0 released on November 10, 2014
#
# Ready to use. For python 2.XX or 3.XX 
#
'''
  The MIT License (MIT)
  Copyright (c) 2014 Jaime Ortiz
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
'''
import math

def info():
	return "rotor - rotates a given point around an arbitrary defined axis"

# Vector and Quaternion algebra

def vectorCrossProduct( u, v ):
	"""Returns the vector resulting from the cross product between two vectors"""
	return [ u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0] ] 
		
def vectorDotProduct( v0, v1 ):
	"""Returns the scalar quantity representing the dot product of two vectors"""
	return v0[0] * v1[0] + v0[1] * v1[1] + v0[2] * v1[2]

def vectorSum( v0, v1 ):
	"""Returns the sum of two vectors"""
	return [ v0[0] + v1[0], v0[1] + v1[1], v0[2] + v1[2] ]

def vectorScaling( scale, v ):
	"""Returns the multiplication of a vector and a scalar"""
	return [ scale * v[0], scale * v[1], scale * v[2] ]

def vectorMagnitude( v ):
	"""Returns the magnitude of the vector"""
	return ( ( v[0] ** 2 + v[1] ** 2 + v[2] ** 2 ) ** 0.5 )

def vectorNormalized( v ):
	"""Returns de normalized vector"""
	v_mag = vectorMagnitude( v );
	return [ v[0] / v_mag, v[1] / v_mag, v[2] / v_mag ] 
	
def quaternionDotProduct( q0, q1 ):
	"""Returns the scalar quantiry representing the dot product of two vectors"""
	return q0[0] * q1[0] + q0[1] * q1[1] + q0[2] * q1[2] + q0[3] * q1[3]
	
def quaternionProduct( q0, q1 ):
	""""Returns the quaternion from two quaternion multiplication"""
	s0 = q0[0]
	s1 = q1[0]
	v0 = [ q0[1], q0[2], q0[3] ]
	v1 = [ q1[1], q1[2], q1[3] ]
	real_part = s0 * s1 - vectorDotProduct( v0, v1 )
	vector_scaling_1 = vectorScaling( s0, v1 )
	vector_scaling_2 = vectorScaling( s1, v0 )
	vector_cross_product_1 = vectorCrossProduct( v0, v1 )
	vector_sum_1 = vectorSum( vector_scaling_1, vector_scaling_2 )
	vector_sum_2 = vectorSum( vector_sum_1, vector_cross_product_1 )
	return[ real_part, vector_sum_2[0], vector_sum_2[1], vector_sum_2[2] ] 

def quaternionMagnitude( q ):
	"""Returns the magnitude of a quaternion"""
	return ( ( q[0] ** 2 + q[1] ** 2 + q[2] ** 2 + q[3] ** 2 ) ** 0.5 )

def quaternionInverse( q ):
	"""Returns the inverse of a quaternion"""
	return ( [ q[0], -q[1], -q[2], -q[3] ] )
	
def quaternionRotor( v, phi ):
	"""Returns the quaternion representing the rotation around the vector v by an angle phi expressed in radians"""
	return [ math.cos( phi / 2.0 ), 
			 math.sin( phi / 2.0 ) * v[0], 
			math.sin( phi / 2.0 ) * v[1], 
			 math.sin( phi / 2.0 ) * v[2] ]

def deg2rad( angle_deg ):
	"""Converts the given angle to radians"""
	return angle_deg * 2.0 * math.pi / 360.0

#  === Rotation functions ===
	
def rotate( p0, angle, v ):
	"""Rotates an arbitrary point p0 around an arbitrary axis v by an angle expessed in degrees"""
	v         = vectorNormalized( v )
	p         = [ 0, p0[0], p0[1], p0[2] ]
	angle_rad = deg2rad( angle )
	q         = quaternionRotor( v, angle_rad )
	invq      = quaternionInverse( q )
	qp        = quaternionProduct( q, p )
	qpinvq    = quaternionProduct( qp, invq )
	return [ qpinvq[ 1 ], qpinvq[ 2 ], qpinvq[ 3 ] ]
		
def rotateX( p0, angle ):
	"""Rotates an arbitrary point p0 around the X axis by an angle expressed in degrees"""
	q1 = rotate( p0, angle, [ 1, 0, 0 ] )
	return [ q1[ 0 ], q1[ 1 ], q1[ 2 ] ]

def rotateY( p0, angle ):
	"""Rotates an arbitrary point p0 around the Y axis by an angle expressed in degrees"""
	q1 = rotate( p0, angle, [ 0, 1, 0 ] )
	return [ q1[ 0 ], q1[ 1 ], q1[ 2 ] ]

def rotateZ( p0, angle ):
	"""Rotates an arbitrary point p0 around the Z axis by an angle expressed in degrees"""
	q1 = rotate( p0, angle, [ 0, 0, 1 ] )
	return [ q1[ 0 ], q1[ 1 ], q1[ 2 ] ]
	
if __name__ == "__main__":
	pass
