EG code: Only gives the best fit

******* Parameters may be unphysical for the best fit****************

##  Files containing the EG Code ##
main.py : Main code to run calls functions from different python files and results in best fit parameters and the best fit plot

operation.py  : Contains all primary functions involved in running main.py returns luminosity and corresponding chi value fir a set of parameters

getpar        : Instances variables like magnetic field , del_t and tau

## Files User has to supply ##
source.py     : Instances source properties of redshift and Volume (as the equipartition over estimated the magnetic field, hence source magnetic field is a variable instantiated in getpar.py)


"Observation".py: Instances the spectra observed for the source ["Name of the observation file can be instantiated at the time of run"]

## To run the code ##
python3 main.py

User has to specify the file containing spectra with extension

User has the choice of selecting on the go 
1. Scenario
2. Phase
3. Coarse or Fine search in parameter search
4. Search for probable injection index OR the user has to specify value of injection index

(IF THE USER PREFERS DEFAULT OPTION , JUST PRESS ENTER)


