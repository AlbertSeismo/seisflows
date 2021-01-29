Seisflows provides several executable Python scripts in ``/path/to/seisflows/scripts``. As the PATH has already been added to environmental varibales, thereby can be executed in any directory.

Tests checking module importing, system, and optimization are also provided in ``/path/to/seisflows/tests``. It's recommmended to past these tests prior to other projects.

脚本
-------

- sfrun (sfsubmit): Workflow submission scripts.
--workdir          Working directory. ${pwd} is given by default.
--parameter_file   Path to ``parameter.py``. ``./parameter.py`` is given by default.
--path_file        Path to ``path.py``. ``./path.py`` is given by default.

- plot2model: A quick plotting script that combines all NPROC slice into one figure.
--nproc            Number of processors/slices.
--coordir          Path to coordinate model. ``../model_init`` is given by default.
--modeldir         Path to binary model slice. ``./`` is given by defualt.
--para             Parameters to plot. [\'vp\'] is given by default.

- ascii2bin: A quick script converting all ascii model to binary slice for SPECFEM.
--nproc            Number of processors/slices.
--dir              PATH to directory containing all .dat/ascii files. ``./`` is given by default.

- sfclean: Delete directories output, output.stat, output.optim
  and scratch in the current directory
- sfresume: Resume current submitted workflow. See ``sfrun``.
- sfexample: Run seisflows example. **Currently not available**.

测试
-----

- run_test_system: Testing parallelizaiton environment.
- run_test_import: Testing seisflows module importing.
- run_test_optimize: 

    Program will run a non-linear optimization for :math:`f_{Rosenbrock}=(1-x_1)^2+100(x_2-x_1^2)^2` with LBFGS and NLCG method. 

- run_test_preprocess: Testing preprocess including reader, writer, filter, muting, misfit and adjoint.
- run_test_tools: Testing other Python tools.

