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

**python3 main_volumever1.py**

**_No requirement to modify internals of the code(user has to instantiate parameters on the fly)_**

_User has to specify the file containing spectra with extension_

_User has to specify on the go_ 
1. Guess Scenario
2. Guess Phase
3. Coarse or Fine search in parameter search
4. Search for probable injection index or specify value of injection index


(IF THE USER PREFERS DEFAULT OPTION , JUST PRESS ENTER)

## Output ##

The fit will be available as a plot with parameters specified on the terminal


