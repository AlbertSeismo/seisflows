
WORKFLOW='inversion'    # inversion, migration
SOLVER='specfem2d'      # specfem2d, specfem3d
SYSTEM='serial'       # serial, pbs, slurm
OPTIMIZE='NLCG'        # LBFGS, NLCG, steepest_descent
PREPROCESS='base'       # base
POSTPROCESS='base'      # base

MISFIT='Waveform'       #Waveform, Envelope, InstantaneousPhase, Traveltime, TraveltimeInexact, Amplitude. See seisflows.plugins.misfit
MATERIALS='Elastic'     #Elastic, 
DENSITY='Constant'
VP='Variable'
VS='Constant'
MINUSGRADIENT=0


# WORKFLOW
BEGIN=16                 # first iteration
END=20                   # last iteration
NREC=81                  # number of receivers
NSRC=15                 # number of sources
SAVEGRADIENT=1          # save gradient how often


# PREPROCESSING
FORMAT='su'             # data file format
CHANNELS='z'            # data channels
NORMALIZE='NormalizeTracesL1'             # normalize
BANDPASS=0              # bandpass
FILTER='Bandpass'
FREQMIN=60.               # low frequency corner
FREQMAX=100.               # high frequency corner



# POSTPROCESSING
SMOOTH=1               # smoothing radius
#SCALE=6.0e6             # scaling factor


# OPTIMIZATION
PRECOND=None            # preconditioner type
STEPMAX=10              # maximum trial steps
#STEPTHRESH=0.1          # step length safeguard


# SOLVER
NT=25000                 # number of time steps
DT=0.00002                 # time step
F0=50                 # dominant frequency

# SYSTEM
NTASK=15                # must satisfy 1 <= NTASK <= NSRC
NPROC=3                 # processors per task
MPIEXEC='mpirun -np 3 '

