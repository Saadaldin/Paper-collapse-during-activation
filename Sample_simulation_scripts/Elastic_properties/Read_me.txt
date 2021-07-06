
#------------------------------------- General note ------------------------------------------#

- These are two examples for calculations of the elastic properties of MOFs.
- The simulation scripts were modified from the "ELASTIC" example in LAMMPS.
- Also, another modified script for MOFs can be found in ref: CrystEngComm, 2019, 21, 1653-1665
 
#---------------------- Main modifications in present script ---------------------------------#

- In present work, a two minimizations stage was used to optimize/relax the structure.
- In addition, the optimization were looped for 100 cycles while jiggling the atoms between cycles.
- This was necessary to improve the optimization of certain structures.

- The examples are for two MOFs:
	- DIHVIB (HKUST-1)
	- SUKYIH

- The reason to provide the second example; because for some MOFs the angle or dihedral styles are hybrid.
- Therefore, the angle coefficients must be read whenever the restart file is recalled.
- So, the displace.mod file have been changed accordingly.
 
#------------------------------------- Additional note ----------------------------------------#

- A python code is included to calculate the elastic properties from the elastic constants.