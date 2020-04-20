#===============================================================================
# EXTRACTION SCRIPT argus_pause.py
#===============================================================================
'''
modifier: 01
eqtime: 15
'''
def main():
        
    ###########################################    
    # UA ANGL Thermo Ar cocktail script (gettered air)
    
    info('Argus VI Ar Pause Script')
    
    sleep(cleanup)
    


    
    
        
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