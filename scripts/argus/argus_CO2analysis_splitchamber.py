#===============================================================================
# EXTRACTION SCRIPT argus_CO2analysis_splitchamber.py
#===============================================================================
'''
eqtime: 15
'''

def main():
        
    ###########################################    
    # UA ANGL CO2 laser analysis splitting into laser chamber for large signals
    
    info('Argus VI Ar Extraction Script-SPLITTING')
    
    #reset valving, pump prep/MS
    close('8') # MS inlet
    open('X') #Prepturbo
    close('1') # Prep ion
    open('9')  # MS ion
    open('2') # Aux 2
    open('3') # Aux 1
    close('4') # Pipette Ref Out
    close('5') # Pipette Ref In
    sleep(10)
    
    open('1') #Prep ion
    sleep(10)
    
   
    
    
    # everything above this line is common to both an unknown and a blank analysis
    # =======================================
    if analysis_type=='blank':
        # this is run for blanks
        info('is blank. not heating')
        '''
        sleep cumulative time to account for blank
        during a multiple position analysis
        '''
        #close pumps
        close('1') #Prep ion
        close('X') #Prepturbo
        #close(description='Microbone to Turbo')
        numPositions=len(position)

        sleep(duration*max(1,numPositions))
    else:
        # this is run only for unknowns
        '''
        this is the most generic what to move and fire the laser
        position is always a list even if only one hole is specified
        '''
        info('enable laser')
        enable()
        for i,pi in enumerate(position):
            '''
            position the laser at pi, pi can be a holenumber or (x,y)
            '''
            sleep(2)
            move_to_position(pi, autocenter=True)
            sleep(2)
            
            if i==0:
                #close pumps
                close('1') #Prep ion
                close('X') #Prepturbo

            sleep(1)
            do_extraction()
            
            if disable_between_positions:
                end_extract()
        end_extract()
        disable()

    # this is common to blanks and unknowns
    #gas cleanup splitting sample gas, using chamber, pumping V1
    sleep(30)
    close('2')
    sleep(1)
    open('X')
    sleep(60)
    close('X')
    sleep(1)
    open('2')
    sleep(cleanup)


def do_extraction():

    info('begin interval')
    begin_interval(duration)
    if ramp_duration>0:
        info('ramping to {} at {} {}/s'.format(extract_value, ramp_rate, extract_units))
        ramp(setpoint=extract_value, duration=ramp_duration, period=0.5)
    else:
        info('set extract to {}, {}'.format(extract_value, extract_units))
        extract(extract_value, extract_units)
    #sleep(2)

    if pattern:
        info('executing pattern {}'.format(pattern))
        execute_pattern(pattern)

    complete_interval()
        
#===============================================================================
# EXTRACTION SCRIPT argus_CO2analysis.py
#===============================================================================

#===============================================================================
# POST EQUILIBRATION SCRIPT argus_pump_v1_1800_turbo.py
#===============================================================================
def main():
    open('X') # Prep turbo
    open('3') # Aux 1
    open('2') # Aux 2
    sleep (1800) 
    close('X') # Prep Turbo
    open('1') # Prep Ion Pump
    
#===============================================================================
# POST MEASUREMENT SCRIPT argus_pump_ms.py
#===============================================================================
def main():
    open('9') # MS Ion Pump