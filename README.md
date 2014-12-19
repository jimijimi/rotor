rotor.py
========

Simple 2D/3D point rotation module written in pure python.

Installation
------------

No installation required. Copy the script to the working directory.

Dependencies
------------

rotor.py utilizes the standard math.py library

License
-------

The project has been released with the MIT license

Author
------

Jaime Ortiz ( jimijimi ) email: jim2o at hotmail.com

Detailed description
--------------------

rotor.py is a collection of functions. There are four main functions. The first three: ```rotateX( point, angle )```, ```rotateY( point, angle )```, ```rotateZ( point, angle )``` are used to rotate a given point around any of the cartesian coordinate axes. The last function is ```rotate( point, angle, vector )``` this allows the rotation around any arbitrary axis represented by vector.

A point is a list of three elements. ```[ x, y, z ]```
A vector is a list of three real numbers of the form ```[ vx, vy, vz ]```. The vector can be normalized or unnormalized.
An angle is specified in degrees.

Additionally the script contains functions handling vectors and quaternions. However rotor.py shuldn't be seen as a vector/quartenion library. 

rotor.py can be used in python 2.XX and python 3.XX

Example: 

Rotate an arbitrary point around the z axys:
```Python

  import rotor as r
  
  p0 = [ 1, 0, 0 ]
  angle = 90
  p1 = r.rotateZ( p0, angle )

  print( "%.3f %.3f %.3f " % ( p0[0], p0[1], p0[2] ) )
  print( "%.3f %.3f %.3f " % ( p1[0], p1[1], p1[2] ) )
```
Output:
```
  1.000 0.000 0.000
  0.000 1.000 0.000
```

![Screenshot](https://raw.github.com/jimijimi/rotor/master/images/001_rotateZ.jpg =299x267)

Example: 

Rotate an arbitrary point around the axys defined by the vector v = [ 1, 1, 1 ]:

```Python

  import rotor as r
  
  p0 = [ 1, 0, 0 ]
  angle = 90
  v = [ 1, 1, 1 ]
  p1 = r.rotate( p0, angle, v )

  print( "%.3f %.3f %.3f " % ( p0[0], p0[1], p0[2] ) )
  print( "%.3f %.3f %.3f " % ( p1[0], p1[1], p1[2] ) )
```

Output:
```
  1.000 0.000 0.000
  0.333 0.911 -0.244
```
Example: 

Create 8 points over the circuference defined around the vector v = [ 1, 1, 1 ] and starting at point p0 = [ 1, 0, 0 ]

```python
  import rotor as r

  p0 = [ 1, 0, 0 ]
  v = [ 1, 1, 1 ]
  
  for angle in range( 0, 360, 45 ):
	  p1 = r.rotate( p0, angle, v )
	  print( "%.3f,%.3f,%.3f " % ( p1[0], p1[1], p1[2] ) )
```

Output:
```
  1.000,0.000,0.000      #0 deg ( initial point )
  0.805,0.506,-0.311     #45 deg
  0.333,0.911,-0.244     #90 deg
  -0.138,0.977,0.161
  -0.333,0.667,0.667
  -0.138,0.161,0.977
  0.333,-0.244,0.911
  0.805,-0.311,0.506     #315 deg
```


