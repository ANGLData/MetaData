#===============================================================================
# EXTRACTION SCRIPT argus_CO2blank_nochamber+noIon.py
#===============================================================================
'''
modifier: 01
eqtime: 15
'''

def main():
        
    ###########################################    
    # UA ANGL full analyitcal blank without Ion pump or laser chamber
    
    info('Argus VI Ar Extraction Script')
    
    #reset valving, pump prep/MS
    close('1') # Prep ion
    close('8') # MS inlet
    open('X') #Prepturbo
    open('9') # MS ion
    open('3') # Aux 1
    close ('2') # Aux 2
    sleep(10)
    
    #close pumps
    close('X') #Prepturbo

    #laser fire
    
    #gas cleanup
    sleep(cleanup)
#===============================================================================
# EXTRACTION SCRIPT argus_CO2blank_nochamber.py
#===============================================================================

#===============================================================================
# POST EQUILIBRATION SCRIPT argus_pump_v1_ion only.py
#===============================================================================
def main():
    open('3') # Aux 1
    open('1') # Prep Ion Pump
    
#===============================================================================
# POST MEASUREMENT SCRIPT argus_pump_ms.py
#===============================================================================
def main():
    open('9') # MS Ion Pump