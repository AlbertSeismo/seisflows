安装
============

首先从GitHhub下载Seisflows代码::

    git clone https://github.com/rmodrak/seisflows.git


设置环境变量。 将以下代码加入 ``.bashrc`` (如果使用其他shell，相应地改变)::

    export PATH=$PATH:/path/to/seisflows/scripts
    export PYTHONPATH=$PYTHONPATH:/path/to/seisflows


依赖软件
======================

SeisFlows需要Python 2.7以及相应的Numpy、Scipy和Obspy库支持。运行SeisFlows前需要提前安装这些库。

正演程序需要提前编译，参考 :ref:`solver`。


硬件要求
======================

Access to a computer cluster is required for most applications.  Base classes are provided for several common cluster configurations, including PBS and SLURM.  Nonstandard configurations can often be accommodated through modifications to one of the base classes; see :ref:`system` for details.


.. _submission:

任务提交
==============

Each job must have it own `working directory` within which users must supply two input files, ``paths.py`` and ``parameters.py``.

To begin executing a workflow, simply type ``sfrun`` within a working directory. If an ``inversion`` workflow and ``serial`` system configuration, for example, are specified in the parameters file, the inversion will begin executing immediately in serial. If a PBS, SLURM, or LSF system configuration is specified instead, execution may wait until required resources become available.

Once the workflow starts running, status information is displayed to the terminal or to the file ``output.log``.  By default, updated models and other inversion results are output to the working directory.


.. _solver:

正演程序配置
====================

SeisFlows includes Python interfaces for SPECFEM2D, SPECFEM3D, and SPECFEM3D_GLOBE.  While the Python interfaces are part of the SeisFlows package, the solver source code must be downloaded separately through GitHub.  

After downloading the solver source code, users must configure and compile it, following the instructions in the solver user manual. Summarized briefly, the configuration and compilation procedure is:

Prior to compilation, users need to run the ``configure`` script and prepare input files such as

- parameter file

- source file

- stations file.

To successfully run the ``configure``, you may need to install compilers, libraries, and other software in your environment.

The result of compilation is a set of binary executables, such as

- mesher

- solver

- smoothing utility

- summing utility.


After compilation, solver input files must be gathered together in one directory and solver executables in another.  The absolute paths to the directories containing input files and executables must be given in ``paths.py``.


.. _developer:


开发参考
===================

To allow classes to work with one another, each must conform to an established interface.  This means certain classes must implement certain methods, with specified input and output.  Required methods include

- ``setup`` methods are generic methods, called from the ``main`` workflow script and meant to provide users the flexibility to perform any required setup tasks. 

- ``check`` methods are the default mechanism for parameter declaration and checking and are called just once, prior to a job being submitted through the scheduler.

Besides required methods, classes may include any number of private methods or utility functions.