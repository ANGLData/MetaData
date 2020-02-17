#===============================================================================
# EXTRACTION SCRIPT argus_CO2blank_nochamber.py
#===============================================================================
'''
modifier: 01
eqtime: 15
'''

def main():
        
    ###########################################    
    # UA ANGL full analyitcal blank without Aux 2
    
    info('Argus VI Ar Extraction Script')
    
    #reset valving, pump prep/MS
    close('8') # MS inlet
    close('2') # Aux 2
    open('X') #Prepturbo
    close('1') # Prep ion
    open('9')  # MS ion
    open('3') # Aux 1
    close('4') # Pipette Ref Out
    close('5') # Pipette Ref In
    sleep(10)
    
    open('1') #Prep ion
    sleep(10)
    
    #close pumps
    close('1') #Prep ion
    close('X') #Prepturbo

    #laser fire
    
    #gas cleanup
    sleep(cleanup)
#===============================================================================
# EXTRACTION SCRIPT argus_CO2blank_nochamber.py
#===============================================================================

#===============================================================================
# POST EQUILIBRATION SCRIPT argus_pump_v1.py
#===============================================================================
def main():
    open('X') # Prep turbo
    open('3') # Aux 1
    open('2') # Aux 2
    sleep (300) 
    open('1') # Prep Ion Pump
    
#===============================================================================
# POST MEASUREMENT SCRIPT argus_pump_ms.py
#===============================================================================
def main():
    open('9') # MS Ion Pump