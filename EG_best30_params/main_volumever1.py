# Modelling Enslin and GopalKrishna 2001
# Major updates 
# This program for a particular value of alphae generates parameter file with the list of parameters correesponding to 
# a list of n smallest value of chi for that alphae. and if a range of alphae is to be explored then, for each alphae , a 
# similar file is generated.

from getpar import getparspace
from astropy.io import ascii
from operations import chicalc
import numpy as np
import matplotlib.pyplot as plt
import time

####################################	Read Observational data	####################################	

def readfile(myspec):
	dat = ascii.read(myspec)
	return dat 
myfile =input('Enter the file name to read observational data')
spec = readfile(myfile)
print(spec)
f_nuobs=np.array(spec['nughz'])
f_err=np.array(spec['fmyerr'])
flx_obs = np.array(spec['fmy'])
flx_obs	=[i*(1e-26) for i in flx_obs]
f_err	=[i*(1e-26) for i in f_err]



#####################################	Input Parameters	#####################################
# Extract the redshift and properties of the system from source.py
import source
print("retieving source parameters from source.py")
z	=source.z
V_src	=source.V*(3.08*1e24)**3
print("********************************************")
print("Source properties")
print("Source properties:redshift",z)
print("Source properties:Volume(in cm3)",V_src)
print("********************************************")
          ###################################################
#clist=[]
#vlist=[]#phase 1volume
	######################################################3
# To Take User Defined inputs regarding assumed scenario and phase for the system.
# Also checks for illegal entry and assigns default entry. 
scen=input("Enter the scenario[A, B or C](default: B): ")
if scen not in ['A','B','C']:
	scen='B'


phase=input("Enter the phase[0,1,2,3 or 4](default: 3): ")
if phase not in ['0','1','2','3','4']:
	phase='3'
phase=int(phase)
print('Choice of Scenario is:',scen,'	','Choice of Phase is',phase)
print("********************************************")

stype=input("Enter the type of search: Coarse[enter C] or Fine[enter F](default: C):")
if stype=='F':
	stype='Fine'
	snum=20
else:
	stype='Coarse'
	snum=10
	
salphae=input("Do you want to search for alphae: No[enter N] or Yes[enter Y(modified Coarse search)] (default: N):")
if salphae=='Y':
	nalphae=np.arange(2.2,2.7,0.1)
	stype='Coarse'
	snum=10
else:
	nalph=input("Enter the value for alphae:")
	nalph=float(nalph)
	nalphae=np.arange(nalph,nalph+1,30)
print("Type of Search:",stype,"		","Value of alphae to be explored:",nalphae)

print("********************************************")

# Compression Ratio Index
b=[1.8,1.2,1e-4,2.0,1e-4]



#####################################	Operational Parameters	#####################################
# To generate time-scale parameter space and save in parex.dat
getparspace(scen,phase,snum)
time.sleep(10)

# Reading data from table to phase-wise iterative solutions 
timeex= ascii.read('parex.dat')

print(timeex)

for alphaex in nalphae:
	chivollist=[]
	chilist=[]
	flx=[]
	nm=[]
	magB=[]
	volV=[]
	count=0	#counter
	# DEFINE PARAMETERS TO STORE RESULT OF EACH SET OF TIMESCALES
	filen='myresult'+str(alphaex)
	result	=open(filen,'w')
	for i in timeex:

		# instancing time scale for each set
		delt	=[0.0,0.0,0.0,0.0,0.0]	#delt0=0 for all sets
		tau	=[0.0,0.0,1e2,0.0,1e2]	#Time scale for tau_4 and tau_2 is prescribed infinity
		#setting up tau
		tau[0]	=i['tau0']
		tau[1]	=(2.0/3.0)*tau[0]
		tau[3]	=i['tau3']
		#setting up delt
		delt[0]	=0
		delt[1]	=i['delt1']
		delt[2]	=i['delt2']
		delt[3]	=i['delt3']
		delt[4]	=i['delt4']	
		B_src=i['Bsrc']*1e-8
		delt	=[i*(3.154*1e16) for i in delt]
		tau	=[i*(3.154*1e16) for i in tau]
		
		print('Iteration number',count+1)
		chi,flux,norm,B,V=chicalc(delt,tau,phase,z,B_src,V_src,b,f_nuobs,f_err,flx_obs,alphaex)
		chilist.append(chi)
		flx.append(flux)
		nm.append(norm)
		magB.append(B)
		volV.append(V)
		myresult	=str(count)+'\t'+str(chi)+'\n'
		result.write(myresult)
		count=count+1
