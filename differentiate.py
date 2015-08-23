import numpy as np

def differentiate(u,dt):
	"""
	this function differentiates
	a mesh function with centered difference
	at inner points and forward and backward difference
	at end points
	"""
	dudt=np.zeros(len(u))
	#centered difference , n=1,..,N-1
	for i in range(1,len(dudt)-1,1):
		dudt[i]=(u[i+1]-u[i-1])/(2*dt)

	#Forward difference at n=1
	i=0
	dudt[i]=(u[i+1]-u[i])/dt
	
 	#Backward fifference at n=N
	i=len(dudt)-1 
	dudt[i]=(u[i]-u[i-1])/dt

	return dudt
	
def test_differentiate():
	"""
	Given a quadratic function
	test if the differentiation in differentiate
	function is correct
	"""
	
	t=np.linspace(0,6,13)
	u=10*t + 5
	dt=t[1]-t[0]
	dudt_computed=differentiate(u,dt)
	dudt_expected=10
	error=abs((dudt_computed-dudt_expected).max())
	Tol=1E-15
	assert error<Tol,"differetiation formula is incorrect"
	print "test passed with error %15f: " %error


def differentiate_vec(u,dt):
	"""
	Using vectorization,
	this function differentiates
	a mesh function with centered difference
	at inner points and forward and backward difference
	at end points
	"""
	dudt=np.zeros(len(u))
	#centered difference , n=1,..,N-1
	dudt[1:-1]=(u[2:]-u[0:-2])/(2*dt)

	#Forward difference at n=1
	dudt[0]=(u[1]-u[0])/dt
	
 	#Backward fifference at n=N
	i=len(dudt)-1 
	dudt[-1]=(u[-1]-u[-2])/dt

	return dudt
	
def test_differentiate_vec():
	"""
	Given a quadratic function
	test if the differentiation in differentiate
	function is correct
	"""
	
	t=np.linspace(0,6,13)
	u=10*t + 5
	dt=t[1]-t[0]
	dudt_computed=differentiate_vec(u,dt)
	dudt_expected=10
	error=abs((dudt_computed-dudt_expected).max())
	Tol=1E-15
	assert error<Tol,"differetiation formula is incorrect"
	print "test passed with error %15f: " %error


test_differentiate_vec()







	
