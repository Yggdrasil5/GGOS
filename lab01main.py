
import numpy as np
import scipy as si

# Constants and fundamentals----------------------
fundamentals = {
'G' : 6.674e-11, #Gravitational constant
'LovenumbersRe' : 0.3077,
'LovenumbersIm' : 0.0036,
'GM_sun' : 1.32712442076e20, #Gravitational parameter of the sun
'GM_moon' : 4.9027779e12, #Gravitational parameter of the moon
'ME' : 5.9737e24, #Mass of Earth
'ER' : 6378136.6, #Earthradius
'Omega_N' : 7.2921151467064e-5, #nominal earth rotation rate
}
fundamentals['A'] = 0.3296108*fundamentals.get('ME')*fundamentals.get('ER')**2,
fundamentals['B'] = fundamentals.get('A'),
fundamentals['C'] = 0.3307007*fundamentals.get('ME')*fundamentals.get('ER')**2,
#--------------------------------------------------
# Import data--------------------------------------
moon = np.loadtxt(fname='./data/moon.txt', skiprows=2)
sun = np.loadtxt(fname='./data/sun.txt', skiprows=2)
earthrotationvec = np.loadtxt(fname='./data/earthRotationVector.txt', skiprows=2)
potentCoeffAOHIS = np.loadtxt(fname='./data/potentialCoefficientsAOHIS.txt', skiprows=2)
potentCoeffTides = np.loadtxt(fname='./data/potentialCoefficientsTides.txt', skiprows=2)

AAM_isdc = np.loadtxt(fname='./data/AAM.txt', skiprows=3)
HAM_isdc = np.loadtxt(fname='./data/HAM.txt', skiprows=3)
OAM_isdc = np.loadtxt(fname='./data/OAM.txt', skiprows=3)
#-------------------------------------------------

stop=0;




