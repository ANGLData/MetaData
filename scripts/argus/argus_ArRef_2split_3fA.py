#===============================================================================
# EXTRACTION SCRIPT argus_ArRef_2split_3fA.py
#===============================================================================
'''
modifier: 01
eqtime: 15
'''
def main():
        
    ###########################################    
    # UA ANGL Thermo Ar cocktail script (gettered air)
    # should be 3fA on the CDD
    
    info('Argus VI Ar Extraction Script')
    
    #reset valving, pump prep/MS/pippette
    close('8') # MS inlet
    close('5') # Pipette Ref In
    open('1')  # Prep ion
    open('9')  # MS ion
    open('3')  # Aux 1
    open('2')  # Aux 2
    open('4')  # Pipette Ref Out
    sleep(30)
    close('4') # Pipette Ref Out
    sleep(1)
    
    
    pipette_fill_duration = 15
    if analysis_type=='blank': #only relavent to extraction scripts
        info('doing blank. not filling pipette')
        sleep(pipette_fill_duration)
    else:
        info('filling pipette')
        open('5') #Pipette Ref Out
        sleep(pipette_fill_duration)
        close('5')
        
    #isolate V1
    close('1')
    sleep(1)
   
    #load pipette into V1
    open('4')
    sleep(30)
    close('4')
    
    #first split into Aux 2 stage-------------SPLIT 1
    close('2')
    sleep(1)
    open('X')
    sleep(60)
    close('X')
    sleep(1)
    
    #expand Aux 1 into V1
    open('2')
    sleep(30)
    
    #second split into Aux 2 stage-----------SPLIT 2
    close('2')
    sleep(1)
    open('X')
    sleep(60)
    close('X')
    sleep(1)
    
    #expand split into V1
    open('2')
    sleep(30)
    
    #third split into Aux 2 stage-----------SPLIT 2
    close('2')
    sleep(1)
    open('X')
    sleep(60)
    close('X')
    sleep(1)
    
    #expand split into V1
    open('2')
    sleep(30)


    
    
        
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