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

ACTIVE_DETECTORS = ('H2','H1')
FITS = ('Ar40H2:parabolic','Ar40H1:parabolic')
BASELINE_FITS=('average_SEM',)

NCYCLES=6
GENERATE_ICMFTABLE=False

def main():
    info('unknown measurement script')

    # protect the CDD
    set_deflection('CDD', 2000)
    activate_detectors(*ACTIVE_DETECTORS)

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
    #sniff(EQ_TIME-1)
    sleep(EQ_TIME-1)
    set_fits(*FITS)
    set_baseline_fits(*BASELINE_FITS)

    sleep(0.5)
    
    mftable_name = 'mftable'
    #if GENERATE_ICMFTABLE:
    #    mftable_name = 'ic_mftable'
    #    generate_ic_mftable(('H1','H2'), peak_center_config='ic_2hops')
    #    set_time_zero()

    peak_hop(ncycles=NCYCLES, hops=hops, mftable=mftable_name)


    if BASELINE_AFTER:
        #necessary if peak hopping
        define_detectors('Ar40','H2')
        define_detectors('Ar40','H1')
      
        baselines(ncounts=BASELINE_COUNTS,mass=BASELINE_MASS, detector=BASELINE_DETECTOR,
                  settling_time=BASELINE_SETTLING_TIME)

    # unprotect CDD
    set_deflection('CDD', 50)

    info('finished measure script')
