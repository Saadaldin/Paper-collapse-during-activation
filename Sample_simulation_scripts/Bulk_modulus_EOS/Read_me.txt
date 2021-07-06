
#------------------------------------- General note ------------------------------------------#

- These are examples for calculations of the bulk modulus of MOFs from energy-volume equation of state.
- The method is modified from that described in ref: J. Phys. Chem. Lett. 2017, 8, 2, 357–363
 
#---------------------- Comment about the adopted method ---------------------------------#

- The optimization were looped for 100 cycles while jiggling the atoms between cycles.
- This was necessary to improve the optimization of certain structures.
- But for some of them, the results were better without looping.

- The examples are for two MOFs:
	- DIHVIB (HKUST-1)
	- SUKYIH

- The reason to provide the second example; because for some MOFs the angle or dihedral styles are hybrid.
- Therefore, the angle coefficients must be read whenever the restart file is recalled.
 
#------------------------------------- Additional note ----------------------------------------#

- A python code is included to calculate and plot the bulk modulus from the energy-volume data.