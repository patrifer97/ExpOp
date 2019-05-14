import numpy as np 
import statistics as stat
import math as mp
import matplotlib.pyplot as plt
import statistics as stats
from gekko import GEKKO

#All the magnitudes are expressed in cm
y=[((1.831-1.481)/10.0), ((2.005-1.653)/10.0), ((1.984-1.584)/10.0), ((1.584-1.283)/10.0), ((1.868-1.513)/10.0),((1.655-1.304)/10.0)]
mediay=stat.mean(y)
varianzay=stat.variance(y)
d=[np.sqrt((1.177-0.661)*(1.296-1.245)), np.sqrt((1.147-0.676)*(1.333-1.281)),np.sqrt((1.378-0.859)*(1.375-1.303)), np.sqrt((1.362-0.843)*(1.343-1.286)),np.sqrt((1.376-0.883)*(1.377-1.311)),np.sqrt((1.542-1.037)*(1.424-1.352))]
mediad=stat.mean(d)
varianzad=stat.variance(d)
D=[(121.18-15.51),(121.04-15.44), (121.11-15.42), (121.19-15.49),(121.05-15.50),(121.11-15.48)]
mediaD=stat.mean(D)
varianzaD=stat.variance(D)

#Wavelength (l +- errorl ) 
l= float((mediay*mediad)/ mediaD)
sum1= mp.pow( (mediad/mediaD),2)*varianzay
sum2=mp.pow( (mediay/mediaD),2)*varianzad
sum3=mp.pow( ( (mediay*mediad)/ mp.pow(mediaD,2)) ,2)*varianzaD
errorl=np.sqrt(sum1+sum2+sum3)

print l
print errorl
