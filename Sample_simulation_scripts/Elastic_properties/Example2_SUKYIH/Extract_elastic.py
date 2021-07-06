# A code to extract elastic properties from MD output data
#
#
# Developed by: Saad Aldin Mohamed
# Date: April 30, 2021
# Email: sa3danny@yahoo.com
#
######################################################################################################
import numpy as np
import csv
import matplotlib.pyplot as plt
from numpy.linalg import inv, eig


#------------------------------------- Reading elastic constants----------------------------------------#

name  = "SUKYIH_clean"
data = np.genfromtxt("Elastic_constants_"+name+".out")
C = data[:,1]
M = np.array([[C[0], C[3], C[4], C[9], C[10], C[11]],
			 [C[3], C[1], C[5], C[12], C[13], C[14]],
			 [C[4], C[5], C[2], C[15], C[16], C[17]],
			 [C[9], C[12], C[15], C[6], C[18], C[19]],
			 [C[10], C[13], C[16], C[18], C[7], C[20]],
			 [C[11], C[14], C[17], C[19], C[20], C[8]]])
S = inv (M)

#------------------------------------ Calculating elastic properties --------------------------------------#					 

""" Bulk Modulus """
Kv = ((M[0,0]+M[1,1]+M[2,2]) + 2*(M[0,1]+M[0,2]+M[1,2]))/9
Kr = 1/(((S[0,0]+S[1,1]+S[2,2]) + 2*(S[0,1]+S[0,2]+S[1,2])))

""" Shear Modulus"""
Gv = ((M[0,0]+M[1,1]+M[2,2])/3 - (M[0,1]+M[0,2]+M[1,2])/3  + (M[3,3]+M[4,4]+M[5,5]))/5
Gr = 5/(4*(S[0,0]+S[1,1]+S[2,2])/3 - 4*(S[0,1]+S[0,2]+S[1,2])/3 + (S[3,3]+S[4,4]+S[5,5]))

""" Young Modulus """
Ev = (9*Kv*Gv)/(3*Kv+Gv) 
Er = (9*Kr*Gr)/(3*Kr+Gr) 

""" Write Output """
with open("Elastic_properties.csv","w", newline="") as output1:
	writer = csv.writer(output1)
	writer.writerow(["name","Kv","Kr","Gv", "Gr", "Ev", "Er"])	#header 
	writer.writerow([name, str("%.3f" %Kv), str("%.3f" %Kr), str("%.3f" %Gv), str("%.3f" %Gr), str("%.3f" %Ev), str("%.3f" %Er)])

output1.close()

#----------------------------------------- Calculating eigenvalues  ---------------------------------------#			

Eig_values, Eig_vectors = eig (M)
Eig_values = np.round(Eig_values,3) # round to 3 digits
list = Eig_values.tolist() # not sorted

""" Write Output """
with open("Eigen_values.csv","w", newline="") as output2:
	writer = csv.writer(output2)
	writer.writerow(["name", "gamma1", "gamma2", "gamma3", "gamma4", "gamma5", "gamma6"])	#header 
	writer.writerow([name] + list)

output2.close()

#----------------------------------------------------------------------------------------------------------#


