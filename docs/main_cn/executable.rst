SeisFlows的 ``scripts/`` 目录下提供了若干可执行Python脚本。 由于环境变量中已经添加了该目录的位置，这些命令可以在任何目录下被执行。

 而 ``tests/`` 目录则提供了若干测试，如py模块导入、系统测试等. 在开始进行设计项目前，必须提前通过测试。

脚本
-------

- sfrun (sfsubmit): 提交任务脚本
--workdir          指定工作目录，默认为${pwd}
--parameter_file   指定 ``parameter.py`` 文件，默认为 ``./parameter.py``
--path_file        指定 ``path.py`` 文件，默认为 ``./path.py``

- plot2model: 绘制二进制模型文件的脚本
--nproc            并行核心数目
--coordir          指定二进制坐标文件目录， 默认为 ``../model_init``
--modeldir         指定二进制模型文件目录， 默认为 ``./``
--para             指定需要绘图的模型参数， 默认为 [\'vp\']

- ascii2bin: 将dat模型文件快速转换为SEM2D二进制模型文件的脚本
--nproc            并行核心数目
--dir              指定包含所有dat模型文件的目录， 默认为 ``./``

- sfclean: 删除目录下 **所有** 反演输出

- sfresume: 继续当前提交的工作. 参考 ``sfrun``.
- sfexample: 运行SeisFlows示例. **当前不可用**.

.. _tests:

测试
-----

- run_test_system: 测试并行环境
- run_test_import: 测试python模块导入
- run_test_optimize: 

    使用NBFGS和NLCG方法运行对 :math:`f_{Rosenbrock}=(1-x_1)^2+100(x_2-x_1^2)^2` 优化问题的求解

- run_test_preprocess: 测试包含reader, writer, filter, muting, misfit 和 adjoint在内的预处理模块
- run_test_tools: 测试其他python工具

