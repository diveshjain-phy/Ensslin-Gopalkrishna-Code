# Modelling Enslin and GopalKrishna 2001
# Major updates 


from astropy.io import ascii
from op import chicalc
import numpy as np
import matplotlib.pyplot as plt
import time


#################################### Frequency range ##############################################
#at which spectra has to computed

f_nuobs=np.arange(0.001*1e9,100*1e9,0.1*1e9)




#####################################	Input Parameters	#####################################
# Extract the redshift and properties of the system from source.py
import source
print("retieving source parameters from source.py")
z	=source.z
print("********************************************")
print("Source properties")
print("Source properties:redshift",z)
print("********************************************")


# To Take User Defined inputs regarding assumed scenario and phase for the system.
# Also checks for illegal entry and assigns default entry. 
scen=input("Enter the scenario[A, B or C](default: scenario B): ")
if scen not in ['A','B','C']:
	scen='B'


phase=input("Enter the phase[0,1,2,3 or 4](default: phase 3): ")
if phase not in ['0','1','2','3','4']:
	phase='3'
phase=int(phase)
print('Choice of Scenario is:',scen,'	','Choice of Phase is',phase)

# Compression Ratio Index
#b=[1.8,1.2,0,2.0,0]

b=[1.8,1.2,1e-2,2.0,1e-2]
##################### Input parameters obtained from EGfit or EG_best30_params##############3
f_err=[]
flx_obs=0

delt=[0, 0.067299999999999999, 0.112, 0.223, 0.29999999999999999]
tau=[0.02, 0.013299999999999999, 1e2, -0.44500000000000001, 1e2]
B_src=[5.6782000000000004, 1.3452, 1.3452, 3.3999999999999999, 0.0]
V_src=[0.017100000000000001, 0.1487, 0.1487, 0.037, 0.0]
norm=0.0003282272023
s=input("Want to vary delt_flash?[yes or no](default: no)")
if s=="yes":
	fdx=np.arange(delt[3]*0.4,delt[3]*2,0.02)
else:
	fdx=np.arange(delt[3],delt[3]+2,30)
for delt[3] in fdx:

	B_src	=[i*1e-6 for i in B_src]
	V_src	=[i*(3.08*1e24)**3 for i in V_src]
	delt	=[i*(3.154*1e16) for i in delt]
	tau	=[i*(3.154*1e16) for i in tau]
	flx_min=[]
	pst	=[]
	print(delt)
	for phase in range(0,4):

		Bsrci=B_src[phase]
		Vsrci=V_src[phase]
		chi,flux,B,u_B,C,C0,V,pst0=chicalc(delt,tau,phase,z,Bsrci,Vsrci,b,f_nuobs,f_err,flx_obs,norm)
		flux	=[i/(1e-26) for i in flux]#1.756*1e-28
		flx_min.append(flux)
		pst.append(pst0)
	delt	=[i/(3.154*1e16) for i in delt]
	tau	=[i/(3.154*1e16) for i in tau]
	B	=[i/1e-6 for i in B]
	V	=[i/(3.08*1e24)**3 for i in V]
	u_B	=[i/(1.6*1e-12) for i in u_B]
		
	#zip(delt,tau,C,b,C0,V,B,u_B,pst)
	delt=np.around(delt, decimals=4)
	tau=np.around(tau, decimals=4)
	C=np.around(C, decimals=4)
	b=np.around(b, decimals=4)
	C0=np.around(C0, decimals=4)
	V=np.around(V, decimals=4)
	B=np.around(B, decimals=4)
	u_B=np.around(u_B, decimals=4)
	pst=np.around(pst, decimals=4)
	import csv
	with open('tableA1914.csv','w') as fle:
		writer	=csv.writer(fle,delimiter='\t')
		writer.writerows(zip(delt,tau,C,b,C0,V,B,u_B,pst))
	#print(flx_min)
	plt.plot(f_nuobs,flx_min[0],'b',label='Injection',linewidth='3')
	plt.plot(f_nuobs,flx_min[1],'g',label='expansion',linewidth='3')
	plt.plot(f_nuobs,flx_min[2],'r',label='lurking',linewidth='3')
	plt.plot(f_nuobs,flx_min[3],label='flashing delta t_3*'+str(np.around(delt[3]/0.223,2)),linewidth='0.5')


def readfile(myspec):
	dat = ascii.read(myspec)
	return dat 
myfile ='A1914_spec.dat'   #col1 =freq col2 = flux col3 = error
spec = readfile(myfile)
print(spec)
f_nuobs=np.array(spec['nughz'])
f_nuobs	=[i*1e9 for i in f_nuobs]
f_err=np.array(spec['fmyerr'])
flx_obs = np.array(spec['fmy'])
plt.errorbar(f_nuobs,flx_obs,yerr=f_err,uplims=True,lolims=True,fmt='o',ecolor='k',linestyle='',markerfacecoloralt='k',markeredgecolor='k',markerfacecolor='k',markersize='1',label='Observation')#,'+',markersize=5,label='Observation')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('frequency in Hz')
plt.ylabel('Flux in mJy')
ax=plt.gca()
ax.set_ylim([1e-10,1e14])
plt.legend()
plt.show()




	
###	
###	 while writing the program for chi square calculation for a time step,
###	 we send only one value of b that coresponds to user input phase
###	c=c+1
















 
