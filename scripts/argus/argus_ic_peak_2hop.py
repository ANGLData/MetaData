#!Measurement
'''
'''
#counts

#baselines
BASELINE_COUNTS= 75
BASELINE_DETECTOR= 'H1'
BASELINE_MASS= 34.2
BASELINE_BEFORE= False
BASELINE_AFTER= True
BASELINE_SETTLING_TIME= 15

#equilibration
EQ_TIME= eqtime
INLET= '8'
OUTLET= '9'
EQ_DELAY= 3.0

ACTIVE_DETECTORS = ('H2','H1', 'AX', 'L1', 'L2', 'CDD')

FITS =('Ar40:parabolic',
       'Ar39:linear',
       'Ar38:linear',
       'Ar37:linear',
       'Ar36:linear',
       'Ar40H1:parabolic',
       'Ar39AX:linear',
       'Ar38L1:linear',
       'Ar37L2:linear',
       'Ar36L2:linear')


BASELINE_FITS=(('average', 'SEM'),)

NCYCLES=20
GENERATE_ICMFTABLE=False


def main():
    info('unknown measurement script')

    # protect the CDD
    
    activate_detectors(*ACTIVE_DETECTORS)
    
    #position_magnet('Ar40', 'H2')
    
    hops=load_hops('hops/ic_2hops.yaml')
    info(hops)
    define_hops(hops)
    '''
    Equilibrate is non-blocking so use a sniff or sleep as a placeholder
    e.g sniff(<equilibration_time>) or sleep(<equilibration_time>)
    '''
    equilibrate(eqtime=EQ_TIME, inlet=INLET, outlet=OUTLET, delay=EQ_DELAY)
    set_time_zero()

    #sniff the gas during equilibration
    #sniff(EQ_TIME)
    sleep(EQ_TIME)
    set_fits(*FITS)
    set_baseline_fits(*BASELINE_FITS)

    sleep(0.5)
    
    peak_hop(ncycles=NCYCLES, hops=hops, mftable='mftable')
    

    if BASELINE_AFTER:
        #necessary if peak hopping
        define_detectors('Ar41','H2')
        define_detectors('Ar40','H1')
        define_detectors('Ar39','AX')
        define_detectors('Ar38','L1')
        define_detectors('Ar37','L2')
        define_detectors('Ar36','CDD')
      
        baselines(ncounts=BASELINE_COUNTS,mass=BASELINE_MASS, detector=BASELINE_DETECTOR,
                  settling_time=BASELINE_SETTLING_TIME)

    activate_detectors(*('H1',), **{'peak_center':True})
    peak_center(detector='H1',isotope='Ar40', config_name='H1_40_Only')

    info('finished measure script')
