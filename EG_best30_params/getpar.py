# In future I will try to add adaptive sampling techniques , we can use observed spectra as loss function. 

import numpy as np

def getparspace(scen,phase,snum):
#Identification of scene
	scenb=True
	scena=False
	




# Now we try to set parameters depending on phase

#Phase 0: The paper shows the average time scale for phase0 is 	if phase=0.15Gyr
#While Ruta has varied the value over a range, we will check it after the first run

#Phase 3: Go through the paper to understand the lower limit for phase 3 and no variation 
#tau 3 included at this moment
	Bsrc=np.linspace(10,500,num=10)
	tauex0=np.linspace(0.005,0.020,num=4)
	if phase>2:
		lolim	=0.001
		uplim	=1.0
		deltex3	=np.linspace(lolim,uplim,num=snum)
	else:
		deltex3	=[0.55]	

	if phase > 2:
		lolim = -1
		uplim = -0.001
		step = 0.02
		tauex3 = np.linspace(lolim,uplim,num=snum)
	else:
		tauex3=[-0.11]

	if scenb==True:

		if phase>0:
			lolim	=0.001
			uplim	=0.2
			deltex1	=np.linspace(lolim,uplim,num=snum)
		else:
			deltex1	=[0.17]

		if phase >1:
			lolim	=0.001
			uplim	=1
			deltex2	=np.linspace(lolim,uplim,num=snum)
		else:
			deltex2=[1.0]	


			
				
		if phase==4:
			lolim 	=0.01
			uplim	=0.4
			deltex4	=np.linspace(lolim,uplim,num=snum)
		else:
			deltex4	=[0.3]

	print("No. of combinations required for each alphae:",len(tauex0)*len(deltex1)*len(deltex2)*len(deltex3)*len(tauex3)*len(deltex4)*len(Bsrc)) 
	




#To save the parameter space in parex.dat
	par	=open('parex.dat','w')
	par.write('tau0\t\tdelt1\t\tdelt2\t\tdelt3\t\ttau3\t\tdelt4\t\tBsrc\n')
	for bs in Bsrc:
		for i in tauex0:
			for j in deltex1:
				for k in deltex2:
					for l in deltex3:
						for m in tauex3:
							for n in deltex4:
								par.write(str(i)+'\t\t'+str(j)+'\t\t'+str(k)+'\t\t'+str(l)+'\t\t'+str(m)+'\t\t'+str(n)+'\t\t'+str(bs)+'\n')
	par.close()

	





		

		






	
	
		

	

