安装
============

首先从GitHub下载Seisflows代码::

    $ git clone https://github.com/rmodrak/seisflows.git


设置环境变量。 将以下代码加入 ``.bashrc`` (如果使用其他shell，相应地改变)::

    $ export PATH=$PATH:/path/to/seisflows/scripts
    $ export PYTHONPATH=$PYTHONPATH:/path/to/seisflows

根据SeisFlow的位置，``/path/to/seisflows/scripts`` 与 ``/path/to/seisflows`` 需要进行对应的调整。重新登陆，或使用::

    $ source ~/.bashrc

应用环境变量更改。应用后，请确保SeisFlow目录不再发生移动。

依赖软件
======================

SeisFlows需要Python 2.7以及相应的NumPy、SciPy和ObsPy库支持。运行SeisFlows前需要提前安装这些库。SeisFlows提供了若干程序测试，为确保其所需的依赖库能正常运行，这些测试必须通过，参见 :ref:`tests`

正演程序需要提前编译，参考 :ref:`solver`。


.. _submission:

任务提交
==============

每一个SeisFlows的任务需要有其独立的目录，目录下必须有用户参数输入文档``paths.py`` 和 ``parameters.py`` 。在命令行该目录下输入 ``sfrun`` 即可开始执行一个任务。

.. _solver:

正演程序配置
====================

SeisFlows包含为SPECFEM2D/3D/3D_GLOBE提供的python接口，而SEM的源代码则必须额外下载。  

首先，应当运行configure命令配置合适的Makefile。以下命令指定gfortran和gcc分别作为fortran和c的编译器，并提供mpi支持::

    $ ./configure FC=gfortran CC=gcc --with-mpi

如果采用mpi，请确认mpif90命令调用与FC对应的编译器::

    $ mpif90 --version       
    GNU Fortran (Homebrew GCC 10.2.0) 10.2.0
    Copyright (C) 2020 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

否则，请先将mpi调用进行变更::

        $ export OMPI_FC=gfortran

configure输出以下内容则成功::

    ## ---------------- ##
    ## Specfem 2D 7.0.0 ##
    ## ---------------- ##

    ./configure has completed and set up a default configuration to build.

    You may wish to modify the following files before running a simulation:
    DATA/Par_file           Set parameters affecting the simulation.
    DATA/SOURCE             Set the source parameters before running the solver.

编译specfem2d主程序::

    $ make all -j 10   

完成编译后，检查检查程序编译是否成功::

    $ ls ./bin/                           
    xadj_seismogram               xcombine_sem                  xmeshfem2D                    xspecfem2D
    xcheck_quality_external_mesh  xconvolve_source_timefunction xsmooth_sem                   xsum_kernels


.. _developer:


开发参考
===================

To allow classes to work with one another, each must conform to an established interface.  This means certain classes must implement certain methods, with specified input and output.  Required methods include

- ``setup`` methods are generic methods, called from the ``main`` workflow script and meant to provide users the flexibility to perform any required setup tasks. 

- ``check`` methods are the default mechanism for parameter declaration and checking and are called just once, prior to a job being submitted through the scheduler.

Besides required methods, classes may include any number of private methods or utility functions.