############################	generating the parameter file consisting of the smallest 30 chi values from chilist	############33
	temp_chilist=chilist
	chivolindex=[]
	### the max value of i decides the number of smallest chi to be considered from chilist
	for i in range(0,30):
		temp_x=np.nanargmin(temp_chilist)
		chivollist.append(temp_chilist[temp_x])
		chivolindex.append(chilist.index(chivollist[i]))
		temp_chilist.remove(chivollist[i])
	filepar='parameters'+str(alphaex)
	print("********************************************")
	print("The parameters corresponding to 10 lowest chi values are stored in:",filepar)
	result_par=open(filepar,'w')
	parresult='Value of chi'+'\t'+'del_t'+'\t'+'tau'+'\t'+'Volume of phases'+'\t'+'Magnetic field at different phases'+'\t'+'Norm'+'\n'
	result_par.write(parresult)
	par_i=0
	for chi_min_ind in chivolindex:
		flx_min		=flx[chi_min_ind]
		norm_min	=nm[chi_min_ind]
		mag_min		=magB[chi_min_ind]
		vol_min		=volV[chi_min_ind]
		mag_min	=[round(i/1e-6,4) for i in mag_min]
		vol_min	=[round(i/(3.08*1e24)**3,4) for i in vol_min]
		# instancing time scale for each set
		delt_m	=[0.0,0.0,0.0,0.0,0.0]	#delt0=0 for all sets
		tau_m	=[0.0,0.0,np.inf,0.0,np.inf]	#Time scale for tau_4 and tau_2 is prescribed infinity
		#setting up tau
		tau_m[0]	=round(timeex['tau0'][chi_min_ind],4)
		tau_m[1]	=round((2.0/3.0)*tau_m[0],4)
		tau_m[3]	=round(timeex['tau3'][chi_min_ind],4)
		#setting up delt
		delt_m[0]	=0
		delt_m[1]	=round(timeex['delt1'][chi_min_ind],4)
		delt_m[2]	=round(timeex['delt2'][chi_min_ind],4)
		delt_m[3]	=round(timeex['delt3'][chi_min_ind],4)
		delt_m[4]	=round(timeex['delt4'][chi_min_ind],4)	
		parresult=str(chivollist[par_i])+'\t'+str(delt_m)+'\t'+str(tau_m)+'\t'+str(vol_min)+'\t'+str(mag_min)+'\t'+str(norm_min)+'\n'
		result_par.write(parresult)
		par_i=par_i+1


# to be added to this program is the choice to open any alphaex and plot for a particular choice of parameters
#	fig,ax = plt.subplots()
#	ax.set_yscale('log')
#	ax.set_xscale('log')
#	ax.set_xlabel('Frequency (GHz)')
#	ax.set_ylabel('Flux density (mJy)')
#	flx_obs1		=[i/(1e-26) for i in flx_obs]
#	ax.plot(f_nuobs,flx_obs1,'bo',label='obs')
#	flx_min1		=[i/(1e-26) for i in flx_min]
#	ax.plot(f_nuobs,flx_min1,'r-',label=str(alphaex))
#	ax.legend()
#print("Chi min for each alphae:",clist)
#print("Volume of expansion phase for each alphae:",vlist)
#plt.show()















 
