#Calcualting the bulk modulus by fitting simulation data to the Murnaghan equation
#
#
#Created by: Saad Aldin Mohamed
#Date: November 30, 2020
#
################################################################################################
import numpy as np
import matplotlib.pyplot as plt
from pymatgen.analysis.eos import EOS

data = np.genfromtxt("V_PE_data_DIHVIB_clean.out")
V = data[:,0]
E = data[:,1]

E0 = min(E)
index = np.argmin(E)
V0 = V[index]

eos = EOS(eos_name='murnaghan')
eos_fit = eos.fit(V, E)
results = [ v for v in eos_fit.results.values()]

e0, b0, b1, v0 = results

#  1 GPa = 0.14393 kcal/mol/Angstrom^(3) (http://openmopac.net/manual/p=n.html)
B0 = b0/0.14393

#----------------------------------------------#
E_new = eos_fit(V)

# correlation coefficient
r_matrix = np.corrcoef(E, E_new)
r = r_matrix[0,1]
r_squared = r**2

#----------------------------------------------#
print ("The bulk modulus = ", B0, "GPa")
print ("R squared coefficient = ", r_squared)
filename = "bulk modulus.txt"
raw = open(filename,"w")
raw.write("B0 = " + str("%.3f" %B0) +" GPa\n") 
raw.write("R^2 = " + str("%.3f" %r_squared)) 
raw.close()


##########################  Plot 1  #####################################
fig = plt.figure()
plt.plot(V - V0, E - E0, 'ro', markersize = 8, linewidth=2, label ="MD data")
plt.plot(V - V0, E_new - E0, "r-", linewidth=1.5, label ="Fitting")

plt.legend(loc="best", fontsize=14)
#plt.title("DIHVIB")
plt.xlabel("V-Vo", fontsize=22)
plt.ylabel("E-Eo", fontsize=22) 
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.rc('font', size=20)
plt.rc('axes', titlesize= 20)

plt.tight_layout()
fig.show()
fig.savefig("EOS_DIHVIB.png")
