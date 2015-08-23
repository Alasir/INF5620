import numpy as np
import pylab as pl
from math import pi, sin


def mesh_function(f,t):
	"""
	given a function f, and an array t
	such that t=t0,t1,...tN, compute
	f(t0),...,f(tN)
	"""
	g=np.zeros(len(t)) #initialise the mesh function g
	
	# loop over the array t
	for i in range(len(t)):
		g[i]=f(t[i])


	#return g
	return g

def mesh_function_plot(a,b,dt):
	"""
	this function plot a mesh function at n mesh points,
        given a continuous function
	f defined on an interval [a,b].
	"""
	#define f
	def f(t):
		if t <=3:
			return np.exp(-t)
		else:
			return np.exp(-3*t)
	#compute mesh function
	n=int((b-a)/dt)
	t=np.arange(a,b,dt)
	u=mesh_function(f,t)
	pl.plot(t,u)
	pl.xlabel('t')
	pl.ylabel('mesh function')
	pl.title('plot of a mesh function for %d mesh points' %n)
	pl.show()

# input values from command 
a=int(raw_input("Enter first interval point a :" ))
b=int(raw_input("Enter second interval point b :" ))
dt=float(raw_input("Enter mesh size  dt :" ))
mesh_function_plot(a,b,dt)

	
	

	
