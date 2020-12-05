#
# This is Seisflows
#
# See LICENCE file
#
###############################################################################

# Import system modules
import sys
from getpass import getuser
from os.path import abspath, exists
from uuid import uuid4

# Local imports
from seisflows.tools import unix
from seisflows.config import ParameterError, custom_import

try:
    PAR = sys.modules['seisflows_parameters']
    PATH = sys.modules['seisflows_paths']
except:
    print("Check parameters and paths.")


class tiger_sm(custom_import('system', 'slurm_sm')):
    """ Specially designed system interface for tiger.princeton.edu

      See parent class for more information.
    """

    def check(self):
        """ Checks parameters and paths
        """
        # where job was submitted
        if 'WORKDIR' not in PATH:
            setattr(PATH, 'WORKDIR', abspath('.'))

        # where temporary files are written
        if 'SCRATCH' not in PATH:
            setattr(PATH, 'SCRATCH', PATH.WORKDIR+'/'+'scratch')

        super(tiger_sm, self).check()

    def submit(self, *args, **kwargs):
        """ Submits job
        """
        if not exists(PATH.SCRATCH):
            path = '/scratch/gpfs' + '/' + getuser() + '/' + 'seisflows' + '/'\
                   + str(uuid4())
            unix.mkdir(path)
            unix.ln(path, PATH.SCRATCH)

        super(tiger_sm, self).submit(*args, **kwargs)
