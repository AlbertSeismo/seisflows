Seisflows provides several executable Python scripts in ``/path/to/seisflows/scripts``. As the PATH has already been added to environmental varibales, thereby can be executed in any directory.

Tests checking module importing, system, and optimization are also provided in ``/path/to/seisflows/tests``. It's recommmended to past these tests prior to other projects.

Scripts
-------

- sfrun (sfsubmit): Workflow submission scripts.
- plotgll: Plots GLL model read from SPECFEM2D Fortran binary file
- sfclean: Delete directories output, output.stat, output.optim
  and scratch in the current directory
- sfresume: Resume current submitted workflow.
- sfexample: Run seisflows example. **Currently not available**.

Tests
-----

- run_test_system: Test parallelizaiton environment.
- run_test_import: Testing seisflows module importing.
- run_test_optimize: 
- run_test_preprocess:
- run_test_tools:

