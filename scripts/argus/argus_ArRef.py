#===============================================================================
# EXTRACTION SCRIPT argus_ArRef.py
#===============================================================================
'''
modifier: 01
eqtime: 20
'''
def main():
        
    ###########################################    
    # UA ANGL Thermo Ar cocktail script (gettered air)
    
    info('Argus VI Ar Extraction Script')
    
    #reset valving, pump prep/MS
    close('8') # MS inlet
    open('1')  # Prep ion
    open('9')  # MS ion
    close('2') # Aux 1
    close('3') # Aux 2
    close('4') # Pipette Ref Out
    close('5') # Pipette Ref In
    
    pipette_fill_duration = 15
    if analysis_type=='blank': #only relavent to extraction scripts
        info('doing blank. not filling pipette')
        sleep(pipette_fill_duration)
    else:
        info('filling pipette')
        open('5') #Pipette Ref Out
        sleep(pipette_fill_duration)
        close('5')
        open('4') #Pipette Ref In
    
    # isolate V1
    close('1')
    
    #load pipette into V1
    open('4')
    sleep(30)

    
    
        
#===============================================================================
# POST EQUILIBRATION SCRIPT argus_pump_v1.py
#===============================================================================
def main():
    open('X') # Prep turbo
    open('3') # Aux 1
    sleep (60) 
    close('X')# Prep turbo
    sleep (2)
    open('1') # Prep Ion Pump
    
#===============================================================================
# POST MEASUREMENT SCRIPT argus_pump_ms.py
#===============================================================================
def main():
    open('9') # MS Ion Pump