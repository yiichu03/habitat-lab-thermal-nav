Your user’s .npmrc file (${HOME}/.npmrc)
has a `globalconfig` and/or a `prefix` setting, which are incompatible with nvm.
Run `nvm use --delete-prefix v22.21.0 --silent` to unset it.
(base) liuyi@liuyi:~/projects/habitat_challenge$ git clone https://github.com/facebookresearch/habitat-challenge.git
cd habitat-challenge
Cloning into 'habitat-challenge'...
remote: Enumerating objects: 1257, done.
remote: Counting objects: 100% (1257/1257), done.
remote: Compressing objects: 100% (481/481), done.
remote: Total 1257 (delta 720), reused 1220 (delta 711), pack-reused 0 (from 0)
Receiving objects: 100% (1257/1257), 46.25 MiB | 17.53 MiB/s, done.
Resolving deltas: 100% (720/720), done.
(base) liuyi@liuyi:~/projects/habitat_challenge/habitat-challenge$ conda create -n habitat python=3.7
conda activate habitat
Retrieving notices: done
WARNING: A conda environment already exists at '/home/liuyi/miniforge3/envs/habitat'

Remove existing environment?
This will remove ALL directories contained within this specified prefix directory, including any other conda environments.

 (y/[n])? y^C
CondaSystemExit: 
Operation aborted.  Exiting.

(habitat) liuyi@liuyi:~/projects/habitat_challenge/habitat-challenge$ conda activate habitat_challenge

EnvironmentNameNotFound: Could not find conda environment: habitat_challenge
You can list all discoverable environments with `conda info --envs`.


(habitat) liuyi@liuyi:~/projects/habitat_challenge/habitat-challenge$ conda create -n habitat_challenge python=3.7
Retrieving notices: done
Channels:
 - conda-forge
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
    current version: 25.11.0
    latest version: 26.1.0

Please update conda by running

    $ conda update -n base -c conda-forge conda



## Package Plan ##

  environment location: /home/liuyi/miniforge3/envs/habitat_challenge

  added / updated specs:
    - python=3.7


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    libffi-3.4.6               |       h2dba641_1          56 KB  conda-forge
    pip-24.0                   |     pyhd8ed1ab_0         1.3 MB  conda-forge
    python-3.7.12              |hf930737_100_cpython        57.3 MB  conda-forge
    setuptools-69.0.3          |     pyhd8ed1ab_0         460 KB  conda-forge
    sqlite-3.51.2              |       h04a0ce9_0         179 KB  conda-forge
    wheel-0.42.0               |     pyhd8ed1ab_0          56 KB  conda-forge
    ------------------------------------------------------------
                                           Total:        59.4 MB

The following NEW packages will be INSTALLED:

  _libgcc_mutex      conda-forge/linux-64::_libgcc_mutex-0.1-conda_forge 
  _openmp_mutex      conda-forge/linux-64::_openmp_mutex-4.5-2_gnu 
  ca-certificates    conda-forge/noarch::ca-certificates-2026.1.4-hbd8a1cb_0 
  icu                conda-forge/linux-64::icu-78.2-h33c6efd_0 
  ld_impl_linux-64   conda-forge/linux-64::ld_impl_linux-64-2.45.1-default_hbd61a6d_101 
  libffi             conda-forge/linux-64::libffi-3.4.6-h2dba641_1 
  libgcc             conda-forge/linux-64::libgcc-15.2.0-he0feb66_17 
  libgcc-ng          conda-forge/linux-64::libgcc-ng-15.2.0-h69a702a_17 
  libgomp            conda-forge/linux-64::libgomp-15.2.0-he0feb66_17 
  liblzma            conda-forge/linux-64::liblzma-5.8.2-hb03c661_0 
  liblzma-devel      conda-forge/linux-64::liblzma-devel-5.8.2-hb03c661_0 
  libnsl             conda-forge/linux-64::libnsl-2.0.1-hb9d3cd8_1 
  libsqlite          conda-forge/linux-64::libsqlite-3.51.2-hf4e2dac_0 
  libstdcxx          conda-forge/linux-64::libstdcxx-15.2.0-h934c35e_17 
  libstdcxx-ng       conda-forge/linux-64::libstdcxx-ng-15.2.0-hdf11a46_17 
  libzlib            conda-forge/linux-64::libzlib-1.3.1-hb9d3cd8_2 
  ncurses            conda-forge/linux-64::ncurses-6.5-h2d0b736_3 
  openssl            conda-forge/linux-64::openssl-3.6.1-h35e630c_1 
  pip                conda-forge/noarch::pip-24.0-pyhd8ed1ab_0 
  python             conda-forge/linux-64::python-3.7.12-hf930737_100_cpython 
  readline           conda-forge/linux-64::readline-8.3-h853b02a_0 
  setuptools         conda-forge/noarch::setuptools-69.0.3-pyhd8ed1ab_0 
  sqlite             conda-forge/linux-64::sqlite-3.51.2-h04a0ce9_0 
  tk                 conda-forge/linux-64::tk-8.6.13-noxft_h366c992_103 
  wheel              conda-forge/noarch::wheel-0.42.0-pyhd8ed1ab_0 
  xz                 conda-forge/linux-64::xz-5.8.2-ha02ee65_0 
  xz-gpl-tools       conda-forge/linux-64::xz-gpl-tools-5.8.2-ha02ee65_0 
  xz-tools           conda-forge/linux-64::xz-tools-5.8.2-hb03c661_0 
  zstd               conda-forge/linux-64::zstd-1.5.7-hb78ec9c_6 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
                                                                                
Preparing transaction: done                                                     
Verifying transaction: done                                                     
Executing transaction: done                                                     
#                                                                               
# To activate this environment, use                                             
#
#     $ conda activate habitat_challenge
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(habitat) liuyi@liuyi:~/projects/habitat_challenge/habitat-challenge$ conda activate habitat_challenge
(habitat_challenge) liuyi@liuyi:~/projects/habitat_challenge/habitat-challenge$ conda install -c aihabitat habitat-sim-challenge-2023
git clone --branch challenge-2023 https://github.com/facebookresearch/habitat-lab.git
cd habitat-lab
pip install -r requirements.txt
python setup.py develop
Channels:
 - aihabitat
 - conda-forge
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
    current version: 25.11.0
    latest version: 26.1.0

Please update conda by running

    $ conda update -n base -c conda-forge conda



## Package Plan ##

  environment location: /home/liuyi/miniforge3/envs/habitat_challenge

  added / updated specs:
    - habitat-sim-challenge-2023


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    attrs-24.2.0               |     pyh71513ae_0          55 KB  conda-forge
    certifi-2024.8.30          |     pyhd8ed1ab_0         160 KB  conda-forge
    colorama-0.4.6             |     pyhd8ed1ab_0          25 KB  conda-forge
    cycler-0.11.0              |     pyhd8ed1ab_0          10 KB  conda-forge
    gitdb-4.0.11               |     pyhd8ed1ab_0          52 KB  conda-forge
    gitpython-3.1.43           |     pyhd8ed1ab_0         153 KB  conda-forge
    habitat-sim-challenge-2023-0.2.3|py3.7_linux_584ef238b9c505e91598a37a15247e52d21782c9       271.1 MB  aihabitat
    habitat-sim-mutex-1.0      | display_nobullet           3 KB  aihabitat
    imageio-2.36.0             |     pyh12aca89_1         285 KB  conda-forge
    imageio-ffmpeg-0.5.1       |     pyhd8ed1ab_0          20 KB  conda-forge
    importlib-metadata-4.11.4  |   py37h89c1867_0          33 KB  conda-forge
    kiwisolver-1.4.4           |   py37h7cecad7_0          73 KB  conda-forge
    lcms2-2.14                 |       h6ed2654_0         256 KB  conda-forge
    libdeflate-1.14            |       h166bdaf_0          81 KB  conda-forge
    libpng-1.6.55              |       h421ea60_0         310 KB  conda-forge
    libtiff-4.4.0              |       h82bc61c_5         473 KB  conda-forge
    libxcb-1.13                |    h7f98852_1004         391 KB  conda-forge
    llvmlite-0.39.1            |   py37h0761922_0         2.5 MB  conda-forge
    matplotlib-base-3.3.2      |   py37h4f6019d_1         6.7 MB  conda-forge
    numba-0.56.3               |   py37hf081915_0         4.0 MB  conda-forge
    numpy-1.21.6               |   py37h976b520_0         6.1 MB  conda-forge
    openjpeg-2.5.0             |       h7d73246_1         533 KB  conda-forge
    pillow-9.2.0               |   py37h850a105_2        45.0 MB  conda-forge
    pyparsing-3.1.4            |     pyhd8ed1ab_0          88 KB  conda-forge
    python-dateutil-2.9.0      |     pyhd8ed1ab_0         218 KB  conda-forge
    python_abi-3.7             |          4_cp37m           6 KB  conda-forge
    quaternion-2022.4.1        |   py37h540881e_0          92 KB  conda-forge
    scipy-1.7.3                |   py37hf2a6cf1_0        21.8 MB  conda-forge
    six-1.16.0                 |     pyh6c4a22f_0          14 KB  conda-forge
    tk-8.6.13                  |noxft_hd72426e_102         3.1 MB  conda-forge
    tornado-6.2                |   py37h540881e_0         651 KB  conda-forge
    tqdm-4.67.1                |     pyhd8ed1ab_0          87 KB  conda-forge
    typing-extensions-4.7.1    |       hd8ed1ab_0          10 KB  conda-forge
    typing_extensions-4.7.1    |     pyha770c72_0          35 KB  conda-forge
    xorg-fixesproto-5.0        |    hb9d3cd8_1003          11 KB  conda-forge
    xorg-inputproto-2.3.2      |    hb9d3cd8_1003          22 KB  conda-forge
    xorg-kbproto-1.0.7         |    hb9d3cd8_1003          30 KB  conda-forge
    xorg-libx11-1.8.4          |       h0b41bf4_0         810 KB  conda-forge
    xorg-libxcursor-1.2.0      |       h0b41bf4_1          31 KB  conda-forge
    xorg-libxext-1.3.4         |       h0b41bf4_2          49 KB  conda-forge
    xorg-libxfixes-5.0.3       |    h7f98852_1004          18 KB  conda-forge
    xorg-libxi-1.7.10          |       h7f98852_0          46 KB  conda-forge
    xorg-libxinerama-1.1.5     |       h27087fc_0          13 KB  conda-forge
    xorg-libxrandr-1.5.2       |       h7f98852_1          29 KB  conda-forge
    xorg-libxrender-0.9.10     |    h7f98852_1003          32 KB  conda-forge
    xorg-randrproto-1.5.0      |    hb9d3cd8_1002          35 KB  conda-forge
    xorg-renderproto-0.11.1    |    hb9d3cd8_1003          12 KB  conda-forge
    xorg-xextproto-7.3.0       |    hb9d3cd8_1004          30 KB  conda-forge
    xorg-xproto-7.0.31         |    hb9d3cd8_1008          72 KB  conda-forge
    zipp-3.15.0                |     pyhd8ed1ab_0          17 KB  conda-forge
    ------------------------------------------------------------
                                           Total:       365.5 MB

The following NEW packages will be INSTALLED:

  attrs              conda-forge/noarch::attrs-24.2.0-pyh71513ae_0 
  certifi            conda-forge/noarch::certifi-2024.8.30-pyhd8ed1ab_0 
  colorama           conda-forge/noarch::colorama-0.4.6-pyhd8ed1ab_0 
  cycler             conda-forge/noarch::cycler-0.11.0-pyhd8ed1ab_0 
  ffmpeg             conda-forge/linux-64::ffmpeg-2.8.6-0 
  freetype           conda-forge/linux-64::freetype-2.14.1-ha770c72_0 
  gitdb              conda-forge/noarch::gitdb-4.0.11-pyhd8ed1ab_0 
  gitpython          conda-forge/noarch::gitpython-3.1.43-pyhd8ed1ab_0 
  habitat-sim-chall~ aihabitat/linux-64::habitat-sim-challenge-2023-0.2.3-py3.7_linux_584ef238b9c505e91598a37a15247e52d21782c9 
  habitat-sim-mutex  aihabitat/noarch::habitat-sim-mutex-1.0-display_nobullet 
  imageio            conda-forge/noarch::imageio-2.36.0-pyh12aca89_1 
  imageio-ffmpeg     conda-forge/noarch::imageio-ffmpeg-0.5.1-pyhd8ed1ab_0 
  importlib-metadata conda-forge/linux-64::importlib-metadata-4.11.4-py37h89c1867_0 
  jpeg               conda-forge/linux-64::jpeg-9e-h0b41bf4_3 
  kiwisolver         conda-forge/linux-64::kiwisolver-1.4.4-py37h7cecad7_0 
  lcms2              conda-forge/linux-64::lcms2-2.14-h6ed2654_0 
  lerc               conda-forge/linux-64::lerc-4.0.0-h0aef613_1 
  libblas            conda-forge/linux-64::libblas-3.9.0-20_linux64_openblas 
  libcblas           conda-forge/linux-64::libcblas-3.9.0-20_linux64_openblas 
  libdeflate         conda-forge/linux-64::libdeflate-1.14-h166bdaf_0 
  libfreetype        conda-forge/linux-64::libfreetype-2.14.1-ha770c72_0 
  libfreetype6       conda-forge/linux-64::libfreetype6-2.14.1-h73754d4_0 
  libgfortran        conda-forge/linux-64::libgfortran-15.2.0-h69a702a_17 
  libgfortran-ng     conda-forge/linux-64::libgfortran-ng-15.2.0-h69a702a_17 
  libgfortran5       conda-forge/linux-64::libgfortran5-15.2.0-h68bc16d_17 
  liblapack          conda-forge/linux-64::liblapack-3.9.0-20_linux64_openblas 
  libllvm11          conda-forge/linux-64::libllvm11-11.1.0-he0ac6c6_5 
  libopenblas        conda-forge/linux-64::libopenblas-0.3.25-pthreads_h413a1c8_0 
  libpng             conda-forge/linux-64::libpng-1.6.55-h421ea60_0 
  libtiff            conda-forge/linux-64::libtiff-4.4.0-h82bc61c_5 
  libwebp-base       conda-forge/linux-64::libwebp-base-1.6.0-hd42ef1d_0 
  libxcb             conda-forge/linux-64::libxcb-1.13-h7f98852_1004 
  llvmlite           conda-forge/linux-64::llvmlite-0.39.1-py37h0761922_0 
  matplotlib         conda-forge/linux-64::matplotlib-3.3.2-0 
  matplotlib-base    conda-forge/linux-64::matplotlib-base-3.3.2-py37h4f6019d_1 
  numba              conda-forge/linux-64::numba-0.56.3-py37hf081915_0 
  numpy              conda-forge/linux-64::numpy-1.21.6-py37h976b520_0 
  openjpeg           conda-forge/linux-64::openjpeg-2.5.0-h7d73246_1 
  pillow             conda-forge/linux-64::pillow-9.2.0-py37h850a105_2 
  pthread-stubs      conda-forge/linux-64::pthread-stubs-0.4-hb9d3cd8_1002 
  pyparsing          conda-forge/noarch::pyparsing-3.1.4-pyhd8ed1ab_0 
  python-dateutil    conda-forge/noarch::python-dateutil-2.9.0-pyhd8ed1ab_0 
  python_abi         conda-forge/linux-64::python_abi-3.7-4_cp37m 
  quaternion         conda-forge/linux-64::quaternion-2022.4.1-py37h540881e_0 
  scipy              conda-forge/linux-64::scipy-1.7.3-py37hf2a6cf1_0 
  six                conda-forge/noarch::six-1.16.0-pyh6c4a22f_0 
  smmap              conda-forge/noarch::smmap-3.0.5-pyh44b312d_0 
  tornado            conda-forge/linux-64::tornado-6.2-py37h540881e_0 
  tqdm               conda-forge/noarch::tqdm-4.67.1-pyhd8ed1ab_0 
  typing-extensions  conda-forge/noarch::typing-extensions-4.7.1-hd8ed1ab_0 
  typing_extensions  conda-forge/noarch::typing_extensions-4.7.1-pyha770c72_0 
  x264               conda-forge/linux-64::x264-1!164.3095-h166bdaf_2 
  xorg-fixesproto    conda-forge/linux-64::xorg-fixesproto-5.0-hb9d3cd8_1003 
  xorg-inputproto    conda-forge/linux-64::xorg-inputproto-2.3.2-hb9d3cd8_1003 
  xorg-kbproto       conda-forge/linux-64::xorg-kbproto-1.0.7-hb9d3cd8_1003 
  xorg-libx11        conda-forge/linux-64::xorg-libx11-1.8.4-h0b41bf4_0 
  xorg-libxau        conda-forge/linux-64::xorg-libxau-1.0.12-hb03c661_1 
  xorg-libxcursor    conda-forge/linux-64::xorg-libxcursor-1.2.0-h0b41bf4_1 
  xorg-libxdmcp      conda-forge/linux-64::xorg-libxdmcp-1.1.5-hb03c661_1 
  xorg-libxext       conda-forge/linux-64::xorg-libxext-1.3.4-h0b41bf4_2 
  xorg-libxfixes     conda-forge/linux-64::xorg-libxfixes-5.0.3-h7f98852_1004 
  xorg-libxi         conda-forge/linux-64::xorg-libxi-1.7.10-h7f98852_0 
  xorg-libxinerama   conda-forge/linux-64::xorg-libxinerama-1.1.5-h27087fc_0 
  xorg-libxrandr     conda-forge/linux-64::xorg-libxrandr-1.5.2-h7f98852_1 
  xorg-libxrender    conda-forge/linux-64::xorg-libxrender-0.9.10-h7f98852_1003 
  xorg-randrproto    conda-forge/linux-64::xorg-randrproto-1.5.0-hb9d3cd8_1002 
  xorg-renderproto   conda-forge/linux-64::xorg-renderproto-0.11.1-hb9d3cd8_1003 
  xorg-xextproto     conda-forge/linux-64::xorg-xextproto-7.3.0-hb9d3cd8_1004 
  xorg-xproto        conda-forge/linux-64::xorg-xproto-7.0.31-hb9d3cd8_1008 
  zipp               conda-forge/noarch::zipp-3.15.0-pyhd8ed1ab_0 
  zlib               conda-forge/linux-64::zlib-1.3.1-hb9d3cd8_2 

The following packages will be REVISED:

  tk                              8.6.13-noxft_h366c992_103 --> 8.6.13-noxft_hd72426e_102 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
                                                                                
Preparing transaction: done                                                     
Verifying transaction: done                                                     
Executing transaction: done                                                     
Cloning into 'habitat-lab'...                                                   
remote: Enumerating objects: 74340, done.
remote: Counting objects: 100% (161/161), done.
remote: Compressing objects: 100% (98/98), done.
remote: Total 74340 (delta 81), reused 66 (delta 61), pack-reused 74179 (from 3)
Receiving objects: 100% (74340/74340), 277.73 MiB | 17.74 MiB/s, done.          
Resolving deltas: 100% (56360/56360), done.                                     
Note: switching to '7a96559b09abfa060e063b4afa248aa7229c8a2d'.                  
                                                                                
You are in 'detached HEAD' state. You can look around, make experimental        
changes and commit them, and you can discard any commits you make in this       
state without impacting any branches by switching back to a branch.             
                                                                                
If you want to create a new branch to retain commits you create, you may        
do so (now or later) by using -c with the switch command. Example:              
                                                                                
  git switch -c <new-branch-name>                                               
                                                                                
Or undo this operation with:                                                    
                      
  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
python: can't open file 'setup.py': [Errno 2] No such file or directory
(habitat_challenge) liuyi@liuyi:~/projects/habitat_challenge/habitat-challenge/habitat-lab$ pip install -r requirements.txt
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
(habitat_challenge) liuyi@liuyi:~/projects/habitat_challenge/habitat-challenge/habitat-lab$ cd habitat-lab
(habitat_challenge) liuyi@liuyi:~/projects/habitat_challenge/habitat-challenge/habitat-lab/habitat-lab$ pip install -r requirements.txt
Collecting home-robot@ git+ssh://****@github.com/facebookresearch/home-robot.git@habitat-challenge-2023#subdirectory=src/home_robot (from -r requirements.txt (line 18))
  Cloning ssh://****@github.com/facebookresearch/home-robot.git (to revision habitat-challenge-2023) to /tmp/pip-install-4ct0f8dl/home-robot_f22310ff692846959d02b6c18e4ab595
  Running command git clone --filter=blob:none --quiet 'ssh://****@github.com/facebookresearch/home-robot.git' /tmp/pip-install-4ct0f8dl/home-robot_f22310ff692846959d02b6c18e4ab595
  Running command git checkout -q c5b5e25ce402cce44b7315f5303e941ea9a3d252
  Resolved ssh://****@github.com/facebookresearch/home-robot.git to commit c5b5e25ce402cce44b7315f5303e941ea9a3d252
  Running command git submodule update --init --recursive -q
  ERROR: Repository not found.
  fatal: Could not read from remote repository.

  Please make sure you have the correct access rights
  and the repository exists.
  fatal: clone of 'git@github.com:cpaxton/hab_stretch.git' into submodule path '/tmp/pip-install-4ct0f8dl/home-robot_f22310ff692846959d02b6c18e4ab595/assets/hab_stretch' failed
  Failed to clone 'assets/hab_stretch'. Retry scheduled
  ERROR: Repository not found.
  fatal: Could not read from remote repository.

  Please make sure you have the correct access rights
  and the repository exists.
  fatal: clone of 'git@github.com:cpaxton/hab_stretch.git' into submodule path '/tmp/pip-install-4ct0f8dl/home-robot_f22310ff692846959d02b6c18e4ab595/assets/hab_stretch' failed
  Failed to clone 'assets/hab_stretch' a second time, aborting
  error: subprocess-exited-with-error
  
  × git submodule update --init --recursive -q did not run successfully.
  │ exit code: 1
  ╰─> See above for output.
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

× git submodule update --init --recursive -q did not run successfully.
│ exit code: 1
╰─> See above for output.

note: This error originates from a subprocess, and is likely not a problem with pip.
(habitat_challenge) liuyi@liuyi:~/projects/habitat_challenge/habitat-challenge/habitat-lab/habitat-lab$ # 进入你的项目目录外层或存放依赖的目录
cd ~/projects/habitat_challenge/

# 手动克隆指定分支 (habitat-challenge-2023)
git clone -b habitat-challenge-2023 https://github.com/facebookresearch/home-robot.git
Cloning into 'home-robot'...
remote: Enumerating objects: 33896, done.
remote: Counting objects: 100% (71/71), done.
remote: Compressing objects: 100% (37/37), done.
remote: Total 33896 (delta 46), reused 34 (delta 34), pack-reused 33825 (from 2)
Receiving objects: 100% (33896/33896), 345.31 MiB | 15.88 MiB/s, done.
Resolving deltas: 100% (23350/23350), done.
Note: switching to '9b9b33158a348ad309f9fe78845ab5d4c9dbbecf'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

(habitat_challenge) liuyi@liuyi:~/projects/habitat_challenge$ cd home-robot
nano .gitmodules  # 或者用 vim / gedit
(habitat_challenge) liuyi@liuyi:~/projects/habitat_challenge/home-robot$ git submodule update --init --recursive
fatal: No url found for submodule path 'assets/hab_stretch' in .gitmodules
(habitat_challenge) liuyi@liuyi:~/projects/habitat_challenge/home-robot$ nano .gitmodules  # 或者用 vim / gedit
(habitat_challenge) liuyi@liuyi:~/projects/habitat_challenge/home-robot$ nano .gitmodules  # 或者用 vim / gedit
(habitat_challenge) liuyi@liuyi:~/projects/habitat_challenge/home-robot$ cd ../
(habitat_challenge) liuyi@liuyi:~/projects/habitat_challenge$ cd habitat-challenge/habitat-lab/habitat-lab
(habitat_challenge) liuyi@liuyi:~/projects/habitat_challenge/habitat-challenge/habitat-lab/habitat-lab$ pip install -r requirements.txt
Collecting home-robot@ git+https://github.com/facebookresearch/home-robot.git@home-robot-ovmm-challenge-2023-v0.1.2#subdirectory=src/home_robot (from -r requirements.txt (line 19))
  Cloning https://github.com/facebookresearch/home-robot.git (to revision home-robot-ovmm-challenge-2023-v0.1.2) to /tmp/pip-install-ykwce1kv/home-robot_23cb3983d8df45d89a273a12533dc52a
  Running command git clone --filter=blob:none --quiet https://github.com/facebookresearch/home-robot.git /tmp/pip-install-ykwce1kv/home-robot_23cb3983d8df45d89a273a12533dc52a
  Running command git checkout -q 89b212fd14909584dd59813aa7a8075add720fb6
  Resolved https://github.com/facebookresearch/home-robot.git to commit 89b212fd14909584dd59813aa7a8075add720fb6
  Running command git submodule update --init --recursive -q
^CERROR: Operation cancelled by user
(habitat_challenge) liuyi@liuyi:~/projects/habitat_challenge/habitat-challenge/habitat-lab/habitat-lab$ cd ~
(habitat_challenge) liuyi@liuyi:~$ conda deactivate
(habitat) liuyi@liuyi:~$ conda deactivate
(base) liuyi@liuyi:~$ conda env list

# conda environments:
#
# * -> active
# + -> frozen
base                 *   /home/liuyi/miniforge3
habitat                  /home/liuyi/miniforge3/envs/habitat
habitat_challenge        /home/liuyi/miniforge3/envs/habitat_challenge
realman-grasp            /home/liuyi/miniforge3/envs/realman-grasp
vlfm                     /home/liuyi/miniforge3/envs/vlfm

(base) liuyi@liuyi:~$ conda env remove habitat_challenge
usage: conda [-h] [-v] [--no-plugins] [-V] COMMAND ...
conda: error: unrecognized arguments: habitat_challenge
(base) liuyi@liuyi:~$ conda env remove -n habitat_challenge

Remove all packages in environment /home/liuyi/miniforge3/envs/habitat_challenge:


## Package Plan ##

  environment location: /home/liuyi/miniforge3/envs/habitat_challenge


The following packages will be REMOVED:

  _libgcc_mutex-0.1-conda_forge
  _openmp_mutex-4.5-2_gnu
  attrs-24.2.0-pyh71513ae_0
  ca-certificates-2026.1.4-hbd8a1cb_0
  certifi-2024.8.30-pyhd8ed1ab_0
  colorama-0.4.6-pyhd8ed1ab_0
  cycler-0.11.0-pyhd8ed1ab_0
  ffmpeg-2.8.6-0
  freetype-2.14.1-ha770c72_0
  gitdb-4.0.11-pyhd8ed1ab_0
  gitpython-3.1.43-pyhd8ed1ab_0
  habitat-sim-challenge-2023-0.2.3-py3.7_linux_584ef238b9c505e91598a37a15247e52d21782c9
  habitat-sim-mutex-1.0-display_nobullet
  icu-78.2-h33c6efd_0
  imageio-2.36.0-pyh12aca89_1
  imageio-ffmpeg-0.5.1-pyhd8ed1ab_0
  importlib-metadata-4.11.4-py37h89c1867_0
  jpeg-9e-h0b41bf4_3
  kiwisolver-1.4.4-py37h7cecad7_0
  lcms2-2.14-h6ed2654_0
  ld_impl_linux-64-2.45.1-default_hbd61a6d_101
  lerc-4.0.0-h0aef613_1
  libblas-3.9.0-20_linux64_openblas
  libcblas-3.9.0-20_linux64_openblas
  libdeflate-1.14-h166bdaf_0
  libffi-3.4.6-h2dba641_1
  libfreetype-2.14.1-ha770c72_0
  libfreetype6-2.14.1-h73754d4_0
  libgcc-15.2.0-he0feb66_17
  libgcc-ng-15.2.0-h69a702a_17
  libgfortran-15.2.0-h69a702a_17
  libgfortran-ng-15.2.0-h69a702a_17
  libgfortran5-15.2.0-h68bc16d_17
  libgomp-15.2.0-he0feb66_17
  liblapack-3.9.0-20_linux64_openblas
  libllvm11-11.1.0-he0ac6c6_5
  liblzma-5.8.2-hb03c661_0
  liblzma-devel-5.8.2-hb03c661_0
  libnsl-2.0.1-hb9d3cd8_1
  libopenblas-0.3.25-pthreads_h413a1c8_0
  libpng-1.6.55-h421ea60_0
  libsqlite-3.51.2-hf4e2dac_0
  libstdcxx-15.2.0-h934c35e_17
  libstdcxx-ng-15.2.0-hdf11a46_17
  libtiff-4.4.0-h82bc61c_5
  libwebp-base-1.6.0-hd42ef1d_0
  libxcb-1.13-h7f98852_1004
  libzlib-1.3.1-hb9d3cd8_2
  llvmlite-0.39.1-py37h0761922_0
  matplotlib-3.3.2-0
  matplotlib-base-3.3.2-py37h4f6019d_1
  ncurses-6.5-h2d0b736_3
  numba-0.56.3-py37hf081915_0
  numpy-1.21.6-py37h976b520_0
  openjpeg-2.5.0-h7d73246_1
  openssl-3.6.1-h35e630c_1
  pillow-9.2.0-py37h850a105_2
  pip-24.0-pyhd8ed1ab_0
  pthread-stubs-0.4-hb9d3cd8_1002
  pyparsing-3.1.4-pyhd8ed1ab_0
  python-3.7.12-hf930737_100_cpython
  python-dateutil-2.9.0-pyhd8ed1ab_0
  python_abi-3.7-4_cp37m
  quaternion-2022.4.1-py37h540881e_0
  readline-8.3-h853b02a_0
  scipy-1.7.3-py37hf2a6cf1_0
  setuptools-69.0.3-pyhd8ed1ab_0
  six-1.16.0-pyh6c4a22f_0
  smmap-3.0.5-pyh44b312d_0
  sqlite-3.51.2-h04a0ce9_0
  tk-8.6.13-noxft_hd72426e_102
  tornado-6.2-py37h540881e_0
  tqdm-4.67.1-pyhd8ed1ab_0
  typing-extensions-4.7.1-hd8ed1ab_0
  typing_extensions-4.7.1-pyha770c72_0
  wheel-0.42.0-pyhd8ed1ab_0
  x264-1!164.3095-h166bdaf_2
  xorg-fixesproto-5.0-hb9d3cd8_1003
  xorg-inputproto-2.3.2-hb9d3cd8_1003
  xorg-kbproto-1.0.7-hb9d3cd8_1003
  xorg-libx11-1.8.4-h0b41bf4_0
  xorg-libxau-1.0.12-hb03c661_1
  xorg-libxcursor-1.2.0-h0b41bf4_1
  xorg-libxdmcp-1.1.5-hb03c661_1
  xorg-libxext-1.3.4-h0b41bf4_2
  xorg-libxfixes-5.0.3-h7f98852_1004
  xorg-libxi-1.7.10-h7f98852_0
  xorg-libxinerama-1.1.5-h27087fc_0
  xorg-libxrandr-1.5.2-h7f98852_1
  xorg-libxrender-0.9.10-h7f98852_1003
  xorg-randrproto-1.5.0-hb9d3cd8_1002
  xorg-renderproto-0.11.1-hb9d3cd8_1003
  xorg-xextproto-7.3.0-hb9d3cd8_1004
  xorg-xproto-7.0.31-hb9d3cd8_1008
  xz-5.8.2-ha02ee65_0
  xz-gpl-tools-5.8.2-ha02ee65_0
  xz-tools-5.8.2-hb03c661_0
  zipp-3.15.0-pyhd8ed1ab_0
  zlib-1.3.1-hb9d3cd8_2
  zstd-1.5.7-hb78ec9c_6


Proceed ([y]/n)? y


Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
Everything found within the environment (/home/liuyi/miniforge3/envs/habitat_challenge), including any conda environment configurations and any non-conda files, will be deleted. Do you wish to continue?
 (y/[n])? y

(base) liuyi@liuyi:~$ conda activate habitat
(habitat) liuyi@liuyi:~$ cd ~/projects/habitat-lab
export TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD=1

python -u -m habitat_baselines.run --config-name=pointnav/ppo_pointnav_example.yaml
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 14:14:18,336 Loading resume state: data/new_checkpoints/.habitat-resume-state.pth
/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ddppo/ddp_utils.py:224: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
  return torch.load(filename, map_location="cpu")
2026-02-10 14:14:18,403 config: habitat:
  seed: 100
  env_task: GymHabitatEnv
  env_task_gym_dependencies: []
  env_task_gym_id: ''
  environment:
    max_episode_steps: 500
    max_episode_seconds: 10000000
    iterator_options:
      cycle: true
      shuffle: true
      group_by_scene: true
      num_episode_sample: -1
      max_scene_repeat_episodes: -1
      max_scene_repeat_steps: 10000
      step_repetition_range: 0.2
  simulator:
    type: Sim-v0
    forward_step_size: 0.25
    turn_angle: 10
    create_renderer: false
    requires_textures: true
    auto_sleep: false
    step_physics: true
    concur_render: false
    needs_markers: true
    update_articulated_agent: true
    scene: data/scene_datasets/habitat-test-scenes/van-gogh-room.glb
    scene_dataset: default
    additional_object_paths: []
    seed: ${habitat.seed}
    default_agent_id: 0
    debug_render: false
    debug_render_articulated_agent: false
    kinematic_mode: false
    should_setup_semantic_ids: true
    debug_render_goal: true
    robot_joint_start_noise: 0.0
    ctrl_freq: 120.0
    ac_freq_ratio: 4
    load_objs: true
    hold_thresh: 0.15
    grasp_impulse: 10000.0
    agents:
      main_agent:
        height: 1.5
        radius: 0.1
        max_climb: 0.2
        max_slope: 45.0
        grasp_managers: 1
        sim_sensors:
          rgb_sensor:
            type: HabitatSimRGBSensor
            height: 256
            width: 256
            position:
            - 0.0
            - 1.25
            - 0.0
            orientation:
            - 0.0
            - 0.0
            - 0.0
            hfov: 90
            sensor_subtype: PINHOLE
            noise_model: None
            noise_model_kwargs: {}
          depth_sensor:
            type: HabitatSimDepthSensor
            height: 256
            width: 256
            position:
            - 0.0
            - 1.25
            - 0.0
            orientation:
            - 0.0
            - 0.0
            - 0.0
            hfov: 90
            sensor_subtype: PINHOLE
            noise_model: None
            noise_model_kwargs: {}
            min_depth: 0.0
            max_depth: 10.0
            normalize_depth: true
        is_set_start_state: false
        start_position:
        - 0.0
        - 0.0
        - 0.0
        start_rotation:
        - 0.0
        - 0.0
        - 0.0
        - 1.0
        joint_start_noise: 0.1
        joint_that_can_control: null
        joint_start_override: null
        articulated_agent_urdf: null
        articulated_agent_type: null
        ik_arm_urdf: null
        motion_data_path: ''
        auto_update_sensor_transform: true
    agents_order:
    - main_agent
    default_agent_navmesh: true
    navmesh_include_static_objects: false
    habitat_sim_v0:
      gpu_device_id: 0
      gpu_gpu: false
      allow_sliding: true
      frustum_culling: true
      enable_physics: false
      enable_hbao: false
      physics_config_file: ./data/default.physics_config.json
      leave_context_with_background_renderer: false
      enable_gfx_replay_save: false
    ep_info: null
    object_ids_start: 100
    renderer:
      enable_batch_renderer: false
      composite_files: null
      classic_replay_renderer: false
  task:
    physics_target_sps: 60.0
    reward_measure: distance_to_goal_reward
    success_measure: spl
    success_reward: 2.5
    slack_reward: -0.01
    end_on_success: true
    type: Nav-v0
    lab_sensors:
      pointgoal_with_gps_compass_sensor:
        type: PointGoalWithGPSCompassSensor
        goal_format: POLAR
        dimensionality: 2
    measurements:
      distance_to_goal:
        type: DistanceToGoal
        distance_to: POINT
      success:
        type: Success
        success_distance: 0.2
      spl:
        type: SPL
      distance_to_goal_reward:
        type: DistanceToGoalReward
    rank0_env0_measure_names:
    - habitat_perf
    rank0_measure_names: []
    goal_sensor_uuid: pointgoal_with_gps_compass
    count_obj_collisions: true
    settle_steps: 5
    constraint_violation_ends_episode: true
    constraint_violation_drops_object: false
    force_regenerate: false
    should_save_to_cache: false
    object_in_hand_sample_prob: 0.167
    min_start_distance: 3.0
    render_target: true
    filter_colliding_states: true
    num_spawn_attempts: 200
    spawn_max_dist_to_obj: 2.0
    base_angle_noise: 0.523599
    spawn_max_dist_to_obj_delta: 0.02
    recep_place_shrink_factor: 0.8
    ee_sample_factor: 0.2
    ee_exclude_region: 0.0
    base_noise: 0.05
    spawn_region_scale: 0.2
    joint_max_impulse: -1.0
    desired_resting_position:
    - 0.5
    - 0.0
    - 1.0
    use_marker_t: true
    cache_robot_init: false
    success_state: 0.0
    should_enforce_target_within_reach: false
    task_spec_base_path: habitat/task/rearrange/pddl/
    task_spec: ''
    pddl_domain_def: replica_cad
    obj_succ_thresh: 0.3
    enable_safe_drop: false
    art_succ_thresh: 0.15
    robot_at_thresh: 2.0
    min_distance_start_agents: -1.0
    actions:
      stop:
        type: StopAction
      move_forward:
        type: MoveForwardAction
        tilt_angle: 15
      turn_left:
        type: TurnLeftAction
        tilt_angle: 15
      turn_right:
        type: TurnRightAction
        tilt_angle: 15
  dataset:
    type: PointNav-v1
    split: train
    scenes_dir: data/scene_datasets
    content_scenes:
    - '*'
    data_path: data/datasets/pointnav/habitat-test-scenes/v1/{split}/{split}.json.gz
    metadata: null
  gym:
    obs_keys: null
    action_keys: null
    achieved_goal_keys: []
    desired_goal_keys: []
habitat_baselines:
  evaluate: false
  trainer_name: ppo
  updater_name: PPO
  distrib_updater_name: DDPPO
  torch_gpu_id: 0
  tensorboard_dir: tb
  writer_type: tb
  video_dir: video_dir
  video_fps: 10
  test_episode_count: 2
  eval_ckpt_path_dir: data/new_checkpoints
  num_environments: 1
  num_processes: -1
  rollout_storage_name: RolloutStorage
  checkpoint_folder: data/new_checkpoints
  num_updates: -1
  num_checkpoints: 50
  checkpoint_interval: -1
  total_num_steps: 1000000.0
  log_interval: 10
  log_file: train.log
  force_blind_policy: false
  verbose: true
  vector_env_factory:
    _target_: habitat_baselines.common.HabitatVectorEnvFactory
  evaluator:
    _target_: habitat_baselines.rl.ppo.habitat_evaluator.HabitatEvaluator
  eval_keys_to_include_in_name: []
  force_torch_single_threaded: true
  wb:
    project_name: ''
    entity: ''
    group: ''
    run_name: ''
  load_resume_state_config: true
  eval:
    split: val
    use_ckpt_config: true
    should_load_ckpt: true
    evals_per_ep: 1
    video_option:
    - disk
    - tensorboard
    extra_sim_sensors: {}
  profiling:
    capture_start_step: -1
    num_steps_to_capture: -1
  should_log_single_proc_infos: false
  on_save_ckpt_callback: null
  rl:
    agent:
      type: SingleAgentAccessMgr
      num_agent_types: 1
      num_active_agents_per_type:
      - 1
      num_pool_agents_per_type:
      - 1
      agent_sample_interval: 20
      force_partner_sample_idx: -1
      behavior_latent_dim: -1
      force_all_agents: false
      discrim_reward_weight: 1.0
      allow_self_play: false
      self_play_batched: false
      load_type1_pop_ckpts: null
    preemption:
      append_slurm_job_id: false
      save_resume_state_interval: 100
      save_state_batch_only: false
    policy:
      main_agent:
        name: PointNavResNetPolicy
        action_distribution_type: categorical
        action_dist:
          use_log_std: true
          use_softplus: false
          std_init: ???
          log_std_init: 0.0
          use_std_param: false
          clamp_std: true
          min_std: 1.0e-06
          max_std: 1
          min_log_std: -5
          max_log_std: 2
          action_activation: tanh
          scheduled_std: false
        obs_transforms: {}
        hierarchical_policy: ???
    ppo:
      clip_param: 0.1
      ppo_epoch: 1
      num_mini_batch: 1
      value_loss_coef: 0.5
      entropy_coef: 0.01
      lr: 0.00025
      eps: 1.0e-05
      max_grad_norm: 0.5
      num_steps: 32
      use_gae: true
      use_linear_lr_decay: true
      use_linear_clip_decay: true
      gamma: 0.99
      tau: 0.95
      reward_window_size: 50
      use_normalized_advantage: false
      hidden_size: 512
      entropy_target_factor: 0.0
      use_adaptive_entropy_pen: false
      use_clipped_value_loss: true
      use_double_buffered_sampler: false
    ddppo:
      sync_frac: 0.6
      distrib_backend: GLOO
      rnn_type: GRU
      num_recurrent_layers: 1
      backbone: resnet18
      pretrained_weights: data/ddppo-models/gibson-2plus-resnet50.pth
      pretrained: false
      pretrained_encoder: false
      train_encoder: true
      reset_critic: true
      force_distributed: false
    ver:
      variable_experience: true
      num_inference_workers: 2
      overlap_rollouts_and_learn: false
    auxiliary_losses: {}

2026-02-10 14:14:18,404 Initializing dataset PointNav-v1
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 14:14:21,014 Initializing dataset PointNav-v1
2026-02-10 14:14:21,210 initializing sim Sim-v0
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
Renderer: NVIDIA GeForce RTX 4060 Laptop GPU/PCIe/SSE2 by NVIDIA Corporation
OpenGL version: 4.6.0 NVIDIA 580.95.05
Using optional features:
    GL_ARB_vertex_array_object
    GL_ARB_separate_shader_objects
    GL_ARB_robustness
    GL_ARB_texture_storage
    GL_ARB_texture_view
    GL_ARB_framebuffer_no_attachments
    GL_ARB_invalidate_subdata
    GL_ARB_texture_storage_multisample
    GL_ARB_multi_bind
    GL_ARB_direct_state_access
    GL_ARB_get_texture_sub_image
    GL_ARB_texture_filter_anisotropic
    GL_KHR_debug
    GL_KHR_parallel_shader_compile
    GL_NV_depth_buffer_float
Using driver workarounds:
    no-forward-compatible-core-context
    nv-egl-incorrect-gl11-function-pointers
    no-layout-qualifiers-on-old-glsl
    nv-zero-context-profile-mask
    nv-implementation-color-read-format-dsa-broken
    nv-cubemap-inconsistent-compressed-image-size
    nv-cubemap-broken-full-compressed-image-query
    nv-compressed-block-size-in-bits
[14:14:21:298262]:[Warning]:[Metadata] SceneDatasetAttributes.cpp(107)::addNewSceneInstanceToDataset : Dataset : 'default' : Lighting Layout Attributes 'no_lights' specified in Scene Attributes but does not exist in dataset, so creating default.
[14:14:21:299154]:[Warning]:[Scene] SemanticScene.h(331)::checkFileExists : ::loadSemanticSceneDescriptor: File `data/scene_datasets/habitat-test-scenes/skokloster-castle.scn` does not exist.  Aborting load.
[14:14:21:299170]:[Warning]:[Scene] SemanticScene.cpp(123)::loadSemanticSceneDescriptor : SSD File Naming Issue! Neither SemanticAttributes-provided name : `data/scene_datasets/habitat-test-scenes/skokloster-castle.scn` nor constructed filename : `data/scene_datasets/habitat-test-scenes/info_semantic.json` exist on disk.
[14:14:21:299184]:[Error]:[Scene] SemanticScene.cpp(139)::loadSemanticSceneDescriptor : SSD Load Failure! File with SemanticAttributes-provided name `data/scene_datasets/habitat-test-scenes/skokloster-castle.scn` exists but failed to load.
[14:14:22:067015]:[Warning]:[Sim] Simulator.cpp(595)::instanceStageForSceneAttributes : The active scene does not contain semantic annotations : activeSemanticSceneID_ = 0
2026-02-10 14:14:22,070 Initializing task Nav-v0
2026-02-10 14:14:22,572 Number of params to train: 5821797
2026-02-10 14:14:22,573 Agent number of parameters: 5821797
2026-02-10 14:14:23,660 update: 6900	fps: 139.594	
2026-02-10 14:14:23,660 Num updates: 6900	Num frames 220800
2026-02-10 14:14:23,660 Average window size: 50  distance_to_goal: 0.585  distance_to_goal_reward: 0.000  reward: 2.492  spl: 0.481  success: 0.604
2026-02-10 14:14:23,660 	Perf Stats: trainer.rollout_collect: 0.687 trainer.sample_action: 0.018 trainer.obs_insert: 0.000 trainer.step_env: 0.002 trainer.update_stats: 0.000 trainer.update_agent: 0.280
2026-02-10 14:14:25,546 update: 6910	fps: 139.630	
2026-02-10 14:14:25,547 Num updates: 6910	Num frames 221120
2026-02-10 14:14:25,547 Average window size: 50  distance_to_goal: 0.693  distance_to_goal_reward: 0.000  reward: 2.619  spl: 0.484  success: 0.592
2026-02-10 14:14:25,547 	Perf Stats: trainer.rollout_collect: 0.215 trainer.sample_action: 0.004 trainer.obs_insert: 0.000 trainer.step_env: 0.002 trainer.update_stats: 0.000 trainer.update_agent: 0.043
2026-02-10 14:14:27,378 update: 6920	fps: 139.671	
2026-02-10 14:14:27,378 Num updates: 6920	Num frames 221440
2026-02-10 14:14:27,378 Average window size: 50  distance_to_goal: 0.728  distance_to_goal_reward: 0.000  reward: 3.092  spl: 0.488  success: 0.587
2026-02-10 14:14:27,378 	Perf Stats: trainer.rollout_collect: 0.190 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.002 trainer.update_stats: 0.000 trainer.update_agent: 0.032
2026-02-10 14:14:29,275 update: 6930	fps: 139.705	
2026-02-10 14:14:29,275 Num updates: 6930	Num frames 221760
2026-02-10 14:14:29,275 Average window size: 50  distance_to_goal: 0.823  distance_to_goal_reward: 0.000  reward: 3.299  spl: 0.423  success: 0.500
2026-02-10 14:14:29,275 	Perf Stats: trainer.rollout_collect: 0.183 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.002 trainer.update_stats: 0.000 trainer.update_agent: 0.028
2026-02-10 14:14:31,194 update: 6940	fps: 139.738	
2026-02-10 14:14:31,194 Num updates: 6940	Num frames 222080
2026-02-10 14:14:31,194 Average window size: 50  distance_to_goal: 0.946  distance_to_goal_reward: 0.000  reward: 4.172  spl: 0.395  success: 0.469
2026-02-10 14:14:31,194 	Perf Stats: trainer.rollout_collect: 0.180 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.002 trainer.update_stats: 0.000 trainer.update_agent: 0.026
2026-02-10 14:14:33,041 update: 6950	fps: 139.777	
2026-02-10 14:14:33,041 Num updates: 6950	Num frames 222400
2026-02-10 14:14:33,041 Average window size: 50  distance_to_goal: 0.567  distance_to_goal_reward: 0.000  reward: 10.118  spl: 0.683  success: 0.846
2026-02-10 14:14:33,041 	Perf Stats: trainer.rollout_collect: 0.177 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.002 trainer.update_stats: 0.000 trainer.update_agent: 0.024
2026-02-10 14:14:34,847 update: 6960	fps: 139.819	
2026-02-10 14:14:34,848 Num updates: 6960	Num frames 222720
2026-02-10 14:14:34,848 Average window size: 50  distance_to_goal: 0.117  distance_to_goal_reward: 0.000  reward: 11.242  spl: 0.740  success: 0.917
2026-02-10 14:14:34,848 	Perf Stats: trainer.rollout_collect: 0.174 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.002 trainer.update_stats: 0.000 trainer.update_agent: 0.023
2026-02-10 14:14:36,697 update: 6970	fps: 139.858	
2026-02-10 14:14:36,697 Num updates: 6970	Num frames 223040
2026-02-10 14:14:36,697 Average window size: 50  distance_to_goal: 0.525  distance_to_goal_reward: 0.000  reward: 10.478  spl: 0.606  success: 0.778
2026-02-10 14:14:36,697 	Perf Stats: trainer.rollout_collect: 0.173 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.002 trainer.update_stats: 0.000 trainer.update_agent: 0.023
2026-02-10 14:14:38,520 update: 6980	fps: 139.898	
2026-02-10 14:14:38,520 Num updates: 6980	Num frames 223360
2026-02-10 14:14:38,520 Average window size: 50  distance_to_goal: 0.481  distance_to_goal_reward: 0.000  reward: 9.436  spl: 0.714  success: 0.900
2026-02-10 14:14:38,520 	Perf Stats: trainer.rollout_collect: 0.171 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.002 trainer.update_stats: 0.000 trainer.update_agent: 0.022
2026-02-10 14:14:40,325 update: 6990	fps: 139.941	
2026-02-10 14:14:40,325 Num updates: 6990	Num frames 223680
2026-02-10 14:14:40,325 Average window size: 50  distance_to_goal: 0.567  distance_to_goal_reward: 0.000  reward: 8.115  spl: 0.715  success: 0.875
2026-02-10 14:14:40,325 	Perf Stats: trainer.rollout_collect: 0.170 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.002 trainer.update_stats: 0.000 trainer.update_agent: 0.022
^C2026-02-10 14:14:41,962 Worker KeyboardInterrupt
Traceback (most recent call last):
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/run.py", line 77, in <module>
    main()
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/hydra/main.py", line 94, in decorated_main
    _run_hydra(
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/hydra/_internal/utils.py", line 394, in _run_hydra
    _run_app(
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/hydra/_internal/utils.py", line 457, in _run_app
    run_and_report(
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/hydra/_internal/utils.py", line 220, in run_and_report
    return func()
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/hydra/_internal/utils.py", line 458, in <lambda>
    lambda: hydra.run(
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/hydra/_internal/hydra.py", line 119, in run
    ret = run_job(
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/hydra/core/utils.py", line 186, in run_job
    ret.return_value = task_function(task_cfg)
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/run.py", line 31, in main
    execute_exp(cfg, "eval" if cfg.habitat_baselines.evaluate else "train")
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/run.py", line 60, in execute_exp
    trainer.train()
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/contextlib.py", line 79, in inner
    return func(*args, **kwds)
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/ppo_trainer.py", line 719, in train
    save_resume_state(
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ddppo/ddp_utils.py", line 135, in _wrapper
    return fn(*args, **kwargs)
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ddppo/ddp_utils.py", line 200, in save_resume_state
    torch.save(state, filename)
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/torch/serialization.py", line 967, in save
    _save(
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/torch/serialization.py", line 1213, in _save
    pickler.dump(obj)
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/torch/serialization.py", line 1209, in persistent_id
    def persistent_id(self, obj):
KeyboardInterrupt
Exception ignored in: <function VectorEnv.__del__ at 0x74d65dddc1f0>
Traceback (most recent call last):
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/core/vector_env.py", line 613, in __del__
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/core/vector_env.py", line 470, in close
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/core/vector_env.py", line 131, in __call__
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/utils/pickle5_multiprocessing.py", line 63, in send
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/multiprocessing/connection.py", line 200, in send_bytes
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/multiprocessing/connection.py", line 411, in _send_bytes
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/multiprocessing/connection.py", line 368, in _send
BrokenPipeError: [Errno 32] Broken pipe

(habitat) liuyi@liuyi:~/projects/habitat-lab$ python examples/example.py
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 14:15:32,579 Initializing dataset RearrangeDataset-v0
Traceback (most recent call last):
  File "/home/liuyi/projects/habitat-lab/examples/example.py", line 31, in <module>
    example()
  File "/home/liuyi/projects/habitat-lab/examples/example.py", line 15, in example
    with gym.make("HabitatRenderPick-v0") as env:
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/gym/envs/registration.py", line 676, in make
    return registry.make(id, **kwargs)
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/gym/envs/registration.py", line 520, in make
    return spec.make(**kwargs)
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/gym/envs/registration.py", line 140, in make
    env = cls(**_kwargs)
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/gym/gym_definitions.py", line 91, in _make_habitat_gym_env
    env = make_gym_from_config(config)
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/gym/gym_definitions.py", line 60, in make_gym_from_config
    return make_env_fn(env_class=env_class, config=config, dataset=dataset)
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/utils/env_utils.py", line 36, in make_env_fn
    dataset = make_dataset(config.dataset.type, config=config.dataset)
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/datasets/registration.py", line 22, in make_dataset
    return _dataset(**kwargs)  # type: ignore
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/datasets/rearrange/rearrange_dataset.py", line 59, in __init__
    raise ValueError(
ValueError: Requested RearrangeDataset config paths 'data/datasets/replica_cad/rearrange/v2/train/rearrange_easy.json.gz' or 'data/replica_cad/' are not downloaded locally. Aborting.
(habitat) liuyi@liuyi:~/projects/habitat-lab$ python examples/interactive_play.py --never-end

Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 14:17:05,935 Initializing dataset RearrangeDataset-v0
Traceback (most recent call last):
  File "/home/liuyi/projects/habitat-lab/examples/interactive_play.py", line 802, in <module>
    with habitat.Env(config=config) as env:
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/core/env.py", line 88, in __init__
    self._dataset = make_dataset(
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/datasets/registration.py", line 22, in make_dataset
    return _dataset(**kwargs)  # type: ignore
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/datasets/rearrange/rearrange_dataset.py", line 59, in __init__
    raise ValueError(
ValueError: Requested RearrangeDataset config paths 'data/datasets/replica_cad/rearrange/v2/train/rearrange_easy.json.gz' or 'data/replica_cad/' are not downloaded locally. Aborting.
(habitat) liuyi@liuyi:~/projects/habitat-lab$ python -m habitat_sim.utils.datasets_download \
  --uids replica_cad_dataset \
  --data-path /data
Traceback (most recent call last):
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/habitat_sim-0.3.3-py3.9-linux-x86_64.egg/habitat_sim/utils/datasets_download.py", line 907, in main
    os.makedirs(data_path, exist_ok=True)
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/os.py", line 225, in makedirs
    mkdir(name, mode)
PermissionError: [Errno 13] Permission denied: '/data'
----------------------------------------------------------------
Aborting download, failed to create data_path.
Try providing --data-path (e.g. '/path/to/habitat-sim/data/')
----------------------------------------------------------------
usage: datasets_download.py [-h] [--uids [UIDS ...] | --list]
                            [--data-path DATA_PATH]
                            [--clean | --replace | --no-replace]
                            [--username USERNAME] [--password PASSWORD]
                            [--no-prune]

optional arguments:
  -h, --help            show this help message and exit
  --uids [UIDS ...]     Unique ID of the data to download.
  --list                List available datasource uid options and exit.
  --data-path DATA_PATH
                        Optionally provide a path to the desired root data/
                        directory. Default is "habitat-sim/data/".
  --clean               Remove nested child directories for the datasource.
  --replace             If set, existing equivalent versions of any dataset
                        found during download will be deleted automatically.
                        Otherwise user will be prompted before overriding
                        existing data.
  --no-replace          If set, existing equivalent versions of any dataset
                        found during download will be skipped automatically.
                        Otherwise user will be prompted before overriding
                        existing data.
  --username USERNAME   Username to use for downloads that require
                        authentication
  --password PASSWORD   Password to use for downloads that require
                        authentication
  --no-prune            Optionally disable pruning for git-lfs repo
                        datasources. Use this if your system git version does
                        not support forced pruning (e.g. Ubuntu 20.x).
(habitat) liuyi@liuyi:~/projects/habitat-lab$ python -m habitat_sim.utils.datasets_download \
  --uids replica_cad_dataset \
  --data-path data/
git clone --depth 1 --branch v1.6 https://huggingface.co/datasets/ai-habitat/ReplicaCAD_dataset.git /home/liuyi/projects/habitat-lab/data/versioned_data/replica_cad_dataset
Cloning into '/home/liuyi/projects/habitat-lab/data/versioned_data/replica_cad_dataset'...
remote: Enumerating objects: 624, done.
remote: Counting objects: 100% (624/624), done.
remote: Compressing objects: 100% (427/427), done.
remote: Total 624 (delta 197), reused 621 (delta 197), pack-reused 0 (from 0)
Receiving objects: 100% (624/624), 785.07 KiB | 1.06 MiB/s, done.
Resolving deltas: 100% (197/197), done.
Note: switching to '6be07e532c83c5799a6e96152f926d07838c2084'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

Filtering content: 100% (201/201), 147.42 MiB | 8.53 MiB/s, done.
prune: 201 local object(s), 201 retained, done.                                 
Traceback (most recent call last):
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/habitat_sim-0.3.3-py3.9-linux-x86_64.egg/habitat_sim/utils/datasets_download.py", line 964, in <module>
    main(sys.argv[1:])
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/habitat_sim-0.3.3-py3.9-linux-x86_64.egg/habitat_sim/utils/datasets_download.py", line 953, in main
    download_and_place(
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/habitat_sim-0.3.3-py3.9-linux-x86_64.egg/habitat_sim/utils/datasets_download.py", line 813, in download_and_place
    os.symlink(src=version_dir, dst=link_path, target_is_directory=True)
FileExistsError: [Errno 17] File exists: '/home/liuyi/projects/habitat-lab/data/versioned_data/replica_cad_dataset' -> '/home/liuyi/projects/habitat-lab/data/replica_cad'
(habitat) liuyi@liuyi:~/projects/habitat-lab$ cd ~/projects/habitat-lab

# 看 data 目录
ls -lah data | sed -n '1,80p'

# 重点看 replica_cad 这一项
ls -l data/replica_cad
total 16K
drwxrwxr-x  4 liuyi liuyi 4.0K Feb 10 14:18 .
drwxrwxr-x 16 liuyi liuyi 4.0K Feb  5 15:25 ..
lrwxrwxrwx  1 liuyi liuyi   37 Feb  5 15:25 datasets -> /home/liuyi/datasets/habitat/datasets
lrwxrwxrwx  1 liuyi liuyi   44 Feb  5 15:30 new_checkpoints -> /home/liuyi/datasets/habitat/new_checkpoints
lrwxrwxrwx  1 liuyi liuyi   36 Feb  5 15:25 objects -> /home/liuyi/datasets/habitat/objects
lrwxrwxrwx  1 liuyi liuyi   40 Feb  5 15:25 replica_cad -> /home/liuyi/datasets/habitat/replica_cad
lrwxrwxrwx  1 liuyi liuyi   35 Feb  5 15:25 robots -> /home/liuyi/datasets/habitat/robots
lrwxrwxrwx  1 liuyi liuyi   43 Feb  5 15:25 scene_datasets -> /home/liuyi/datasets/habitat/scene_datasets
drwxrwxr-x  3 liuyi liuyi 4.0K Feb 10 14:18 versioned_data
drwxrwxr-x  2 liuyi liuyi 4.0K Feb  5 15:31 videos
lrwxrwxrwx 1 liuyi liuyi 40 Feb  5 15:25 data/replica_cad -> /home/liuyi/datasets/habitat/replica_cad
(habitat) liuyi@liuyi:~/projects/habitat-lab$ readlink -f data/replica_cad 2>/dev/null || true

# 看它的类型（symlink/dir/file）
stat -c '%F -> %N' data/replica_cad 2>/dev/null || true
/home/liuyi/datasets/habitat/versioned_data/replica_cad_dataset
symbolic link -> 'data/replica_cad' -> '/home/liuyi/datasets/habitat/replica_cad'
(habitat) liuyi@liuyi:~/projects/habitat-lab$ python -m habitat_sim.utils.datasets_download --uids habitat_test_scenes --data-path data/
python -m habitat_sim.utils.datasets_download --uids habitat_test_pointnav_dataset --data-path data/

python examples/example.py
git clone --depth 1 --branch main https://huggingface.co/datasets/ai-habitat/habitat_test_scenes.git /home/liuyi/projects/habitat-lab/data/versioned_data/habitat_test_scenes
Cloning into '/home/liuyi/projects/habitat-lab/data/versioned_data/habitat_test_scenes'...
remote: Enumerating objects: 11, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 11 (delta 0), reused 11 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (11/11), 16.62 KiB | 3.32 MiB/s, done.
Filtering content: 100% (4/4), 105.54 MiB | 10.15 MiB/s, done.
prune: 4 local object(s), 0 retained, done.                                     
prune: Deleting objects: 100% (4/4), done.                                      
=======================================================
Dataset (habitat_test_scenes) successfully downloaded.
Source: '/home/liuyi/projects/habitat-lab/data/versioned_data/habitat_test_scenes'
Symlink: '/home/liuyi/projects/habitat-lab/data/scene_datasets/habitat-test-scenes'
=======================================================
--2026-02-10 14:22:17--  http://dl.fbaipublicfiles.com/habitat/habitat-test-pointnav-dataset_v1.0.zip
Resolving dl.fbaipublicfiles.com (dl.fbaipublicfiles.com)... 65.8.76.47, 65.8.76.35, 65.8.76.89, ...
Connecting to dl.fbaipublicfiles.com (dl.fbaipublicfiles.com)|65.8.76.47|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 894623 (874K) [application/zip]
Saving to: ‘/home/liuyi/projects/habitat-lab/data/habitat-test-pointnav-dataset_v1.0.zip’

habitat-test-pointn 100%[===================>] 873.66K  1.37MB/s    in 0.6s    

2026-02-10 14:22:18 (1.37 MB/s) - ‘/home/liuyi/projects/habitat-lab/data/habitat-test-pointnav-dataset_v1.0.zip’ saved [894623/894623]

Traceback (most recent call last):
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/habitat_sim-0.3.3-py3.9-linux-x86_64.egg/habitat_sim/utils/datasets_download.py", line 964, in <module>
    main(sys.argv[1:])
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/habitat_sim-0.3.3-py3.9-linux-x86_64.egg/habitat_sim/utils/datasets_download.py", line 953, in main
    download_and_place(
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/habitat_sim-0.3.3-py3.9-linux-x86_64.egg/habitat_sim/utils/datasets_download.py", line 810, in download_and_place
    os.unlink(link_path)
IsADirectoryError: [Errno 21] Is a directory: '/home/liuyi/projects/habitat-lab/data/datasets/pointnav/habitat-test-scenes'
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 14:22:20,644 Initializing dataset RearrangeDataset-v0
Traceback (most recent call last):
  File "/home/liuyi/projects/habitat-lab/examples/example.py", line 31, in <module>
    example()
  File "/home/liuyi/projects/habitat-lab/examples/example.py", line 15, in example
    with gym.make("HabitatRenderPick-v0") as env:
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/gym/envs/registration.py", line 676, in make
    return registry.make(id, **kwargs)
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/gym/envs/registration.py", line 520, in make
    return spec.make(**kwargs)
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/gym/envs/registration.py", line 140, in make
    env = cls(**_kwargs)
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/gym/gym_definitions.py", line 91, in _make_habitat_gym_env
    env = make_gym_from_config(config)
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/gym/gym_definitions.py", line 60, in make_gym_from_config
    return make_env_fn(env_class=env_class, config=config, dataset=dataset)
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/utils/env_utils.py", line 36, in make_env_fn
    dataset = make_dataset(config.dataset.type, config=config.dataset)
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/datasets/registration.py", line 22, in make_dataset
    return _dataset(**kwargs)  # type: ignore
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/datasets/rearrange/rearrange_dataset.py", line 59, in __init__
    raise ValueError(
ValueError: Requested RearrangeDataset config paths 'data/datasets/replica_cad/rearrange/v2/train/rearrange_easy.json.gz' or 'data/replica_cad/' are not downloaded locally. Aborting.
(habitat) liuyi@liuyi:~/projects/habitat-lab$ cd ~/projects/habitat-lab
export TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD=1
DATA_ROOT=/home/liuyi/datasets/habitat
(habitat) liuyi@liuyi:~/projects/habitat-lab$ # 关键：把 Rearrange 依赖一次性补 齐（example.py / interactive_play.py 需要）
python -m habitat_sim.utils.datasets_download \
  --uids rearrange_task_assets \
  --data-path "$DATA_ROOT" \
  --replace
git clone --depth 1 --branch v1.6 https://huggingface.co/datasets/ai-habitat/ReplicaCAD_dataset.git /home/liuyi/datasets/habitat/versioned_data/replica_cad_dataset
Cloning into '/home/liuyi/datasets/habitat/versioned_data/replica_cad_dataset'...
remote: Enumerating objects: 624, done.
remote: Counting objects: 100% (624/624), done.
remote: Compressing objects: 100% (427/427), done.
remote: Total 624 (delta 197), reused 621 (delta 197), pack-reused 0 (from 0)
Receiving objects: 100% (624/624), 785.07 KiB | 10.47 MiB/s, done.
Resolving deltas: 100% (197/197), done.
Note: switching to '6be07e532c83c5799a6e96152f926d07838c2084'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

Filtering content: 100% (201/201), 147.42 MiB | 10.03 MiB/s, done.
prune: 201 local object(s), 201 retained, done.                                 
=======================================================
Dataset (replica_cad_dataset) successfully downloaded.
Source: '/home/liuyi/datasets/habitat/versioned_data/replica_cad_dataset'
Symlink: '/home/liuyi/datasets/habitat/replica_cad'
=======================================================
git clone --depth 1 --branch v2.0 https://huggingface.co/datasets/ai-habitat/hab_fetch.git /home/liuyi/datasets/habitat/versioned_data/hab_fetch
Cloning into '/home/liuyi/datasets/habitat/versioned_data/hab_fetch'...
remote: Enumerating objects: 78, done.
remote: Counting objects: 100% (78/78), done.
remote: Compressing objects: 100% (70/70), done.
remote: Total 78 (delta 8), reused 77 (delta 8), pack-reused 0 (from 0)
Unpacking objects: 100% (78/78), 1.00 MiB | 1.24 MiB/s, done.
Note: switching to 'd3f7c41602e6eea1a46f8f9dfc4d8fb2778c6773'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

Filtering content: 100% (27/27), 30.46 MiB | 9.63 MiB/s, done.
prune: 27 local object(s), 27 retained, done.                                   
=======================================================
Dataset (hab_fetch) successfully downloaded.
Source: '/home/liuyi/datasets/habitat/versioned_data/hab_fetch'
Symlink: '/home/liuyi/datasets/habitat/robots/hab_fetch'
=======================================================
git clone --depth 1 --branch main https://huggingface.co/datasets/ai-habitat/ycb.git /home/liuyi/datasets/habitat/versioned_data/ycb
Cloning into '/home/liuyi/datasets/habitat/versioned_data/ycb'...
remote: Enumerating objects: 480, done.
remote: Counting objects: 100% (480/480), done.
remote: Compressing objects: 100% (326/326), done.
remote: Total 480 (delta 75), reused 480 (delta 75), pack-reused 0 (from 0)
Receiving objects: 100% (480/480), 50.06 KiB | 12.51 MiB/s, done.
Resolving deltas: 100% (75/75), done.
Filtering content: 100% (236/236), 475.30 MiB | 10.80 MiB/s, done.
prune: 236 local object(s), 0 retained, done.                                   
prune: Deleting objects: 100% (236/236), done.                                  
=======================================================
Dataset (ycb) successfully downloaded.
Source: '/home/liuyi/datasets/habitat/versioned_data/ycb'
Symlink: '/home/liuyi/datasets/habitat/objects/ycb'
=======================================================
--2026-02-10 14:38:12--  https://dl.fbaipublicfiles.com/habitat/data/datasets/rearrange_pick/replica_cad/v0/rearrange_pick_replica_cad_v0.zip
Resolving dl.fbaipublicfiles.com (dl.fbaipublicfiles.com)... 65.8.76.77, 65.8.76.47, 65.8.76.89, ...
Connecting to dl.fbaipublicfiles.com (dl.fbaipublicfiles.com)|65.8.76.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 11648969 (11M) [application/zip]
Saving to: ‘/home/liuyi/datasets/habitat/rearrange_pick_replica_cad_v0.zip’

rearrange_pick_repl 100%[===================>]  11.11M  11.4MB/s    in 1.0s    

2026-02-10 14:38:13 (11.4 MB/s) - ‘/home/liuyi/datasets/habitat/rearrange_pick_replica_cad_v0.zip’ saved [11648969/11648969]

=======================================================
Dataset (rearrange_pick_dataset_v0) successfully downloaded.
Source: '/home/liuyi/datasets/habitat/versioned_data/rearrange_pick_dataset_v0_1.0'
Symlink: '/home/liuyi/datasets/habitat/datasets/rearrange_pick/replica_cad/v0'
=======================================================
--2026-02-10 14:38:13--  https://dl.fbaipublicfiles.com/habitat/data/datasets/replica_cad/v2.zip
Resolving dl.fbaipublicfiles.com (dl.fbaipublicfiles.com)... 65.8.76.89, 65.8.76.35, 65.8.76.47, ...
Connecting to dl.fbaipublicfiles.com (dl.fbaipublicfiles.com)|65.8.76.89|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 214815852 (205M) [application/zip]
Saving to: ‘/home/liuyi/datasets/habitat/v2.zip’

v2.zip              100%[===================>] 204.86M  11.3MB/s    in 18s     

2026-02-10 14:38:32 (11.2 MB/s) - ‘/home/liuyi/datasets/habitat/v2.zip’ saved [214815852/214815852]

=======================================================
Dataset (rearrange_dataset_v2) successfully downloaded.
Source: '/home/liuyi/datasets/habitat/versioned_data/rearrange_dataset_v2_1.0'
Symlink: '/home/liuyi/datasets/habitat/datasets/replica_cad/rearrange'
=======================================================
(habitat) liuyi@liuyi:~/projects/habitat-lab$ python -m habitat_sim.utils.datasets_download   --uids rearrange_task_assets   --data-path "$DATA_ROOT"   --replace^C
(habitat) liuyi@liuyi:~/projects/habitat-lab$ python -m habitat_sim.utils.datasets_download \
  --uids habitat_test_scenes habitat_test_pointnav_dataset \
  --data-path "$DATA_ROOT" \
  --replace
Found the existing repo for (habitat_test_scenes): /home/liuyi/datasets/habitat/versioned_data/habitat_test_scenes
 checking out main and pulling changes from repo.
=======================================================
Generating symlink (/home/liuyi/datasets/habitat/scene_datasets/habitat-test-scenes).
=======================================================
Existing data source (habitat_test_pointnav_dataset) version (1.0) is current. Data located: '/home/liuyi/datasets/habitat/versioned_data/habitat_test_pointnav_dataset_1.0'. Symblink: '/home/liuyi/datasets/habitat/datasets/pointnav/habitat-test-scenes'.
Cleaning datasource (habitat_test_pointnav_dataset). Directory: '/home/liuyi/datasets/habitat/versioned_data/habitat_test_pointnav_dataset_1.0'. Symlink: '/home/liuyi/datasets/habitat/datasets/pointnav/habitat-test-scenes'.
--2026-02-10 14:43:26--  http://dl.fbaipublicfiles.com/habitat/habitat-test-pointnav-dataset_v1.0.zip
Resolving dl.fbaipublicfiles.com (dl.fbaipublicfiles.com)... 65.8.76.35, 65.8.76.89, 65.8.76.47, ...
Connecting to dl.fbaipublicfiles.com (dl.fbaipublicfiles.com)|65.8.76.35|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 894623 (874K) [application/zip]
Saving to: ‘/home/liuyi/datasets/habitat/habitat-test-pointnav-dataset_v1.0.zip’

habitat-test-pointn 100%[===================>] 873.66K  1.51MB/s    in 0.6s    

2026-02-10 14:43:26 (1.51 MB/s) - ‘/home/liuyi/datasets/habitat/habitat-test-pointnav-dataset_v1.0.zip’ saved [894623/894623]

Traceback (most recent call last):
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/habitat_sim-0.3.3-py3.9-linux-x86_64.egg/habitat_sim/utils/datasets_download.py", line 964, in <module>
    main(sys.argv[1:])
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/habitat_sim-0.3.3-py3.9-linux-x86_64.egg/habitat_sim/utils/datasets_download.py", line 953, in main
    download_and_place(
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/habitat_sim-0.3.3-py3.9-linux-x86_64.egg/habitat_sim/utils/datasets_download.py", line 810, in download_and_place
    os.unlink(link_path)
IsADirectoryError: [Errno 21] Is a directory: '/home/liuyi/datasets/habitat/datasets/pointnav/habitat-test-scenes'
(habitat) liuyi@liuyi:~/projects/habitat-lab$ mv "$DATA_ROOT/datasets/pointnav/habitat-test-scenes" \
   "$DATA_ROOT/datasets/pointnav/habitat-test-scenes.bak.$(date +%Y%m%d_%H%M%S)" 
(habitat) liuyi@liuyi:~/projects/habitat-lab$ python -m habitat_sim.utils.datasets_download \
  --uids habitat_test_scenes habitat_test_pointnav_dataset \
  --data-path "$DATA_ROOT" \
  --replace
Found the existing repo for (habitat_test_scenes): /home/liuyi/datasets/habitat/versioned_data/habitat_test_scenes
 checking out main and pulling changes from repo.
=======================================================
Generating symlink (/home/liuyi/datasets/habitat/scene_datasets/habitat-test-scenes).
=======================================================
Existing data source (habitat_test_pointnav_dataset) version (1.0) is current. Data located: '/home/liuyi/datasets/habitat/versioned_data/habitat_test_pointnav_dataset_1.0'. Symblink: '/home/liuyi/datasets/habitat/datasets/pointnav/habitat-test-scenes'.
Cleaning datasource (habitat_test_pointnav_dataset). Directory: '/home/liuyi/datasets/habitat/versioned_data/habitat_test_pointnav_dataset_1.0'. Symlink: '/home/liuyi/datasets/habitat/datasets/pointnav/habitat-test-scenes'.
--2026-02-10 14:44:08--  http://dl.fbaipublicfiles.com/habitat/habitat-test-pointnav-dataset_v1.0.zip
Resolving dl.fbaipublicfiles.com (dl.fbaipublicfiles.com)... 65.8.76.77, 65.8.76.89, 65.8.76.35, ...
Connecting to dl.fbaipublicfiles.com (dl.fbaipublicfiles.com)|65.8.76.77|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 894623 (874K) [application/zip]
Saving to: ‘/home/liuyi/datasets/habitat/habitat-test-pointnav-dataset_v1.0.zip’

habitat-test-pointn 100%[===================>] 873.66K  1.45MB/s    in 0.6s    

2026-02-10 14:44:08 (1.45 MB/s) - ‘/home/liuyi/datasets/habitat/habitat-test-pointnav-dataset_v1.0.zip’ saved [894623/894623]

=======================================================
Dataset (habitat_test_pointnav_dataset) successfully downloaded.
Source: '/home/liuyi/datasets/habitat/versioned_data/habitat_test_pointnav_dataset_1.0'
Symlink: '/home/liuyi/datasets/habitat/datasets/pointnav/habitat-test-scenes'
=======================================================
(habitat) liuyi@liuyi:~/projects/habitat-lab$ test -f data/datasets/replica_cad/rearrange/v2/train/rearrange_easy.json.gz && echo OK_rearrange_v2
test -f data/replica_cad/replicaCAD.scene_dataset_config.json && echo OK_replica_cad
test -d data/objects/ycb/configs && echo OK_ycb
test -f data/robots/hab_fetch/robots/fetch_onlyarm.urdf && echo OK_hab_fetch
OK_rearrange_v2
OK_replica_cad
OK_ycb
OK_hab_fetch
(habitat) liuyi@liuyi:~/projects/habitat-lab$ python examples/example.py
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 14:44:30,970 Initializing dataset RearrangeDataset-v0
2026-02-10 14:44:40,060 initializing sim RearrangeSim-v0
[14:44:40:074192]:[Warning]:[Metadata] AbstractAttributesManager.h(531)::buildAttrSrcPathsFromJSONAndLoad : <Articulated Object> : No Glob path result found for `data/hab_fetch_1.0/robots/fetch_no_base.urdf` so unable to load templates from that path.
[14:44:40:096451]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_00` Value : `navmeshes/v3_sc4_staging_00.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096476]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_01` Value : `navmeshes/v3_sc4_staging_01.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096492]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_02` Value : `navmeshes/v3_sc4_staging_02.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096502]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_03` Value : `navmeshes/v3_sc4_staging_03.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096512]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_04` Value : `navmeshes/v3_sc4_staging_04.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096524]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_05` Value : `navmeshes/v3_sc4_staging_05.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096539]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_06` Value : `navmeshes/v3_sc4_staging_06.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096551]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_07` Value : `navmeshes/v3_sc4_staging_07.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096561]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_08` Value : `navmeshes/v3_sc4_staging_08.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096572]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_09` Value : `navmeshes/v3_sc4_staging_09.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096582]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_10` Value : `navmeshes/v3_sc4_staging_10.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096593]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_11` Value : `navmeshes/v3_sc4_staging_11.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096603]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_12` Value : `navmeshes/v3_sc4_staging_12.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096614]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_13` Value : `navmeshes/v3_sc4_staging_13.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096624]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_14` Value : `navmeshes/v3_sc4_staging_14.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096636]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_15` Value : `navmeshes/v3_sc4_staging_15.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096651]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_16` Value : `navmeshes/v3_sc4_staging_16.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096663]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_17` Value : `navmeshes/v3_sc4_staging_17.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096676]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_18` Value : `navmeshes/v3_sc4_staging_18.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096689]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_19` Value : `navmeshes/v3_sc4_staging_19.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:44:40:096702]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_20` Value : `navmeshes/v3_sc4_staging_20.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
Renderer: NVIDIA GeForce RTX 4060 Laptop GPU/PCIe/SSE2 by NVIDIA Corporation
OpenGL version: 4.6.0 NVIDIA 580.95.05
Using optional features:
    GL_ARB_vertex_array_object
    GL_ARB_separate_shader_objects
    GL_ARB_robustness
    GL_ARB_texture_storage
    GL_ARB_texture_view
    GL_ARB_framebuffer_no_attachments
    GL_ARB_invalidate_subdata
    GL_ARB_texture_storage_multisample
    GL_ARB_multi_bind
    GL_ARB_direct_state_access
    GL_ARB_get_texture_sub_image
    GL_ARB_texture_filter_anisotropic
    GL_KHR_debug
    GL_KHR_parallel_shader_compile
    GL_NV_depth_buffer_float
Using driver workarounds:
    no-forward-compatible-core-context
    nv-egl-incorrect-gl11-function-pointers
    no-layout-qualifiers-on-old-glsl
    nv-zero-context-profile-mask
    nv-implementation-color-read-format-dsa-broken
    nv-cubemap-inconsistent-compressed-image-size
    nv-cubemap-broken-full-compressed-image-query
    nv-compressed-block-size-in-bits
MeshTools::compile(): ignoring Trade::MeshAttribute::TextureCoordinates 1 as its binding slot is already occupied by Trade::MeshAttribute::TextureCoordinates 0
MeshTools::compile(): ignoring Trade::MeshAttribute::TextureCoordinates 1 as its binding slot is already occupied by Trade::MeshAttribute::TextureCoordinates 0
MeshTools::compile(): ignoring Trade::MeshAttribute::TextureCoordinates 1 as its binding slot is already occupied by Trade::MeshAttribute::TextureCoordinates 0
MeshTools::compile(): ignoring Trade::MeshAttribute::TextureCoordinates 1 as its binding slot is already occupied by Trade::MeshAttribute::TextureCoordinates 0
[14:44:42:369479]:[Warning]:[Sim] Simulator.cpp(595)::instanceStageForSceneAttributes : The active scene does not contain semantic annotations : activeSemanticSceneID_ = 0
2026-02-10 14:44:43,893 Initializing task RearrangePickTask-v0
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/gym/spaces/box.py:84: UserWarning: WARN: Box bound precision lowered by casting to float32
  logger.warn(f"Box bound precision lowered by casting to {self.dtype}")
Environment creation successful
b3Warning[examples/Importers/ImportURDFDemo/BulletUrdfImporter.cpp,467]:
Bad inertia tensor properties, setting inertia to zero for link: r_gripper_finger_link
b3Warning[examples/Importers/ImportURDFDemo/BulletUrdfImporter.cpp,467]:
Bad inertia tensor properties, setting inertia to zero for link: l_gripper_finger_link
b3Warning[examples/Importers/ImportURDFDemo/BulletUrdfImporter.cpp,467]:
Bad inertia tensor properties, setting inertia to zero for link: r_gripper_finger_link
b3Warning[examples/Importers/ImportURDFDemo/BulletUrdfImporter.cpp,467]:
Bad inertia tensor properties, setting inertia to zero for link: l_gripper_finger_link
Agent acting inside environment.
Episode finished after 300 steps.
(habitat) liuyi@liuyi:~/projects/habitat-lab$ python examples/interactive_play.py --never-end
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 14:44:59,614 Initializing dataset RearrangeDataset-v0
2026-02-10 14:45:08,799 initializing sim RearrangeSim-v0
[14:45:08:815421]:[Warning]:[Metadata] AbstractAttributesManager.h(531)::buildAttrSrcPathsFromJSONAndLoad : <Articulated Object> : No Glob path result found for `data/hab_fetch_1.0/robots/fetch_no_base.urdf` so unable to load templates from that path.
[14:45:08:844148]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_00` Value : `navmeshes/v3_sc4_staging_00.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844171]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_01` Value : `navmeshes/v3_sc4_staging_01.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844185]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_02` Value : `navmeshes/v3_sc4_staging_02.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844194]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_03` Value : `navmeshes/v3_sc4_staging_03.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844202]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_04` Value : `navmeshes/v3_sc4_staging_04.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844210]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_05` Value : `navmeshes/v3_sc4_staging_05.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844218]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_06` Value : `navmeshes/v3_sc4_staging_06.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844227]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_07` Value : `navmeshes/v3_sc4_staging_07.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844235]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_08` Value : `navmeshes/v3_sc4_staging_08.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844243]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_09` Value : `navmeshes/v3_sc4_staging_09.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844251]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_10` Value : `navmeshes/v3_sc4_staging_10.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844259]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_11` Value : `navmeshes/v3_sc4_staging_11.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844269]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_12` Value : `navmeshes/v3_sc4_staging_12.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844282]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_13` Value : `navmeshes/v3_sc4_staging_13.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844291]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_14` Value : `navmeshes/v3_sc4_staging_14.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844302]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_15` Value : `navmeshes/v3_sc4_staging_15.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844311]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_16` Value : `navmeshes/v3_sc4_staging_16.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844320]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_17` Value : `navmeshes/v3_sc4_staging_17.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844330]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_18` Value : `navmeshes/v3_sc4_staging_18.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844339]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_19` Value : `navmeshes/v3_sc4_staging_19.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
[14:45:08:844352]:[Error]:[Metadata] SceneDatasetAttributesManager.cpp(305)::validateMap : `navmesh_instances` Key : `v3_sc4_staging_20` Value : `navmeshes/v3_sc4_staging_20.navmesh` not found on disk as absolute path or relative to `data/replica_cad`
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
Renderer: NVIDIA GeForce RTX 4060 Laptop GPU/PCIe/SSE2 by NVIDIA Corporation
OpenGL version: 4.6.0 NVIDIA 580.95.05
Using optional features:
    GL_ARB_vertex_array_object
    GL_ARB_separate_shader_objects
    GL_ARB_robustness
    GL_ARB_texture_storage
    GL_ARB_texture_view
    GL_ARB_framebuffer_no_attachments
    GL_ARB_invalidate_subdata
    GL_ARB_texture_storage_multisample
    GL_ARB_multi_bind
    GL_ARB_direct_state_access
    GL_ARB_get_texture_sub_image
    GL_ARB_texture_filter_anisotropic
    GL_KHR_debug
    GL_KHR_parallel_shader_compile
    GL_NV_depth_buffer_float
Using driver workarounds:
    no-forward-compatible-core-context
    nv-egl-incorrect-gl11-function-pointers
    no-layout-qualifiers-on-old-glsl
    nv-zero-context-profile-mask
    nv-implementation-color-read-format-dsa-broken
    nv-cubemap-inconsistent-compressed-image-size
    nv-cubemap-broken-full-compressed-image-query
    nv-compressed-block-size-in-bits
MeshTools::compile(): ignoring Trade::MeshAttribute::TextureCoordinates 1 as its binding slot is already occupied by Trade::MeshAttribute::TextureCoordinates 0
MeshTools::compile(): ignoring Trade::MeshAttribute::TextureCoordinates 1 as its binding slot is already occupied by Trade::MeshAttribute::TextureCoordinates 0
MeshTools::compile(): ignoring Trade::MeshAttribute::TextureCoordinates 1 as its binding slot is already occupied by Trade::MeshAttribute::TextureCoordinates 0
MeshTools::compile(): ignoring Trade::MeshAttribute::TextureCoordinates 1 as its binding slot is already occupied by Trade::MeshAttribute::TextureCoordinates 0
[14:45:11:117966]:[Warning]:[Sim] Simulator.cpp(595)::instanceStageForSceneAttributes : The active scene does not contain semantic annotations : activeSemanticSceneID_ = 0
2026-02-10 14:45:12,652 Initializing task RearrangeEmptyTask-v0
b3Warning[examples/Importers/ImportURDFDemo/BulletUrdfImporter.cpp,467]:
Bad inertia tensor properties, setting inertia to zero for link: r_gripper_finger_link
b3Warning[examples/Importers/ImportURDFDemo/BulletUrdfImporter.cpp,467]:
Bad inertia tensor properties, setting inertia to zero for link: l_gripper_finger_link
b3Warning[examples/Importers/ImportURDFDemo/BulletUrdfImporter.cpp,467]:
Bad inertia tensor properties, setting inertia to zero for link: r_gripper_finger_link
b3Warning[examples/Importers/ImportURDFDemo/BulletUrdfImporter.cpp,467]:
Bad inertia tensor properties, setting inertia to zero for link: l_gripper_finger_link
X Error of failed request:  BadAccess (attempt to access private resource denied)
  Major opcode of failed request:  152 (GLX)
  Minor opcode of failed request:  5 (X_GLXMakeCurrent)
  Serial number of failed request:  170
  Current serial number in output stream:  170
(habitat) liuyi@liuyi:~/projects/habitat-lab$ cd ~/projects/habitat-lab
conda activate habitat
export TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD=1
(habitat) liuyi@liuyi:~/projects/habitat-lab$ # 先熟悉训练流程（DDPPO，test scenes，小步数）
python -u -m habitat_baselines.run \
  --config-name=pointnav/ppo_pointnav_example.yaml \
  habitat_baselines.trainer_name=ddppo \
  habitat_baselines.load_resume_state_config=False \
  habitat_baselines.num_environments=1 \
  habitat_baselines.total_num_steps=3200 \
  habitat_baselines.log_interval=1 \
  habitat_baselines.checkpoint_folder=data/new_checkpoints_ddppo_demo \
  habitat_baselines.eval_ckpt_path_dir=data/new_checkpoints_ddppo_demo
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 14:50:42,131 config: habitat:
  seed: 100
  env_task: GymHabitatEnv
  env_task_gym_dependencies: []
  env_task_gym_id: ''
  environment:
    max_episode_steps: 500
    max_episode_seconds: 10000000
    iterator_options:
      cycle: true
      shuffle: true
      group_by_scene: true
      num_episode_sample: -1
      max_scene_repeat_episodes: -1
      max_scene_repeat_steps: 10000
      step_repetition_range: 0.2
  simulator:
    type: Sim-v0
    forward_step_size: 0.25
    turn_angle: 10
    create_renderer: false
    requires_textures: true
    auto_sleep: false
    step_physics: true
    concur_render: false
    needs_markers: true
    update_articulated_agent: true
    scene: data/scene_datasets/habitat-test-scenes/van-gogh-room.glb
    scene_dataset: default
    additional_object_paths: []
    seed: ${habitat.seed}
    default_agent_id: 0
    debug_render: false
    debug_render_articulated_agent: false
    kinematic_mode: false
    should_setup_semantic_ids: true
    debug_render_goal: true
    robot_joint_start_noise: 0.0
    ctrl_freq: 120.0
    ac_freq_ratio: 4
    load_objs: true
    hold_thresh: 0.15
    grasp_impulse: 10000.0
    agents:
      main_agent:
        height: 1.5
        radius: 0.1
        max_climb: 0.2
        max_slope: 45.0
        grasp_managers: 1
        sim_sensors:
          rgb_sensor:
            type: HabitatSimRGBSensor
            height: 256
            width: 256
            position:
            - 0.0
            - 1.25
            - 0.0
            orientation:
            - 0.0
            - 0.0
            - 0.0
            hfov: 90
            sensor_subtype: PINHOLE
            noise_model: None
            noise_model_kwargs: {}
          depth_sensor:
            type: HabitatSimDepthSensor
            height: 256
            width: 256
            position:
            - 0.0
            - 1.25
            - 0.0
            orientation:
            - 0.0
            - 0.0
            - 0.0
            hfov: 90
            sensor_subtype: PINHOLE
            noise_model: None
            noise_model_kwargs: {}
            min_depth: 0.0
            max_depth: 10.0
            normalize_depth: true
        is_set_start_state: false
        start_position:
        - 0.0
        - 0.0
        - 0.0
        start_rotation:
        - 0.0
        - 0.0
        - 0.0
        - 1.0
        joint_start_noise: 0.1
        joint_that_can_control: null
        joint_start_override: null
        articulated_agent_urdf: null
        articulated_agent_type: null
        ik_arm_urdf: null
        motion_data_path: ''
        auto_update_sensor_transform: true
    agents_order:
    - main_agent
    default_agent_navmesh: true
    navmesh_include_static_objects: false
    habitat_sim_v0:
      gpu_device_id: 0
      gpu_gpu: false
      allow_sliding: true
      frustum_culling: true
      enable_physics: false
      enable_hbao: false
      physics_config_file: ./data/default.physics_config.json
      leave_context_with_background_renderer: false
      enable_gfx_replay_save: false
    ep_info: null
    object_ids_start: 100
    renderer:
      enable_batch_renderer: false
      composite_files: null
      classic_replay_renderer: false
  task:
    physics_target_sps: 60.0
    reward_measure: distance_to_goal_reward
    success_measure: spl
    success_reward: 2.5
    slack_reward: -0.01
    end_on_success: true
    type: Nav-v0
    lab_sensors:
      pointgoal_with_gps_compass_sensor:
        type: PointGoalWithGPSCompassSensor
        goal_format: POLAR
        dimensionality: 2
    measurements:
      distance_to_goal:
        type: DistanceToGoal
        distance_to: POINT
      success:
        type: Success
        success_distance: 0.2
      spl:
        type: SPL
      distance_to_goal_reward:
        type: DistanceToGoalReward
    rank0_env0_measure_names:
    - habitat_perf
    rank0_measure_names: []
    goal_sensor_uuid: pointgoal_with_gps_compass
    count_obj_collisions: true
    settle_steps: 5
    constraint_violation_ends_episode: true
    constraint_violation_drops_object: false
    force_regenerate: false
    should_save_to_cache: false
    object_in_hand_sample_prob: 0.167
    min_start_distance: 3.0
    render_target: true
    filter_colliding_states: true
    num_spawn_attempts: 200
    spawn_max_dist_to_obj: 2.0
    base_angle_noise: 0.523599
    spawn_max_dist_to_obj_delta: 0.02
    recep_place_shrink_factor: 0.8
    ee_sample_factor: 0.2
    ee_exclude_region: 0.0
    base_noise: 0.05
    spawn_region_scale: 0.2
    joint_max_impulse: -1.0
    desired_resting_position:
    - 0.5
    - 0.0
    - 1.0
    use_marker_t: true
    cache_robot_init: false
    success_state: 0.0
    should_enforce_target_within_reach: false
    task_spec_base_path: habitat/task/rearrange/pddl/
    task_spec: ''
    pddl_domain_def: replica_cad
    obj_succ_thresh: 0.3
    enable_safe_drop: false
    art_succ_thresh: 0.15
    robot_at_thresh: 2.0
    min_distance_start_agents: -1.0
    actions:
      stop:
        type: StopAction
      move_forward:
        type: MoveForwardAction
        tilt_angle: 15
      turn_left:
        type: TurnLeftAction
        tilt_angle: 15
      turn_right:
        type: TurnRightAction
        tilt_angle: 15
  dataset:
    type: PointNav-v1
    split: train
    scenes_dir: data/scene_datasets
    content_scenes:
    - '*'
    data_path: data/datasets/pointnav/habitat-test-scenes/v1/{split}/{split}.json.gz
    metadata: null
  gym:
    obs_keys: null
    action_keys: null
    achieved_goal_keys: []
    desired_goal_keys: []
habitat_baselines:
  evaluate: false
  trainer_name: ddppo
  updater_name: PPO
  distrib_updater_name: DDPPO
  torch_gpu_id: 0
  tensorboard_dir: tb
  writer_type: tb
  video_dir: video_dir
  video_fps: 10
  test_episode_count: 2
  eval_ckpt_path_dir: data/new_checkpoints_ddppo_demo
  num_environments: 1
  num_processes: -1
  rollout_storage_name: RolloutStorage
  checkpoint_folder: data/new_checkpoints_ddppo_demo
  num_updates: -1
  num_checkpoints: 50
  checkpoint_interval: -1
  total_num_steps: 3200.0
  log_interval: 1
  log_file: train.log
  force_blind_policy: false
  verbose: true
  vector_env_factory:
    _target_: habitat_baselines.common.HabitatVectorEnvFactory
  evaluator:
    _target_: habitat_baselines.rl.ppo.habitat_evaluator.HabitatEvaluator
  eval_keys_to_include_in_name: []
  force_torch_single_threaded: true
  wb:
    project_name: ''
    entity: ''
    group: ''
    run_name: ''
  load_resume_state_config: false
  eval:
    split: val
    use_ckpt_config: true
    should_load_ckpt: true
    evals_per_ep: 1
    video_option:
    - disk
    - tensorboard
    extra_sim_sensors: {}
  profiling:
    capture_start_step: -1
    num_steps_to_capture: -1
  should_log_single_proc_infos: false
  on_save_ckpt_callback: null
  rl:
    agent:
      type: SingleAgentAccessMgr
      num_agent_types: 1
      num_active_agents_per_type:
      - 1
      num_pool_agents_per_type:
      - 1
      agent_sample_interval: 20
      force_partner_sample_idx: -1
      behavior_latent_dim: -1
      force_all_agents: false
      discrim_reward_weight: 1.0
      allow_self_play: false
      self_play_batched: false
      load_type1_pop_ckpts: null
    preemption:
      append_slurm_job_id: false
      save_resume_state_interval: 100
      save_state_batch_only: false
    policy:
      main_agent:
        name: PointNavResNetPolicy
        action_distribution_type: categorical
        action_dist:
          use_log_std: true
          use_softplus: false
          std_init: ???
          log_std_init: 0.0
          use_std_param: false
          clamp_std: true
          min_std: 1.0e-06
          max_std: 1
          min_log_std: -5
          max_log_std: 2
          action_activation: tanh
          scheduled_std: false
        obs_transforms: {}
        hierarchical_policy: ???
    ppo:
      clip_param: 0.1
      ppo_epoch: 1
      num_mini_batch: 1
      value_loss_coef: 0.5
      entropy_coef: 0.01
      lr: 0.00025
      eps: 1.0e-05
      max_grad_norm: 0.5
      num_steps: 32
      use_gae: true
      use_linear_lr_decay: true
      use_linear_clip_decay: true
      gamma: 0.99
      tau: 0.95
      reward_window_size: 50
      use_normalized_advantage: false
      hidden_size: 512
      entropy_target_factor: 0.0
      use_adaptive_entropy_pen: false
      use_clipped_value_loss: true
      use_double_buffered_sampler: false
    ddppo:
      sync_frac: 0.6
      distrib_backend: GLOO
      rnn_type: GRU
      num_recurrent_layers: 1
      backbone: resnet18
      pretrained_weights: data/ddppo-models/gibson-2plus-resnet50.pth
      pretrained: false
      pretrained_encoder: false
      train_encoder: true
      reset_critic: true
      force_distributed: false
    ver:
      variable_experience: true
      num_inference_workers: 2
      overlap_rollouts_and_learn: false
    auxiliary_losses: {}

2026-02-10 14:50:42,132 Initializing dataset PointNav-v1
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 14:50:44,819 Initializing dataset PointNav-v1
2026-02-10 14:50:45,019 initializing sim Sim-v0
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
Renderer: NVIDIA GeForce RTX 4060 Laptop GPU/PCIe/SSE2 by NVIDIA Corporation
OpenGL version: 4.6.0 NVIDIA 580.95.05
Using optional features:
    GL_ARB_vertex_array_object
    GL_ARB_separate_shader_objects
    GL_ARB_robustness
    GL_ARB_texture_storage
    GL_ARB_texture_view
    GL_ARB_framebuffer_no_attachments
    GL_ARB_invalidate_subdata
    GL_ARB_texture_storage_multisample
    GL_ARB_multi_bind
    GL_ARB_direct_state_access
    GL_ARB_get_texture_sub_image
    GL_ARB_texture_filter_anisotropic
    GL_KHR_debug
    GL_KHR_parallel_shader_compile
    GL_NV_depth_buffer_float
Using driver workarounds:
    no-forward-compatible-core-context
    nv-egl-incorrect-gl11-function-pointers
    no-layout-qualifiers-on-old-glsl
    nv-zero-context-profile-mask
    nv-implementation-color-read-format-dsa-broken
    nv-cubemap-inconsistent-compressed-image-size
    nv-cubemap-broken-full-compressed-image-query
    nv-compressed-block-size-in-bits
[14:50:45:095993]:[Warning]:[Metadata] SceneDatasetAttributes.cpp(107)::addNewSceneInstanceToDataset : Dataset : 'default' : Lighting Layout Attributes 'no_lights' specified in Scene Attributes but does not exist in dataset, so creating default.
[14:50:45:098427]:[Warning]:[Scene] SemanticScene.h(331)::checkFileExists : ::loadSemanticSceneDescriptor: File `data/scene_datasets/habitat-test-scenes/skokloster-castle.scn` does not exist.  Aborting load.
[14:50:45:098441]:[Warning]:[Scene] SemanticScene.cpp(123)::loadSemanticSceneDescriptor : SSD File Naming Issue! Neither SemanticAttributes-provided name : `data/scene_datasets/habitat-test-scenes/skokloster-castle.scn` nor constructed filename : `data/scene_datasets/habitat-test-scenes/info_semantic.json` exist on disk.
[14:50:45:098448]:[Error]:[Scene] SemanticScene.cpp(139)::loadSemanticSceneDescriptor : SSD Load Failure! File with SemanticAttributes-provided name `data/scene_datasets/habitat-test-scenes/skokloster-castle.scn` exists but failed to load.
[14:50:45:843565]:[Warning]:[Sim] Simulator.cpp(595)::instanceStageForSceneAttributes : The active scene does not contain semantic annotations : activeSemanticSceneID_ = 0
2026-02-10 14:50:45,845 Initializing task Nav-v0
2026-02-10 14:50:46,277 Number of params to train: 5821797
2026-02-10 14:50:46,278 Agent number of parameters: 5821797
2026-02-10 14:50:46,968 update: 1	fps: 47.208	
2026-02-10 14:50:46,968 Num updates: 1	Num frames 32
2026-02-10 14:50:46,968 Average window size: 1  distance_to_goal: 7.466  distance_to_goal_reward: 0.000  reward: -0.075  spl: 0.000  success: 0.000
2026-02-10 14:50:46,968 	Perf Stats: trainer.rollout_collect: 0.510 trainer.sample_action: 0.012 trainer.obs_insert: 0.000 trainer.step_env: 0.003 trainer.update_stats: 0.000 trainer.update_agent: 0.165
2026-02-10 14:50:47,239 update: 2	fps: 67.443	
2026-02-10 14:50:47,239 Num updates: 2	Num frames 64
2026-02-10 14:50:47,239 Average window size: 2  distance_to_goal: 10.333  distance_to_goal_reward: 0.000  reward: -0.009  spl: 0.000  success: 0.000
2026-02-10 14:50:47,239 	Perf Stats: trainer.rollout_collect: 0.354 trainer.sample_action: 0.007 trainer.obs_insert: 0.000 trainer.step_env: 0.003 trainer.update_stats: 0.000 trainer.update_agent: 0.092
2026-02-10 14:50:47,496 update: 3	fps: 79.607	
2026-02-10 14:50:47,497 Num updates: 3	Num frames 96
2026-02-10 14:50:47,497 Average window size: 3  distance_to_goal: 8.936  distance_to_goal_reward: 0.000  reward: -0.088  spl: 0.000  success: 0.000
2026-02-10 14:50:47,497 	Perf Stats: trainer.rollout_collect: 0.315 trainer.sample_action: 0.005 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.068
2026-02-10 14:50:47,730 update: 4	fps: 88.911	
2026-02-10 14:50:47,730 Num updates: 4	Num frames 128
2026-02-10 14:50:47,730 Average window size: 4  distance_to_goal: 8.912  distance_to_goal_reward: 0.000  reward: -0.037  spl: 0.000  success: 0.000
2026-02-10 14:50:47,730 	Perf Stats: trainer.rollout_collect: 0.289 trainer.sample_action: 0.005 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.055
2026-02-10 14:50:48,010 update: 5	fps: 93.010	
2026-02-10 14:50:48,010 Num updates: 5	Num frames 160
2026-02-10 14:50:48,010 Average window size: 5  distance_to_goal: 9.111  distance_to_goal_reward: 0.000  reward: -0.013  spl: 0.000  success: 0.000
2026-02-10 14:50:48,010 	Perf Stats: trainer.rollout_collect: 0.273 trainer.sample_action: 0.004 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.048
2026-02-10 14:50:48,233 update: 6	fps: 98.829	
2026-02-10 14:50:48,233 Num updates: 6	Num frames 192
2026-02-10 14:50:48,233 Average window size: 6  distance_to_goal: 9.142  distance_to_goal_reward: 0.000  reward: -0.046  spl: 0.000  success: 0.000
2026-02-10 14:50:48,233 	Perf Stats: trainer.rollout_collect: 0.261 trainer.sample_action: 0.004 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.043
2026-02-10 14:50:48,450 update: 7	fps: 103.689	
2026-02-10 14:50:48,450 Num updates: 7	Num frames 224
2026-02-10 14:50:48,451 Average window size: 7  distance_to_goal: 9.021  distance_to_goal_reward: 0.000  reward: -0.070  spl: 0.000  success: 0.000
2026-02-10 14:50:48,451 	Perf Stats: trainer.rollout_collect: 0.252 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.040
2026-02-10 14:50:48,699 update: 8	fps: 106.257	
2026-02-10 14:50:48,699 Num updates: 8	Num frames 256
2026-02-10 14:50:48,699 Average window size: 8  distance_to_goal: 8.732  distance_to_goal_reward: 0.000  reward: -0.073  spl: 0.000  success: 0.000
2026-02-10 14:50:48,699 	Perf Stats: trainer.rollout_collect: 0.242 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.037
2026-02-10 14:50:48,904 update: 9	fps: 110.166	
2026-02-10 14:50:48,905 Num updates: 9	Num frames 288
2026-02-10 14:50:48,905 Average window size: 9  distance_to_goal: 8.684  distance_to_goal_reward: 0.000  reward: -0.070  spl: 0.000  success: 0.000
2026-02-10 14:50:48,905 	Perf Stats: trainer.rollout_collect: 0.236 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.035
2026-02-10 14:50:49,129 update: 10	fps: 112.721	
2026-02-10 14:50:49,129 Num updates: 10	Num frames 320
2026-02-10 14:50:49,129 Average window size: 10  distance_to_goal: 8.794  distance_to_goal_reward: 0.000  reward: -0.057  spl: 0.000  success: 0.000
2026-02-10 14:50:49,129 	Perf Stats: trainer.rollout_collect: 0.232 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.034
2026-02-10 14:50:49,425 update: 11	fps: 112.272	
2026-02-10 14:50:49,426 Num updates: 11	Num frames 352
2026-02-10 14:50:49,426 Average window size: 11  distance_to_goal: 8.670  distance_to_goal_reward: 0.000  reward: -0.061  spl: 0.000  success: 0.000
2026-02-10 14:50:49,426 	Perf Stats: trainer.rollout_collect: 0.231 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.032
2026-02-10 14:50:49,685 update: 12	fps: 113.117	
2026-02-10 14:50:49,685 Num updates: 12	Num frames 384
2026-02-10 14:50:49,685 Average window size: 12  distance_to_goal: 8.685  distance_to_goal_reward: 0.000  reward: -0.077  spl: 0.000  success: 0.000
2026-02-10 14:50:49,685 	Perf Stats: trainer.rollout_collect: 0.232 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.031
2026-02-10 14:50:49,936 update: 13	fps: 114.110	
2026-02-10 14:50:49,936 Num updates: 13	Num frames 416
2026-02-10 14:50:49,936 Average window size: 13  distance_to_goal: 8.652  distance_to_goal_reward: 0.000  reward: -0.061  spl: 0.000  success: 0.000
2026-02-10 14:50:49,936 	Perf Stats: trainer.rollout_collect: 0.232 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.030
2026-02-10 14:50:50,248 update: 14	fps: 113.188	
2026-02-10 14:50:50,248 Num updates: 14	Num frames 448
2026-02-10 14:50:50,248 Average window size: 14  distance_to_goal: 8.770  distance_to_goal_reward: 0.000  reward: -0.053  spl: 0.000  success: 0.000
2026-02-10 14:50:50,248 	Perf Stats: trainer.rollout_collect: 0.230 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.030
2026-02-10 14:50:50,493 update: 15	fps: 114.194	
2026-02-10 14:50:50,494 Num updates: 15	Num frames 480
2026-02-10 14:50:50,494 Average window size: 15  distance_to_goal: 8.673  distance_to_goal_reward: 0.000  reward: -0.039  spl: 0.000  success: 0.000
2026-02-10 14:50:50,494 	Perf Stats: trainer.rollout_collect: 0.230 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.029
2026-02-10 14:50:50,727 update: 16	fps: 115.399	
2026-02-10 14:50:50,727 Num updates: 16	Num frames 512
2026-02-10 14:50:50,727 Average window size: 16  distance_to_goal: 8.683  distance_to_goal_reward: 0.000  reward: -0.039  spl: 0.000  success: 0.000
2026-02-10 14:50:50,727 	Perf Stats: trainer.rollout_collect: 0.229 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.028
2026-02-10 14:50:51,018 update: 17	fps: 115.064	
2026-02-10 14:50:51,018 Num updates: 17	Num frames 544
2026-02-10 14:50:51,018 Average window size: 17  distance_to_goal: 8.789  distance_to_goal_reward: 0.000  reward: -0.040  spl: 0.000  success: 0.000
2026-02-10 14:50:51,018 	Perf Stats: trainer.rollout_collect: 0.227 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.028
2026-02-10 14:50:51,282 update: 18	fps: 115.399	
2026-02-10 14:50:51,282 Num updates: 18	Num frames 576
2026-02-10 14:50:51,282 Average window size: 18  distance_to_goal: 8.807  distance_to_goal_reward: 0.000  reward: -0.039  spl: 0.000  success: 0.000
2026-02-10 14:50:51,282 	Perf Stats: trainer.rollout_collect: 0.228 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.027
2026-02-10 14:50:51,554 update: 19	fps: 115.488	
2026-02-10 14:50:51,555 Num updates: 19	Num frames 608
2026-02-10 14:50:51,555 Average window size: 19  distance_to_goal: 8.854  distance_to_goal_reward: 0.000  reward: -0.039  spl: 0.000  success: 0.000
2026-02-10 14:50:51,555 	Perf Stats: trainer.rollout_collect: 0.230 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.027
2026-02-10 14:50:51,819 update: 20	fps: 115.756	
2026-02-10 14:50:51,819 Num updates: 20	Num frames 640
2026-02-10 14:50:51,819 Average window size: 20  distance_to_goal: 8.736  distance_to_goal_reward: 0.000  reward: -0.032  spl: 0.000  success: 0.000
2026-02-10 14:50:51,819 	Perf Stats: trainer.rollout_collect: 0.227 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.026
2026-02-10 14:50:52,107 update: 21	fps: 115.524	
2026-02-10 14:50:52,107 Num updates: 21	Num frames 672
2026-02-10 14:50:52,107 Average window size: 21  distance_to_goal: 8.621  distance_to_goal_reward: 0.000  reward: -0.031  spl: 0.000  success: 0.000
2026-02-10 14:50:52,107 	Perf Stats: trainer.rollout_collect: 0.229 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.026
2026-02-10 14:50:52,352 update: 22	fps: 116.129	
2026-02-10 14:50:52,352 Num updates: 22	Num frames 704
2026-02-10 14:50:52,352 Average window size: 22  distance_to_goal: 8.703  distance_to_goal_reward: 0.000  reward: -0.029  spl: 0.000  success: 0.000
2026-02-10 14:50:52,352 	Perf Stats: trainer.rollout_collect: 0.229 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.026
2026-02-10 14:50:52,658 update: 23	fps: 115.573	
2026-02-10 14:50:52,658 Num updates: 23	Num frames 736
2026-02-10 14:50:52,659 Average window size: 23  distance_to_goal: 8.698  distance_to_goal_reward: 0.000  reward: -0.027  spl: 0.000  success: 0.000
2026-02-10 14:50:52,659 	Perf Stats: trainer.rollout_collect: 0.229 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.025
2026-02-10 14:50:52,868 update: 24	fps: 116.760	
2026-02-10 14:50:52,868 Num updates: 24	Num frames 768
2026-02-10 14:50:52,868 Average window size: 24  distance_to_goal: 8.631  distance_to_goal_reward: 0.000  reward: -0.029  spl: 0.000  success: 0.000
2026-02-10 14:50:52,868 	Perf Stats: trainer.rollout_collect: 0.227 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.025
2026-02-10 14:50:53,098 update: 25	fps: 117.514	
2026-02-10 14:50:53,098 Num updates: 25	Num frames 800
2026-02-10 14:50:53,098 Average window size: 25  distance_to_goal: 8.664  distance_to_goal_reward: 0.000  reward: -0.023  spl: 0.000  success: 0.000
2026-02-10 14:50:53,098 	Perf Stats: trainer.rollout_collect: 0.226 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.025
2026-02-10 14:50:53,393 update: 26	fps: 117.136	
2026-02-10 14:50:53,393 Num updates: 26	Num frames 832
2026-02-10 14:50:53,393 Average window size: 26  distance_to_goal: 8.689  distance_to_goal_reward: 0.000  reward: -0.021  spl: 0.000  success: 0.000
2026-02-10 14:50:53,393 	Perf Stats: trainer.rollout_collect: 0.226 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.025
2026-02-10 14:50:53,618 update: 27	fps: 117.907	
2026-02-10 14:50:53,618 Num updates: 27	Num frames 864
2026-02-10 14:50:53,618 Average window size: 27  distance_to_goal: 8.712  distance_to_goal_reward: 0.000  reward: -0.023  spl: 0.000  success: 0.000
2026-02-10 14:50:53,618 	Perf Stats: trainer.rollout_collect: 0.225 trainer.sample_action: 0.003 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.025
2026-02-10 14:50:53,831 update: 28	fps: 118.817	
2026-02-10 14:50:53,831 Num updates: 28	Num frames 896
2026-02-10 14:50:53,831 Average window size: 28  distance_to_goal: 8.761  distance_to_goal_reward: 0.000  reward: -0.024  spl: 0.000  success: 0.000
2026-02-10 14:50:53,831 	Perf Stats: trainer.rollout_collect: 0.224 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.024
2026-02-10 14:50:54,097 update: 29	fps: 118.873	
2026-02-10 14:50:54,097 Num updates: 29	Num frames 928
2026-02-10 14:50:54,097 Average window size: 29  distance_to_goal: 8.664  distance_to_goal_reward: 0.000  reward: -0.026  spl: 0.000  success: 0.000
2026-02-10 14:50:54,097 	Perf Stats: trainer.rollout_collect: 0.223 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.024
2026-02-10 14:50:54,317 update: 30	fps: 119.594	
2026-02-10 14:50:54,317 Num updates: 30	Num frames 960
2026-02-10 14:50:54,317 Average window size: 30  distance_to_goal: 8.601  distance_to_goal_reward: 0.000  reward: -0.022  spl: 0.000  success: 0.000
2026-02-10 14:50:54,317 	Perf Stats: trainer.rollout_collect: 0.222 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.024
2026-02-10 14:50:54,519 update: 31	fps: 120.558	
2026-02-10 14:50:54,519 Num updates: 31	Num frames 992
2026-02-10 14:50:54,519 Average window size: 31  distance_to_goal: 8.595  distance_to_goal_reward: 0.000  reward: -0.020  spl: 0.000  success: 0.000
2026-02-10 14:50:54,519 	Perf Stats: trainer.rollout_collect: 0.221 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.024
2026-02-10 14:50:54,813 update: 32	fps: 120.142	
2026-02-10 14:50:54,813 Num updates: 32	Num frames 1024
2026-02-10 14:50:54,813 Average window size: 32  distance_to_goal: 8.555  distance_to_goal_reward: 0.000  reward: -0.016  spl: 0.000  success: 0.000
2026-02-10 14:50:54,813 	Perf Stats: trainer.rollout_collect: 0.220 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.024
2026-02-10 14:50:55,052 update: 33	fps: 120.523	
2026-02-10 14:50:55,052 Num updates: 33	Num frames 1056
2026-02-10 14:50:55,052 Average window size: 33  distance_to_goal: 8.571  distance_to_goal_reward: 0.000  reward: -0.016  spl: 0.000  success: 0.000
2026-02-10 14:50:55,052 	Perf Stats: trainer.rollout_collect: 0.220 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.024
2026-02-10 14:50:55,259 update: 34	fps: 121.315	
2026-02-10 14:50:55,259 Num updates: 34	Num frames 1088
2026-02-10 14:50:55,259 Average window size: 34  distance_to_goal: 8.588  distance_to_goal_reward: 0.000  reward: -0.016  spl: 0.000  success: 0.000
2026-02-10 14:50:55,259 	Perf Stats: trainer.rollout_collect: 0.219 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.023
2026-02-10 14:50:55,544 update: 35	fps: 121.034	
2026-02-10 14:50:55,544 Num updates: 35	Num frames 1120
2026-02-10 14:50:55,544 Average window size: 35  distance_to_goal: 8.602  distance_to_goal_reward: 0.000  reward: -0.014  spl: 0.000  success: 0.000
2026-02-10 14:50:55,544 	Perf Stats: trainer.rollout_collect: 0.219 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.023
2026-02-10 14:50:55,766 update: 36	fps: 121.568	
2026-02-10 14:50:55,766 Num updates: 36	Num frames 1152
2026-02-10 14:50:55,766 Average window size: 36  distance_to_goal: 8.645  distance_to_goal_reward: 0.000  reward: -0.014  spl: 0.000  success: 0.000
2026-02-10 14:50:55,766 	Perf Stats: trainer.rollout_collect: 0.219 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.023
2026-02-10 14:50:55,974 update: 37	fps: 122.258	
2026-02-10 14:50:55,974 Num updates: 37	Num frames 1184
2026-02-10 14:50:55,974 Average window size: 37  distance_to_goal: 8.634  distance_to_goal_reward: 0.000  reward: -0.013  spl: 0.000  success: 0.000
2026-02-10 14:50:55,974 	Perf Stats: trainer.rollout_collect: 0.218 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.023
2026-02-10 14:50:56,249 update: 38	fps: 122.102	
2026-02-10 14:50:56,249 Num updates: 38	Num frames 1216
2026-02-10 14:50:56,249 Average window size: 38  distance_to_goal: 8.631  distance_to_goal_reward: 0.000  reward: -0.014  spl: 0.000  success: 0.000
2026-02-10 14:50:56,249 	Perf Stats: trainer.rollout_collect: 0.218 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.023
2026-02-10 14:50:56,488 update: 39	fps: 122.379	
2026-02-10 14:50:56,488 Num updates: 39	Num frames 1248
2026-02-10 14:50:56,488 Average window size: 39  distance_to_goal: 8.629  distance_to_goal_reward: 0.000  reward: -0.016  spl: 0.000  success: 0.000
2026-02-10 14:50:56,488 	Perf Stats: trainer.rollout_collect: 0.217 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.023
2026-02-10 14:50:56,705 update: 40	fps: 122.903	
2026-02-10 14:50:56,705 Num updates: 40	Num frames 1280
2026-02-10 14:50:56,705 Average window size: 40  distance_to_goal: 8.669  distance_to_goal_reward: 0.000  reward: -0.018  spl: 0.000  success: 0.000
2026-02-10 14:50:56,705 	Perf Stats: trainer.rollout_collect: 0.217 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.023
2026-02-10 14:50:56,978 update: 41	fps: 122.755	
2026-02-10 14:50:56,978 Num updates: 41	Num frames 1312
2026-02-10 14:50:56,978 Average window size: 41  distance_to_goal: 8.705  distance_to_goal_reward: 0.000  reward: -0.011  spl: 0.000  success: 0.000
2026-02-10 14:50:56,978 	Perf Stats: trainer.rollout_collect: 0.217 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.023
2026-02-10 14:50:57,202 update: 42	fps: 123.170	
2026-02-10 14:50:57,202 Num updates: 42	Num frames 1344
2026-02-10 14:50:57,202 Average window size: 42  distance_to_goal: 8.714  distance_to_goal_reward: 0.000  reward: -0.011  spl: 0.000  success: 0.000
2026-02-10 14:50:57,202 	Perf Stats: trainer.rollout_collect: 0.216 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.023
2026-02-10 14:50:57,413 update: 43	fps: 123.711	
2026-02-10 14:50:57,413 Num updates: 43	Num frames 1376
2026-02-10 14:50:57,413 Average window size: 43  distance_to_goal: 8.772  distance_to_goal_reward: 0.000  reward: -0.009  spl: 0.000  success: 0.000
2026-02-10 14:50:57,413 	Perf Stats: trainer.rollout_collect: 0.216 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.023
2026-02-10 14:50:57,678 update: 44	fps: 123.640	
2026-02-10 14:50:57,678 Num updates: 44	Num frames 1408
2026-02-10 14:50:57,678 Average window size: 44  distance_to_goal: 8.770  distance_to_goal_reward: 0.000  reward: -0.011  spl: 0.000  success: 0.000
2026-02-10 14:50:57,678 	Perf Stats: trainer.rollout_collect: 0.215 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.022
2026-02-10 14:50:57,904 update: 45	fps: 123.988	
2026-02-10 14:50:57,904 Num updates: 45	Num frames 1440
2026-02-10 14:50:57,904 Average window size: 45  distance_to_goal: 8.764  distance_to_goal_reward: 0.000  reward: -0.010  spl: 0.000  success: 0.000
2026-02-10 14:50:57,904 	Perf Stats: trainer.rollout_collect: 0.215 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.022
2026-02-10 14:50:58,118 update: 46	fps: 124.455	
2026-02-10 14:50:58,118 Num updates: 46	Num frames 1472
2026-02-10 14:50:58,118 Average window size: 46  distance_to_goal: 8.768  distance_to_goal_reward: 0.000  reward: -0.012  spl: 0.000  success: 0.000
2026-02-10 14:50:58,118 	Perf Stats: trainer.rollout_collect: 0.215 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.022
2026-02-10 14:50:58,377 update: 47	fps: 124.432	
2026-02-10 14:50:58,377 Num updates: 47	Num frames 1504
2026-02-10 14:50:58,377 Average window size: 47  distance_to_goal: 8.788  distance_to_goal_reward: 0.000  reward: -0.013  spl: 0.000  success: 0.000
2026-02-10 14:50:58,377 	Perf Stats: trainer.rollout_collect: 0.214 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.022
2026-02-10 14:50:58,593 update: 48	fps: 124.846	
2026-02-10 14:50:58,594 Num updates: 48	Num frames 1536
2026-02-10 14:50:58,594 Average window size: 48  distance_to_goal: 8.841  distance_to_goal_reward: 0.000  reward: -0.016  spl: 0.000  success: 0.000
2026-02-10 14:50:58,594 	Perf Stats: trainer.rollout_collect: 0.214 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.022
2026-02-10 14:50:58,828 update: 49	fps: 125.057	
2026-02-10 14:50:58,829 Num updates: 49	Num frames 1568
2026-02-10 14:50:58,829 Average window size: 49  distance_to_goal: 8.826  distance_to_goal_reward: 0.000  reward: -0.017  spl: 0.000  success: 0.000
2026-02-10 14:50:58,829 	Perf Stats: trainer.rollout_collect: 0.214 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.022
2026-02-10 14:50:59,088 update: 50	fps: 125.018	
2026-02-10 14:50:59,088 Num updates: 50	Num frames 1600
2026-02-10 14:50:59,089 Average window size: 50  distance_to_goal: 8.839  distance_to_goal_reward: 0.000  reward: -0.017  spl: 0.000  success: 0.000
2026-02-10 14:50:59,089 	Perf Stats: trainer.rollout_collect: 0.213 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.022
2026-02-10 14:50:59,307 update: 51	fps: 125.376	
2026-02-10 14:50:59,307 Num updates: 51	Num frames 1632
2026-02-10 14:50:59,307 Average window size: 50  distance_to_goal: 8.825  distance_to_goal_reward: 0.000  reward: -0.016  spl: 0.000  success: 0.000
2026-02-10 14:50:59,307 	Perf Stats: trainer.rollout_collect: 0.213 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.022
2026-02-10 14:50:59,536 update: 52	fps: 125.623	
2026-02-10 14:50:59,536 Num updates: 52	Num frames 1664
2026-02-10 14:50:59,536 Average window size: 50  distance_to_goal: 8.855  distance_to_goal_reward: 0.000  reward: -0.015  spl: 0.000  success: 0.000
2026-02-10 14:50:59,536 	Perf Stats: trainer.rollout_collect: 0.213 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.022
2026-02-10 14:50:59,797 update: 53	fps: 125.567	
2026-02-10 14:50:59,797 Num updates: 53	Num frames 1696
2026-02-10 14:50:59,797 Average window size: 50  distance_to_goal: 8.887  distance_to_goal_reward: 0.000  reward: -0.018  spl: 0.000  success: 0.000
2026-02-10 14:50:59,797 	Perf Stats: trainer.rollout_collect: 0.213 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.022
2026-02-10 14:51:00,047 update: 54	fps: 125.613	
2026-02-10 14:51:00,047 Num updates: 54	Num frames 1728
2026-02-10 14:51:00,047 Average window size: 50  distance_to_goal: 8.887  distance_to_goal_reward: 0.000  reward: -0.018  spl: 0.000  success: 0.000
2026-02-10 14:51:00,047 	Perf Stats: trainer.rollout_collect: 0.213 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.022
2026-02-10 14:51:00,257 update: 55	fps: 126.014	
2026-02-10 14:51:00,257 Num updates: 55	Num frames 1760
2026-02-10 14:51:00,257 Average window size: 50  distance_to_goal: 8.841  distance_to_goal_reward: 0.000  reward: -0.014  spl: 0.000  success: 0.000
2026-02-10 14:51:00,257 	Perf Stats: trainer.rollout_collect: 0.212 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.022
2026-02-10 14:51:00,555 update: 56	fps: 125.624	
2026-02-10 14:51:00,555 Num updates: 56	Num frames 1792
2026-02-10 14:51:00,555 Average window size: 50  distance_to_goal: 8.887  distance_to_goal_reward: 0.000  reward: -0.011  spl: 0.000  success: 0.000
2026-02-10 14:51:00,555 	Perf Stats: trainer.rollout_collect: 0.213 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.022
2026-02-10 14:51:00,793 update: 57	fps: 125.772	
2026-02-10 14:51:00,793 Num updates: 57	Num frames 1824
2026-02-10 14:51:00,793 Average window size: 50  distance_to_goal: 8.898  distance_to_goal_reward: 0.000  reward: -0.008  spl: 0.000  success: 0.000
2026-02-10 14:51:00,793 	Perf Stats: trainer.rollout_collect: 0.213 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.022
2026-02-10 14:51:01,017 update: 58	fps: 126.025	
2026-02-10 14:51:01,017 Num updates: 58	Num frames 1856
2026-02-10 14:51:01,017 Average window size: 50  distance_to_goal: 8.919  distance_to_goal_reward: 0.000  reward: -0.006  spl: 0.000  success: 0.000
2026-02-10 14:51:01,017 	Perf Stats: trainer.rollout_collect: 0.213 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.022
2026-02-10 14:51:01,286 update: 59	fps: 125.897	
2026-02-10 14:51:01,286 Num updates: 59	Num frames 1888
2026-02-10 14:51:01,287 Average window size: 50  distance_to_goal: 8.944  distance_to_goal_reward: 0.000  reward: -0.009  spl: 0.000  success: 0.000
2026-02-10 14:51:01,287 	Perf Stats: trainer.rollout_collect: 0.212 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.022
2026-02-10 14:51:01,525 update: 60	fps: 126.031	
2026-02-10 14:51:01,525 Num updates: 60	Num frames 1920
2026-02-10 14:51:01,525 Average window size: 50  distance_to_goal: 8.956  distance_to_goal_reward: 0.000  reward: -0.009  spl: 0.000  success: 0.000
2026-02-10 14:51:01,525 	Perf Stats: trainer.rollout_collect: 0.213 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:01,723 update: 61	fps: 126.484	
2026-02-10 14:51:01,723 Num updates: 61	Num frames 1952
2026-02-10 14:51:01,723 Average window size: 50  distance_to_goal: 8.966  distance_to_goal_reward: 0.000  reward: -0.005  spl: 0.000  success: 0.000
2026-02-10 14:51:01,723 	Perf Stats: trainer.rollout_collect: 0.212 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:01,990 update: 62	fps: 126.374	
2026-02-10 14:51:01,990 Num updates: 62	Num frames 1984
2026-02-10 14:51:01,990 Average window size: 50  distance_to_goal: 8.953  distance_to_goal_reward: 0.000  reward: -0.007  spl: 0.000  success: 0.000
2026-02-10 14:51:01,990 	Perf Stats: trainer.rollout_collect: 0.212 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:02,200 update: 63	fps: 126.710	
2026-02-10 14:51:02,201 Num updates: 63	Num frames 2016
2026-02-10 14:51:02,201 Average window size: 50  distance_to_goal: 8.910  distance_to_goal_reward: 0.000  reward: -0.009  spl: 0.000  success: 0.000
2026-02-10 14:51:02,201 	Perf Stats: trainer.rollout_collect: 0.211 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:02,434 update: 64	fps: 126.858	
2026-02-10 14:51:02,434 Num updates: 64	Num frames 2048
2026-02-10 14:51:02,434 Average window size: 50  distance_to_goal: 8.956  distance_to_goal_reward: 0.000  reward: -0.012  spl: 0.000  success: 0.000
2026-02-10 14:51:02,435 	Perf Stats: trainer.rollout_collect: 0.211 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:02,701 update: 65	fps: 126.745	
2026-02-10 14:51:02,701 Num updates: 65	Num frames 2080
2026-02-10 14:51:02,701 Average window size: 50  distance_to_goal: 8.933  distance_to_goal_reward: 0.000  reward: -0.014  spl: 0.000  success: 0.000
2026-02-10 14:51:02,701 	Perf Stats: trainer.rollout_collect: 0.211 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:02,920 update: 66	fps: 127.000	
2026-02-10 14:51:02,920 Num updates: 66	Num frames 2112
2026-02-10 14:51:02,920 Average window size: 50  distance_to_goal: 8.903  distance_to_goal_reward: 0.000  reward: -0.012  spl: 0.000  success: 0.000
2026-02-10 14:51:02,920 	Perf Stats: trainer.rollout_collect: 0.211 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:03,124 update: 67	fps: 127.368	
2026-02-10 14:51:03,124 Num updates: 67	Num frames 2144
2026-02-10 14:51:03,124 Average window size: 50  distance_to_goal: 8.887  distance_to_goal_reward: 0.000  reward: -0.018  spl: 0.000  success: 0.000
2026-02-10 14:51:03,124 	Perf Stats: trainer.rollout_collect: 0.211 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:03,391 update: 68	fps: 127.245	
2026-02-10 14:51:03,391 Num updates: 68	Num frames 2176
2026-02-10 14:51:03,391 Average window size: 50  distance_to_goal: 8.845  distance_to_goal_reward: 0.000  reward: -0.017  spl: 0.000  success: 0.000
2026-02-10 14:51:03,391 	Perf Stats: trainer.rollout_collect: 0.210 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:03,603 update: 69	fps: 127.536	
2026-02-10 14:51:03,603 Num updates: 69	Num frames 2208
2026-02-10 14:51:03,603 Average window size: 50  distance_to_goal: 8.860  distance_to_goal_reward: 0.000  reward: -0.017  spl: 0.000  success: 0.000
2026-02-10 14:51:03,603 	Perf Stats: trainer.rollout_collect: 0.210 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:03,806 update: 70	fps: 127.883	
2026-02-10 14:51:03,807 Num updates: 70	Num frames 2240
2026-02-10 14:51:03,807 Average window size: 50  distance_to_goal: 8.889  distance_to_goal_reward: 0.000  reward: -0.020  spl: 0.000  success: 0.000
2026-02-10 14:51:03,807 	Perf Stats: trainer.rollout_collect: 0.210 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:04,062 update: 71	fps: 127.843	
2026-02-10 14:51:04,062 Num updates: 71	Num frames 2272
2026-02-10 14:51:04,062 Average window size: 50  distance_to_goal: 8.860  distance_to_goal_reward: 0.000  reward: -0.022  spl: 0.000  success: 0.000
2026-02-10 14:51:04,062 	Perf Stats: trainer.rollout_collect: 0.209 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:04,276 update: 72	fps: 128.100	
2026-02-10 14:51:04,276 Num updates: 72	Num frames 2304
2026-02-10 14:51:04,276 Average window size: 50  distance_to_goal: 8.848  distance_to_goal_reward: 0.000  reward: -0.023  spl: 0.000  success: 0.000
2026-02-10 14:51:04,276 	Perf Stats: trainer.rollout_collect: 0.209 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:04,495 update: 73	fps: 128.315	
2026-02-10 14:51:04,495 Num updates: 73	Num frames 2336
2026-02-10 14:51:04,495 Average window size: 50  distance_to_goal: 8.874  distance_to_goal_reward: 0.000  reward: -0.018  spl: 0.000  success: 0.000
2026-02-10 14:51:04,495 	Perf Stats: trainer.rollout_collect: 0.209 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:04,750 update: 74	fps: 128.274	
2026-02-10 14:51:04,751 Num updates: 74	Num frames 2368
2026-02-10 14:51:04,751 Average window size: 50  distance_to_goal: 8.829  distance_to_goal_reward: 0.000  reward: -0.020  spl: 0.000  success: 0.000
2026-02-10 14:51:04,751 	Perf Stats: trainer.rollout_collect: 0.209 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:04,972 update: 75	fps: 128.471	
2026-02-10 14:51:04,972 Num updates: 75	Num frames 2400
2026-02-10 14:51:04,972 Average window size: 50  distance_to_goal: 8.795  distance_to_goal_reward: 0.000  reward: -0.020  spl: 0.000  success: 0.000
2026-02-10 14:51:04,972 	Perf Stats: trainer.rollout_collect: 0.209 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:05,197 update: 76	fps: 128.633	
2026-02-10 14:51:05,197 Num updates: 76	Num frames 2432
2026-02-10 14:51:05,197 Average window size: 50  distance_to_goal: 8.769  distance_to_goal_reward: 0.000  reward: -0.018  spl: 0.000  success: 0.000
2026-02-10 14:51:05,197 	Perf Stats: trainer.rollout_collect: 0.209 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:05,479 update: 77	fps: 128.409	
2026-02-10 14:51:05,479 Num updates: 77	Num frames 2464
2026-02-10 14:51:05,479 Average window size: 50  distance_to_goal: 8.746  distance_to_goal_reward: 0.000  reward: -0.019  spl: 0.000  success: 0.000
2026-02-10 14:51:05,479 	Perf Stats: trainer.rollout_collect: 0.209 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:05,690 update: 78	fps: 128.658	
2026-02-10 14:51:05,690 Num updates: 78	Num frames 2496
2026-02-10 14:51:05,691 Average window size: 50  distance_to_goal: 8.800  distance_to_goal_reward: 0.000  reward: -0.012  spl: 0.000  success: 0.000
2026-02-10 14:51:05,691 	Perf Stats: trainer.rollout_collect: 0.208 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:05,906 update: 79	fps: 128.876	
2026-02-10 14:51:05,906 Num updates: 79	Num frames 2528
2026-02-10 14:51:05,906 Average window size: 50  distance_to_goal: 8.861  distance_to_goal_reward: 0.000  reward: -0.014  spl: 0.000  success: 0.000
2026-02-10 14:51:05,906 	Perf Stats: trainer.rollout_collect: 0.208 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:06,151 update: 80	fps: 128.897	
2026-02-10 14:51:06,151 Num updates: 80	Num frames 2560
2026-02-10 14:51:06,151 Average window size: 50  distance_to_goal: 8.844  distance_to_goal_reward: 0.000  reward: -0.017  spl: 0.000  success: 0.000
2026-02-10 14:51:06,151 	Perf Stats: trainer.rollout_collect: 0.208 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:06,364 update: 81	fps: 129.123	
2026-02-10 14:51:06,364 Num updates: 81	Num frames 2592
2026-02-10 14:51:06,364 Average window size: 50  distance_to_goal: 8.890  distance_to_goal_reward: 0.000  reward: -0.020  spl: 0.000  success: 0.000
2026-02-10 14:51:06,364 	Perf Stats: trainer.rollout_collect: 0.208 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:06,578 update: 82	fps: 129.339	
2026-02-10 14:51:06,578 Num updates: 82	Num frames 2624
2026-02-10 14:51:06,578 Average window size: 50  distance_to_goal: 8.929  distance_to_goal_reward: 0.000  reward: -0.021  spl: 0.000  success: 0.000
2026-02-10 14:51:06,578 	Perf Stats: trainer.rollout_collect: 0.207 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:06,857 update: 83	fps: 129.142	
2026-02-10 14:51:06,857 Num updates: 83	Num frames 2656
2026-02-10 14:51:06,857 Average window size: 50  distance_to_goal: 8.931  distance_to_goal_reward: 0.000  reward: -0.020  spl: 0.000  success: 0.000
2026-02-10 14:51:06,857 	Perf Stats: trainer.rollout_collect: 0.208 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:07,116 update: 84	fps: 129.071	
2026-02-10 14:51:07,116 Num updates: 84	Num frames 2688
2026-02-10 14:51:07,116 Average window size: 50  distance_to_goal: 9.002  distance_to_goal_reward: 0.000  reward: -0.021  spl: 0.000  success: 0.000
2026-02-10 14:51:07,116 	Perf Stats: trainer.rollout_collect: 0.208 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:07,323 update: 85	fps: 129.318	
2026-02-10 14:51:07,324 Num updates: 85	Num frames 2720
2026-02-10 14:51:07,324 Average window size: 50  distance_to_goal: 8.970  distance_to_goal_reward: 0.000  reward: -0.021  spl: 0.000  success: 0.000
2026-02-10 14:51:07,324 	Perf Stats: trainer.rollout_collect: 0.208 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:07,593 update: 86	fps: 129.185	
2026-02-10 14:51:07,593 Num updates: 86	Num frames 2752
2026-02-10 14:51:07,593 Average window size: 50  distance_to_goal: 9.016  distance_to_goal_reward: 0.000  reward: -0.021  spl: 0.000  success: 0.000
2026-02-10 14:51:07,593 	Perf Stats: trainer.rollout_collect: 0.208 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:07,806 update: 87	fps: 129.393	
2026-02-10 14:51:07,806 Num updates: 87	Num frames 2784
2026-02-10 14:51:07,806 Average window size: 50  distance_to_goal: 9.024  distance_to_goal_reward: 0.000  reward: -0.020  spl: 0.000  success: 0.000
2026-02-10 14:51:07,806 	Perf Stats: trainer.rollout_collect: 0.207 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:08,016 update: 88	fps: 129.615	
2026-02-10 14:51:08,016 Num updates: 88	Num frames 2816
2026-02-10 14:51:08,016 Average window size: 50  distance_to_goal: 9.032  distance_to_goal_reward: 0.000  reward: -0.021  spl: 0.000  success: 0.000
2026-02-10 14:51:08,016 	Perf Stats: trainer.rollout_collect: 0.207 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:08,283 update: 89	fps: 129.493	
2026-02-10 14:51:08,283 Num updates: 89	Num frames 2848
2026-02-10 14:51:08,284 Average window size: 50  distance_to_goal: 9.038  distance_to_goal_reward: 0.000  reward: -0.020  spl: 0.000  success: 0.000
2026-02-10 14:51:08,284 	Perf Stats: trainer.rollout_collect: 0.207 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:08,493 update: 90	fps: 129.713	
2026-02-10 14:51:08,493 Num updates: 90	Num frames 2880
2026-02-10 14:51:08,493 Average window size: 50  distance_to_goal: 9.005  distance_to_goal_reward: 0.000  reward: -0.026  spl: 0.000  success: 0.000
2026-02-10 14:51:08,493 	Perf Stats: trainer.rollout_collect: 0.207 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:08,706 update: 91	fps: 129.907	
2026-02-10 14:51:08,706 Num updates: 91	Num frames 2912
2026-02-10 14:51:08,706 Average window size: 50  distance_to_goal: 8.978  distance_to_goal_reward: 0.000  reward: -0.026  spl: 0.000  success: 0.000
2026-02-10 14:51:08,706 	Perf Stats: trainer.rollout_collect: 0.207 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:08,992 update: 92	fps: 129.679	
2026-02-10 14:51:08,992 Num updates: 92	Num frames 2944
2026-02-10 14:51:08,992 Average window size: 50  distance_to_goal: 8.960  distance_to_goal_reward: 0.000  reward: -0.029  spl: 0.000  success: 0.000
2026-02-10 14:51:08,993 	Perf Stats: trainer.rollout_collect: 0.207 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:09,222 update: 93	fps: 129.775	
2026-02-10 14:51:09,222 Num updates: 93	Num frames 2976
2026-02-10 14:51:09,222 Average window size: 50  distance_to_goal: 9.013  distance_to_goal_reward: 0.000  reward: -0.028  spl: 0.000  success: 0.000
2026-02-10 14:51:09,222 	Perf Stats: trainer.rollout_collect: 0.207 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:09,483 update: 94	fps: 129.696	
2026-02-10 14:51:09,483 Num updates: 94	Num frames 3008
2026-02-10 14:51:09,483 Average window size: 50  distance_to_goal: 9.071  distance_to_goal_reward: 0.000  reward: -0.029  spl: 0.000  success: 0.000
2026-02-10 14:51:09,483 	Perf Stats: trainer.rollout_collect: 0.207 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:09,760 update: 95	fps: 129.527	
2026-02-10 14:51:09,760 Num updates: 95	Num frames 3040
2026-02-10 14:51:09,760 Average window size: 50  distance_to_goal: 9.055  distance_to_goal_reward: 0.000  reward: -0.029  spl: 0.000  success: 0.000
2026-02-10 14:51:09,761 	Perf Stats: trainer.rollout_collect: 0.207 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:09,983 update: 96	fps: 129.659	
2026-02-10 14:51:09,983 Num updates: 96	Num frames 3072
2026-02-10 14:51:09,983 Average window size: 50  distance_to_goal: 9.102  distance_to_goal_reward: 0.000  reward: -0.030  spl: 0.000  success: 0.000
2026-02-10 14:51:09,983 	Perf Stats: trainer.rollout_collect: 0.207 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:10,188 update: 97	fps: 129.885	
2026-02-10 14:51:10,188 Num updates: 97	Num frames 3104
2026-02-10 14:51:10,188 Average window size: 50  distance_to_goal: 9.040  distance_to_goal_reward: 0.000  reward: -0.026  spl: 0.000  success: 0.000
2026-02-10 14:51:10,188 	Perf Stats: trainer.rollout_collect: 0.207 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:10,499 update: 98	fps: 129.539	
2026-02-10 14:51:10,499 Num updates: 98	Num frames 3136
2026-02-10 14:51:10,499 Average window size: 50  distance_to_goal: 9.065  distance_to_goal_reward: 0.000  reward: -0.027  spl: 0.000  success: 0.000
2026-02-10 14:51:10,499 	Perf Stats: trainer.rollout_collect: 0.207 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:10,743 update: 99	fps: 129.556	
2026-02-10 14:51:10,743 Num updates: 99	Num frames 3168
2026-02-10 14:51:10,743 Average window size: 50  distance_to_goal: 9.009  distance_to_goal_reward: 0.000  reward: -0.028  spl: 0.000  success: 0.000
2026-02-10 14:51:10,743 	Perf Stats: trainer.rollout_collect: 0.207 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.021
2026-02-10 14:51:11,061 update: 100	fps: 129.182	
2026-02-10 14:51:11,061 Num updates: 100	Num frames 3200
2026-02-10 14:51:11,061 Average window size: 50  distance_to_goal: 8.999  distance_to_goal_reward: 0.000  reward: -0.028  spl: 0.000  success: 0.000
2026-02-10 14:51:11,062 	Perf Stats: trainer.rollout_collect: 0.207 trainer.sample_action: 0.002 trainer.obs_insert: 0.000 trainer.step_env: 0.004 trainer.update_stats: 0.000 trainer.update_agent: 0.020
(habitat) liuyi@liuyi:~/projects/habitat-lab$ # 评估并导出视频
python -u -m habitat_baselines.run \
  --config-name=pointnav/ppo_pointnav_example.yaml \
  habitat_baselines.trainer_name=ddppo \
  habitat_baselines.evaluate=True \
  habitat_baselines.load_resume_state_config=False \
  habitat_baselines.eval_ckpt_path_dir=data/new_checkpoints_ddppo_demo/latest.pth \
  habitat_baselines.video_dir=videos/ddppo_demo_eval
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 14:51:19,463 Loading resume state: data/new_checkpoints/.habitat-resume-stateeval.pth
/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ddppo/ddp_utils.py:224: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
  return torch.load(filename, map_location="cpu")
/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/ppo_trainer.py:341: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
  return torch.load(checkpoint_path, *args, **kwargs)
2026-02-10 14:51:19,489 Loaded checkpoint trained for 3200 steps
2026-02-10 14:51:19,507 env config: habitat:
  seed: 100
  env_task: GymHabitatEnv
  env_task_gym_dependencies: []
  env_task_gym_id: ''
  environment:
    max_episode_steps: 500
    max_episode_seconds: 10000000
    iterator_options:
      cycle: true
      shuffle: true
      group_by_scene: true
      num_episode_sample: -1
      max_scene_repeat_episodes: -1
      max_scene_repeat_steps: 10000
      step_repetition_range: 0.2
  simulator:
    type: Sim-v0
    forward_step_size: 0.25
    turn_angle: 10
    create_renderer: false
    requires_textures: true
    auto_sleep: false
    step_physics: true
    concur_render: false
    needs_markers: true
    update_articulated_agent: true
    scene: data/scene_datasets/habitat-test-scenes/van-gogh-room.glb
    scene_dataset: default
    additional_object_paths: []
    seed: ${habitat.seed}
    default_agent_id: 0
    debug_render: false
    debug_render_articulated_agent: false
    kinematic_mode: false
    should_setup_semantic_ids: true
    debug_render_goal: true
    robot_joint_start_noise: 0.0
    ctrl_freq: 120.0
    ac_freq_ratio: 4
    load_objs: true
    hold_thresh: 0.15
    grasp_impulse: 10000.0
    agents:
      main_agent:
        height: 1.5
        radius: 0.1
        max_climb: 0.2
        max_slope: 45.0
        grasp_managers: 1
        sim_sensors:
          rgb_sensor:
            type: HabitatSimRGBSensor
            height: 256
            width: 256
            position:
            - 0.0
            - 1.25
            - 0.0
            orientation:
            - 0.0
            - 0.0
            - 0.0
            hfov: 90
            sensor_subtype: PINHOLE
            noise_model: None
            noise_model_kwargs: {}
          depth_sensor:
            type: HabitatSimDepthSensor
            height: 256
            width: 256
            position:
            - 0.0
            - 1.25
            - 0.0
            orientation:
            - 0.0
            - 0.0
            - 0.0
            hfov: 90
            sensor_subtype: PINHOLE
            noise_model: None
            noise_model_kwargs: {}
            min_depth: 0.0
            max_depth: 10.0
            normalize_depth: true
        is_set_start_state: false
        start_position:
        - 0.0
        - 0.0
        - 0.0
        start_rotation:
        - 0.0
        - 0.0
        - 0.0
        - 1.0
        joint_start_noise: 0.1
        joint_that_can_control: null
        joint_start_override: null
        articulated_agent_urdf: null
        articulated_agent_type: null
        ik_arm_urdf: null
        motion_data_path: ''
        auto_update_sensor_transform: true
    agents_order:
    - main_agent
    default_agent_navmesh: true
    navmesh_include_static_objects: false
    habitat_sim_v0:
      gpu_device_id: 0
      gpu_gpu: false
      allow_sliding: true
      frustum_culling: true
      enable_physics: false
      enable_hbao: false
      physics_config_file: ./data/default.physics_config.json
      leave_context_with_background_renderer: false
      enable_gfx_replay_save: false
    ep_info: null
    object_ids_start: 100
    renderer:
      enable_batch_renderer: false
      composite_files: null
      classic_replay_renderer: false
  task:
    physics_target_sps: 60.0
    reward_measure: distance_to_goal_reward
    success_measure: spl
    success_reward: 2.5
    slack_reward: -0.01
    end_on_success: true
    type: Nav-v0
    lab_sensors:
      pointgoal_with_gps_compass_sensor:
        type: PointGoalWithGPSCompassSensor
        goal_format: POLAR
        dimensionality: 2
    measurements:
      distance_to_goal:
        type: DistanceToGoal
        distance_to: POINT
      success:
        type: Success
        success_distance: 0.2
      spl:
        type: SPL
      distance_to_goal_reward:
        type: DistanceToGoalReward
    rank0_env0_measure_names:
    - habitat_perf
    rank0_measure_names: []
    goal_sensor_uuid: pointgoal_with_gps_compass
    count_obj_collisions: true
    settle_steps: 5
    constraint_violation_ends_episode: true
    constraint_violation_drops_object: false
    force_regenerate: false
    should_save_to_cache: false
    object_in_hand_sample_prob: 0.167
    min_start_distance: 3.0
    render_target: true
    filter_colliding_states: true
    num_spawn_attempts: 200
    spawn_max_dist_to_obj: 2.0
    base_angle_noise: 0.523599
    spawn_max_dist_to_obj_delta: 0.02
    recep_place_shrink_factor: 0.8
    ee_sample_factor: 0.2
    ee_exclude_region: 0.0
    base_noise: 0.05
    spawn_region_scale: 0.2
    joint_max_impulse: -1.0
    desired_resting_position:
    - 0.5
    - 0.0
    - 1.0
    use_marker_t: true
    cache_robot_init: false
    success_state: 0.0
    should_enforce_target_within_reach: false
    task_spec_base_path: habitat/task/rearrange/pddl/
    task_spec: ''
    pddl_domain_def: replica_cad
    obj_succ_thresh: 0.3
    enable_safe_drop: false
    art_succ_thresh: 0.15
    robot_at_thresh: 2.0
    min_distance_start_agents: -1.0
    actions:
      stop:
        type: StopAction
      move_forward:
        type: MoveForwardAction
        tilt_angle: 15
      turn_left:
        type: TurnLeftAction
        tilt_angle: 15
      turn_right:
        type: TurnRightAction
        tilt_angle: 15
  dataset:
    type: PointNav-v1
    split: val
    scenes_dir: data/scene_datasets
    content_scenes:
    - '*'
    data_path: data/datasets/pointnav/habitat-test-scenes/v1/{split}/{split}.json.gz
    metadata: null
  gym:
    obs_keys: null
    action_keys: null
    achieved_goal_keys: []
    desired_goal_keys: []
habitat_baselines:
  evaluate: true
  trainer_name: ddppo
  updater_name: PPO
  distrib_updater_name: DDPPO
  torch_gpu_id: 0
  tensorboard_dir: tb
  writer_type: tb
  video_dir: videos/ddppo_demo_eval
  video_fps: 10
  test_episode_count: 2
  eval_ckpt_path_dir: data/new_checkpoints_ddppo_demo/latest.pth
  num_environments: 1
  num_processes: -1
  rollout_storage_name: RolloutStorage
  checkpoint_folder: data/new_checkpoints
  num_updates: -1
  num_checkpoints: 50
  checkpoint_interval: -1
  total_num_steps: 1000000.0
  log_interval: 10
  log_file: train.log
  force_blind_policy: false
  verbose: true
  vector_env_factory:
    _target_: habitat_baselines.common.HabitatVectorEnvFactory
  evaluator:
    _target_: habitat_baselines.rl.ppo.habitat_evaluator.HabitatEvaluator
  eval_keys_to_include_in_name: []
  force_torch_single_threaded: true
  wb:
    project_name: ''
    entity: ''
    group: ''
    run_name: ''
  load_resume_state_config: false
  eval:
    split: val
    use_ckpt_config: true
    should_load_ckpt: true
    evals_per_ep: 1
    video_option:
    - disk
    - tensorboard
    extra_sim_sensors: {}
  profiling:
    capture_start_step: -1
    num_steps_to_capture: -1
  should_log_single_proc_infos: false
  on_save_ckpt_callback: null
  rl:
    agent:
      type: SingleAgentAccessMgr
      num_agent_types: 1
      num_active_agents_per_type:
      - 1
      num_pool_agents_per_type:
      - 1
      agent_sample_interval: 20
      force_partner_sample_idx: -1
      behavior_latent_dim: -1
      force_all_agents: false
      discrim_reward_weight: 1.0
      allow_self_play: false
      self_play_batched: false
      load_type1_pop_ckpts: null
    preemption:
      append_slurm_job_id: false
      save_resume_state_interval: 100
      save_state_batch_only: false
    policy:
      main_agent:
        name: PointNavResNetPolicy
        action_distribution_type: categorical
        action_dist:
          use_log_std: true
          use_softplus: false
          std_init: ???
          log_std_init: 0.0
          use_std_param: false
          clamp_std: true
          min_std: 1.0e-06
          max_std: 1
          min_log_std: -5
          max_log_std: 2
          action_activation: tanh
          scheduled_std: false
        obs_transforms: {}
        hierarchical_policy: ???
    ppo:
      clip_param: 0.1
      ppo_epoch: 1
      num_mini_batch: 1
      value_loss_coef: 0.5
      entropy_coef: 0.01
      lr: 0.00025
      eps: 1.0e-05
      max_grad_norm: 0.5
      num_steps: 32
      use_gae: true
      use_linear_lr_decay: true
      use_linear_clip_decay: true
      gamma: 0.99
      tau: 0.95
      reward_window_size: 50
      use_normalized_advantage: false
      hidden_size: 512
      entropy_target_factor: 0.0
      use_adaptive_entropy_pen: false
      use_clipped_value_loss: true
      use_double_buffered_sampler: false
    ddppo:
      sync_frac: 0.6
      distrib_backend: GLOO
      rnn_type: GRU
      num_recurrent_layers: 1
      backbone: resnet18
      pretrained_weights: data/ddppo-models/gibson-2plus-resnet50.pth
      pretrained: false
      pretrained_encoder: false
      train_encoder: true
      reset_critic: true
      force_distributed: false
    ver:
      variable_experience: true
      num_inference_workers: 2
      overlap_rollouts_and_learn: false
    auxiliary_losses: {}

2026-02-10 14:51:19,507 Initializing dataset PointNav-v1
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 14:51:21,822 Initializing dataset PointNav-v1
2026-02-10 14:51:21,824 initializing sim Sim-v0
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
Renderer: NVIDIA GeForce RTX 4060 Laptop GPU/PCIe/SSE2 by NVIDIA Corporation
OpenGL version: 4.6.0 NVIDIA 580.95.05
Using optional features:
    GL_ARB_vertex_array_object
    GL_ARB_separate_shader_objects
    GL_ARB_robustness
    GL_ARB_texture_storage
    GL_ARB_texture_view
    GL_ARB_framebuffer_no_attachments
    GL_ARB_invalidate_subdata
    GL_ARB_texture_storage_multisample
    GL_ARB_multi_bind
    GL_ARB_direct_state_access
    GL_ARB_get_texture_sub_image
    GL_ARB_texture_filter_anisotropic
    GL_KHR_debug
    GL_KHR_parallel_shader_compile
    GL_NV_depth_buffer_float
Using driver workarounds:
    no-forward-compatible-core-context
    nv-egl-incorrect-gl11-function-pointers
    no-layout-qualifiers-on-old-glsl
    nv-zero-context-profile-mask
    nv-implementation-color-read-format-dsa-broken
    nv-cubemap-inconsistent-compressed-image-size
    nv-cubemap-broken-full-compressed-image-query
    nv-compressed-block-size-in-bits
[14:51:21:918682]:[Warning]:[Metadata] SceneDatasetAttributes.cpp(107)::addNewSceneInstanceToDataset : Dataset : 'default' : Lighting Layout Attributes 'no_lights' specified in Scene Attributes but does not exist in dataset, so creating default.
[14:51:21:921010]:[Warning]:[Scene] SemanticScene.h(331)::checkFileExists : ::loadSemanticSceneDescriptor: File `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` does not exist.  Aborting load.
[14:51:21:921024]:[Warning]:[Scene] SemanticScene.cpp(123)::loadSemanticSceneDescriptor : SSD File Naming Issue! Neither SemanticAttributes-provided name : `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` nor constructed filename : `data/scene_datasets/habitat-test-scenes/info_semantic.json` exist on disk.
[14:51:21:921030]:[Error]:[Scene] SemanticScene.cpp(139)::loadSemanticSceneDescriptor : SSD Load Failure! File with SemanticAttributes-provided name `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` exists but failed to load.
[14:51:22:474157]:[Warning]:[Sim] Simulator.cpp(595)::instanceStageForSceneAttributes : The active scene does not contain semantic annotations : activeSemanticSceneID_ = 0
2026-02-10 14:51:22,475 Initializing task Nav-v0
2026-02-10 14:51:22,888 Number of params to train: 5821797
2026-02-10 14:51:22,888 Agent number of parameters: 5821797
 50%|██████████████████████▌                      | 1/2 [00:00<00:00,  2.50it/s]2026-02-10 14:51:23,308 Video created: videos/ddppo_demo_eval/episode=7_1-ckpt=0-distance_to_goal=2.13-success=0.00-spl=0.00-distance_to_goal_reward=-0.00.mp4
100%|███████████████████████████████████████████| 13/13 [00:00<00:00, 55.88it/s]
moviepy is installed, but can't import moviepy.editor. Some packages could be missing [imageio, requests]
100%|█████████████████████████████████████████████| 2/2 [00:00<00:00,  2.43it/s]2026-02-10 14:51:23,724 Video created: videos/ddppo_demo_eval/episode=26_1-ckpt=0-distance_to_goal=2.06-success=0.00-spl=0.00-distance_to_goal_reward=-0.00.mp4
100%|████████████████████████████████████████████| 4/4 [00:00<00:00, 119.71it/s]
moviepy is installed, but can't import moviepy.editor. Some packages could be missing [imageio, requests]
100%|█████████████████████████████████████████████| 2/2 [00:00<00:00,  2.25it/s]
2026-02-10 14:51:23,796 Average episode reward: 0.0396
2026-02-10 14:51:23,796 Average episode spl: 0.0000
2026-02-10 14:51:23,796 Average episode success: 0.0000
2026-02-10 14:51:23,796 Average episode distance_to_goal: 2.0958
2026-02-10 14:51:23,796 Average episode distance_to_goal_reward: 0.0000
(habitat) liuyi@liuyi:~/projects/habitat-lab$ cd ~/projects/habitat-lab
mkdir -p data/ddppo-models
wget -c \
  https://dl.fbaipublicfiles.com/habitat/data/baselines/v1/ddppo/ddppo-models/gibson-2plus-resnet50.pth \
  -O data/ddppo-models/gibson-2plus-resnet50.pth
--2026-02-10 16:43:13--  https://dl.fbaipublicfiles.com/habitat/data/baselines/v1/ddppo/ddppo-models/gibson-2plus-resnet50.pth
Resolving dl.fbaipublicfiles.com (dl.fbaipublicfiles.com)... 65.8.76.47, 65.8.76.89, 65.8.76.77, ...
Connecting to dl.fbaipublicfiles.com (dl.fbaipublicfiles.com)|65.8.76.47|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 49853716 (48M) [application/octet-stream]
Saving to: ‘data/ddppo-models/gibson-2plus-resnet50.pth’

data/ddppo-models/ 100%[================>]  47.54M  11.7MB/s    in 4.0s    

2026-02-10 16:43:17 (11.8 MB/s) - ‘data/ddppo-models/gibson-2plus-resnet50.pth’ saved [49853716/49853716]

(habitat) liuyi@liuyi:~/projects/habitat-lab$ python -u -m habitat_baselines.run \
  --config-name=pointnav/ddppo_pointnav.yaml \
  benchmark/nav/pointnav=pointnav_habitat_test \
  habitat_baselines.evaluate=True \
  habitat_baselines.eval.should_load_ckpt=False \
  habitat_baselines.rl.ddppo.pretrained=True \
  habitat_baselines.rl.ddppo.pretrained_weights=data/ddppo-models/gibson-2plus-resnet50.pth \
  habitat_baselines.load_resume_state_config=False \
  habitat_baselines.num_environments=1 \
  habitat_baselines.test_episode_count=10 \
  habitat_baselines.video_dir=videos/ddppo_pretrained_eval \
  habitat_baselines.tensorboard_dir=tb/ddppo_pretrained_eval
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 16:43:26,566 Loading resume state: data/new_checkpoints/.habitat-resume-stateeval.pth
/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ddppo/ddp_utils.py:224: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
  return torch.load(filename, map_location="cpu")
2026-02-10 16:43:26,584 Initializing dataset PointNav-v1
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 16:43:28,912 Initializing dataset PointNav-v1
2026-02-10 16:43:28,914 initializing sim Sim-v0
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
Renderer: NVIDIA GeForce RTX 4060 Laptop GPU/PCIe/SSE2 by NVIDIA Corporation
OpenGL version: 4.6.0 NVIDIA 580.95.05
Using optional features:
    GL_ARB_vertex_array_object
    GL_ARB_separate_shader_objects
    GL_ARB_robustness
    GL_ARB_texture_storage
    GL_ARB_texture_view
    GL_ARB_framebuffer_no_attachments
    GL_ARB_invalidate_subdata
    GL_ARB_texture_storage_multisample
    GL_ARB_multi_bind
    GL_ARB_direct_state_access
    GL_ARB_get_texture_sub_image
    GL_ARB_texture_filter_anisotropic
    GL_KHR_debug
    GL_KHR_parallel_shader_compile
    GL_NV_depth_buffer_float
Using driver workarounds:
    no-forward-compatible-core-context
    nv-egl-incorrect-gl11-function-pointers
    no-layout-qualifiers-on-old-glsl
    nv-zero-context-profile-mask
    nv-implementation-color-read-format-dsa-broken
    nv-cubemap-inconsistent-compressed-image-size
    nv-cubemap-broken-full-compressed-image-query
    nv-compressed-block-size-in-bits
[16:43:28:985321]:[Warning]:[Metadata] SceneDatasetAttributes.cpp(107)::addNewSceneInstanceToDataset : Dataset : 'default' : Lighting Layout Attributes 'no_lights' specified in Scene Attributes but does not exist in dataset, so creating default.
[16:43:28:985390]:[Warning]:[Scene] SemanticScene.h(331)::checkFileExists : ::loadSemanticSceneDescriptor: File `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` does not exist.  Aborting load.
[16:43:28:985399]:[Warning]:[Scene] SemanticScene.cpp(123)::loadSemanticSceneDescriptor : SSD File Naming Issue! Neither SemanticAttributes-provided name : `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` nor constructed filename : `data/scene_datasets/habitat-test-scenes/info_semantic.json` exist on disk.
[16:43:28:985406]:[Error]:[Scene] SemanticScene.cpp(139)::loadSemanticSceneDescriptor : SSD Load Failure! File with SemanticAttributes-provided name `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` exists but failed to load.
[16:43:29:525855]:[Warning]:[Sim] Simulator.cpp(595)::instanceStageForSceneAttributes : The active scene does not contain semantic annotations : activeSemanticSceneID_ = 0
2026-02-10 16:43:29,527 Initializing task Nav-v0
/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/single_agent_access_mgr.py:205: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
  pretrained_state = torch.load(
Error executing job with overrides: ['benchmark/nav/pointnav=pointnav_habitat_test', 'habitat_baselines.evaluate=True', 'habitat_baselines.eval.should_load_ckpt=False', 'habitat_baselines.rl.ddppo.pretrained=True', 'habitat_baselines.rl.ddppo.pretrained_weights=data/ddppo-models/gibson-2plus-resnet50.pth', 'habitat_baselines.load_resume_state_config=False', 'habitat_baselines.num_environments=1', 'habitat_baselines.test_episode_count=10', 'habitat_baselines.video_dir=videos/ddppo_pretrained_eval', 'habitat_baselines.tensorboard_dir=tb/ddppo_pretrained_eval']
Traceback (most recent call last):
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/run.py", line 31, in main
    execute_exp(cfg, "eval" if cfg.habitat_baselines.evaluate else "train")
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/run.py", line 62, in execute_exp
    trainer.eval()
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/common/base_trainer.py", line 129, in eval
    self._eval_checkpoint(
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/ppo_trainer.py", line 876, in _eval_checkpoint
    self._agent = self._create_agent(None)
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/ppo_trainer.py", line 123, in _create_agent
    return baseline_registry.get_agent_access_mgr(
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/single_agent_access_mgr.py", line 83, in __init__
    self._init_policy_and_updater(lr_schedule_fn, resume_state)
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/single_agent_access_mgr.py", line 86, in _init_policy_and_updater
    self._actor_critic = self._create_policy()
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/single_agent_access_mgr.py", line 211, in _create_policy
    actor_critic.load_state_dict(
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/torch/nn/modules/module.py", line 2624, in load_state_dict
    raise RuntimeError(
RuntimeError: Error(s) in loading state_dict for PointNavResNetPolicy:
	Missing key(s) in state_dict: "net.visual_encoder.running_mean_and_var._mean", "net.visual_encoder.running_mean_and_var._var", "net.visual_encoder.running_mean_and_var._count". 
	size mismatch for net.visual_encoder.backbone.conv1.0.weight: copying a param with shape torch.Size([32, 1, 7, 7]) from checkpoint, the shape in current model is torch.Size([32, 4, 7, 7]).

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
Exception ignored in: <function VectorEnv.__del__ at 0x7440541dc280>
Traceback (most recent call last):
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/core/vector_env.py", line 613, in __del__
    self.close()
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/core/vector_env.py", line 470, in close
    write_fn((CLOSE_COMMAND, None))
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/core/vector_env.py", line 131, in __call__
    self.write_fn(data)
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/utils/pickle5_multiprocessing.py", line 63, in send
    self.send_bytes(buf.getvalue())
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/multiprocessing/connection.py", line 200, in send_bytes
    self._send_bytes(m[offset:offset + size])
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/multiprocessing/connection.py", line 411, in _send_bytes
    self._send(header + buf)
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/multiprocessing/connection.py", line 368, in _send
    n = write(self._handle, buf)
BrokenPipeError: [Errno 32] Broken pipe
(habitat) liuyi@liuyi:~/projects/habitat-lab$ python -u -m habitat_baselines.run \
  --config-name=pointnav/ddppo_pointnav.yaml \
  benchmark/nav/pointnav=pointnav_habitat_test \
  habitat_baselines.evaluate=True \
  habitat_baselines.eval.should_load_ckpt=False \
  habitat_baselines.rl.ddppo.pretrained=True \
  habitat_baselines.rl.ddppo.pretrained_weights=data/ddppo-models/gibson-2plus-resnet50.pth \
  'habitat.gym.obs_keys=[depth,pointgoal_with_gps_compass]' \
  habitat_baselines.load_resume_state_config=False \
  habitat_baselines.checkpoint_folder=data/new_checkpoints_pretrained_eval_tmp \
  habitat_baselines.num_environments=1 \
  habitat_baselines.test_episode_count=10 \
  habitat_baselines.video_dir=videos/ddppo_pretrained_eval \
  habitat_baselines.tensorboard_dir=tb/ddppo_pretrained_eval
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 16:47:57,082 Initializing dataset PointNav-v1
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 16:47:59,327 Initializing dataset PointNav-v1
2026-02-10 16:47:59,329 initializing sim Sim-v0
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
Renderer: NVIDIA GeForce RTX 4060 Laptop GPU/PCIe/SSE2 by NVIDIA Corporation
OpenGL version: 4.6.0 NVIDIA 580.95.05
Using optional features:
    GL_ARB_vertex_array_object
    GL_ARB_separate_shader_objects
    GL_ARB_robustness
    GL_ARB_texture_storage
    GL_ARB_texture_view
    GL_ARB_framebuffer_no_attachments
    GL_ARB_invalidate_subdata
    GL_ARB_texture_storage_multisample
    GL_ARB_multi_bind
    GL_ARB_direct_state_access
    GL_ARB_get_texture_sub_image
    GL_ARB_texture_filter_anisotropic
    GL_KHR_debug
    GL_KHR_parallel_shader_compile
    GL_NV_depth_buffer_float
Using driver workarounds:
    no-forward-compatible-core-context
    nv-egl-incorrect-gl11-function-pointers
    no-layout-qualifiers-on-old-glsl
    nv-zero-context-profile-mask
    nv-implementation-color-read-format-dsa-broken
    nv-cubemap-inconsistent-compressed-image-size
    nv-cubemap-broken-full-compressed-image-query
    nv-compressed-block-size-in-bits
[16:47:59:400903]:[Warning]:[Metadata] SceneDatasetAttributes.cpp(107)::addNewSceneInstanceToDataset : Dataset : 'default' : Lighting Layout Attributes 'no_lights' specified in Scene Attributes but does not exist in dataset, so creating default.
[16:47:59:400979]:[Warning]:[Scene] SemanticScene.h(331)::checkFileExists : ::loadSemanticSceneDescriptor: File `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` does not exist.  Aborting load.
[16:47:59:400991]:[Warning]:[Scene] SemanticScene.cpp(123)::loadSemanticSceneDescriptor : SSD File Naming Issue! Neither SemanticAttributes-provided name : `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` nor constructed filename : `data/scene_datasets/habitat-test-scenes/info_semantic.json` exist on disk.
[16:47:59:400999]:[Error]:[Scene] SemanticScene.cpp(139)::loadSemanticSceneDescriptor : SSD Load Failure! File with SemanticAttributes-provided name `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` exists but failed to load.
[16:47:59:934582]:[Warning]:[Sim] Simulator.cpp(595)::instanceStageForSceneAttributes : The active scene does not contain semantic annotations : activeSemanticSceneID_ = 0
2026-02-10 16:47:59,935 Initializing task Nav-v0
/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/single_agent_access_mgr.py:205: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
  pretrained_state = torch.load(
2026-02-10 16:48:00,601 Number of params to train: 12454917
2026-02-10 16:48:00,602 Agent number of parameters: 12454917
100%|███████████████████████████████████████| 10/10 [00:01<00:00,  7.38it/s]
2026-02-10 16:48:01,966 Average episode spl: 0.9703
2026-02-10 16:48:01,966 Average episode reward: 4.1383
2026-02-10 16:48:01,966 Average episode distance_to_goal_reward: 0.0000
2026-02-10 16:48:01,966 Average episode success: 1.0000
2026-02-10 16:48:01,966 Average episode distance_to_goal: 0.0625
(habitat) liuyi@liuyi:~/projects/habitat-lab$ ls -lh videos/ddppo_pretrained_eval
ls: cannot access 'videos/ddppo_pretrained_eval': No such file or directory
(habitat) liuyi@liuyi:~/projects/habitat-lab$ python -u -m habitat_baselines.run \
  --config-name=pointnav/ddppo_pointnav.yaml \
  benchmark/nav/pointnav=pointnav_habitat_test \
  habitat_baselines.evaluate=True \
  habitat_baselines.eval.should_load_ckpt=False \
  habitat_baselines.eval.video_option=[disk] \
  habitat_baselines.rl.ddppo.pretrained=True \
  habitat_baselines.rl.ddppo.pretrained_weights=data/ddppo-models/gibson-2plus-resnet50.pth \
  'habitat.gym.obs_keys=[depth,pointgoal_with_gps_compass]' \
  habitat_baselines.load_resume_state_config=False \
  habitat_baselines.checkpoint_folder=data/new_checkpoints_pretrained_eval_tmp \
  habitat_baselines.num_environments=1 \
  habitat_baselines.test_episode_count=10 \
  habitat_baselines.video_dir=videos/ddppo_pretrained_eval \
  habitat_baselines.tensorboard_dir=tb/ddppo_pretrained_eval
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 16:51:16,474 Initializing dataset PointNav-v1
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 16:51:18,687 Initializing dataset PointNav-v1
2026-02-10 16:51:18,689 initializing sim Sim-v0
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
Renderer: NVIDIA GeForce RTX 4060 Laptop GPU/PCIe/SSE2 by NVIDIA Corporation
OpenGL version: 4.6.0 NVIDIA 580.95.05
Using optional features:
    GL_ARB_vertex_array_object
    GL_ARB_separate_shader_objects
    GL_ARB_robustness
    GL_ARB_texture_storage
    GL_ARB_texture_view
    GL_ARB_framebuffer_no_attachments
    GL_ARB_invalidate_subdata
    GL_ARB_texture_storage_multisample
    GL_ARB_multi_bind
    GL_ARB_direct_state_access
    GL_ARB_get_texture_sub_image
    GL_ARB_texture_filter_anisotropic
    GL_KHR_debug
    GL_KHR_parallel_shader_compile
    GL_NV_depth_buffer_float
Using driver workarounds:
    no-forward-compatible-core-context
    nv-egl-incorrect-gl11-function-pointers
    no-layout-qualifiers-on-old-glsl
    nv-zero-context-profile-mask
    nv-implementation-color-read-format-dsa-broken
    nv-cubemap-inconsistent-compressed-image-size
    nv-cubemap-broken-full-compressed-image-query
    nv-compressed-block-size-in-bits
[16:51:18:762540]:[Warning]:[Metadata] SceneDatasetAttributes.cpp(107)::addNewSceneInstanceToDataset : Dataset : 'default' : Lighting Layout Attributes 'no_lights' specified in Scene Attributes but does not exist in dataset, so creating default.
[16:51:18:762612]:[Warning]:[Scene] SemanticScene.h(331)::checkFileExists : ::loadSemanticSceneDescriptor: File `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` does not exist.  Aborting load.
[16:51:18:762622]:[Warning]:[Scene] SemanticScene.cpp(123)::loadSemanticSceneDescriptor : SSD File Naming Issue! Neither SemanticAttributes-provided name : `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` nor constructed filename : `data/scene_datasets/habitat-test-scenes/info_semantic.json` exist on disk.
[16:51:18:762629]:[Error]:[Scene] SemanticScene.cpp(139)::loadSemanticSceneDescriptor : SSD Load Failure! File with SemanticAttributes-provided name `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` exists but failed to load.
[16:51:19:299821]:[Warning]:[Sim] Simulator.cpp(595)::instanceStageForSceneAttributes : The active scene does not contain semantic annotations : activeSemanticSceneID_ = 0
2026-02-10 16:51:19,301 Initializing task Nav-v0
/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/single_agent_access_mgr.py:205: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
  pretrained_state = torch.load(
2026-02-10 16:51:19,958 Number of params to train: 12454917
2026-02-10 16:51:19,959 Agent number of parameters: 12454917
 10%|████                                    | 1/10 [00:00<00:03,  2.34it/s]2026-02-10 16:51:20,398 Video created: videos/ddppo_pretrained_eval/episode=7_1-ckpt=0-distance_to_goal=0.05-success=1.00-spl=1.00-distance_to_goal_reward=-0.00.mp4
100%|██████████████████████████████████████| 21/21 [00:00<00:00, 131.08it/s]
 20%|████████                                | 2/10 [00:00<00:03,  2.45it/s]2026-02-10 16:51:20,791 Video created: videos/ddppo_pretrained_eval/episode=26_1-ckpt=0-distance_to_goal=0.02-success=1.00-spl=0.95-distance_to_goal_reward=-0.00.mp4
100%|██████████████████████████████████████| 27/27 [00:00<00:00, 864.82it/s]
 30%|████████████                            | 3/10 [00:01<00:02,  3.26it/s]2026-02-10 16:51:20,977 Video created: videos/ddppo_pretrained_eval/episode=33_1-ckpt=0-distance_to_goal=0.13-success=1.00-spl=1.00-distance_to_goal_reward=-0.00.mp4
100%|██████████████████████████████████████| 16/16 [00:00<00:00, 613.71it/s]
 40%|████████████████                        | 4/10 [00:01<00:01,  3.66it/s]2026-02-10 16:51:21,199 Video created: videos/ddppo_pretrained_eval/episode=39_1-ckpt=0-distance_to_goal=0.06-success=1.00-spl=0.91-distance_to_goal_reward=-0.00.mp4
100%|██████████████████████████████████████| 22/22 [00:00<00:00, 643.59it/s]
 50%|████████████████████                    | 5/10 [00:01<00:01,  3.89it/s]2026-02-10 16:51:21,428 Video created: videos/ddppo_pretrained_eval/episode=12_1-ckpt=0-distance_to_goal=0.02-success=1.00-spl=0.96-distance_to_goal_reward=-0.00.mp4
100%|██████████████████████████████████████| 26/26 [00:00<00:00, 688.83it/s]
 60%|████████████████████████                | 6/10 [00:01<00:01,  3.81it/s]2026-02-10 16:51:21,701 Video created: videos/ddppo_pretrained_eval/episode=35_1-ckpt=0-distance_to_goal=0.04-success=1.00-spl=0.94-distance_to_goal_reward=-0.00.mp4
100%|██████████████████████████████████████| 29/29 [00:00<00:00, 873.26it/s]
 70%|████████████████████████████            | 7/10 [00:01<00:00,  4.06it/s]2026-02-10 16:51:21,913 Video created: videos/ddppo_pretrained_eval/episode=3_1-ckpt=0-distance_to_goal=0.05-success=1.00-spl=1.00-distance_to_goal_reward=-0.00.mp4
100%|██████████████████████████████████████| 19/19 [00:00<00:00, 530.29it/s]
 80%|████████████████████████████████        | 8/10 [00:02<00:00,  4.30it/s]2026-02-10 16:51:22,117 Video created: videos/ddppo_pretrained_eval/episode=29_1-ckpt=0-distance_to_goal=0.07-success=1.00-spl=0.98-distance_to_goal_reward=-0.00.mp4
100%|██████████████████████████████████████| 17/17 [00:00<00:00, 607.27it/s]
 90%|████████████████████████████████████    | 9/10 [00:02<00:00,  4.63it/s]2026-02-10 16:51:22,297 Video created: videos/ddppo_pretrained_eval/episode=23_1-ckpt=0-distance_to_goal=0.11-success=1.00-spl=1.00-distance_to_goal_reward=-0.00.mp4
100%|██████████████████████████████████████| 16/16 [00:00<00:00, 496.49it/s]
100%|███████████████████████████████████████| 10/10 [00:02<00:00,  4.30it/s]2026-02-10 16:51:22,567 Video created: videos/ddppo_pretrained_eval/episode=19_1-ckpt=0-distance_to_goal=0.07-success=1.00-spl=0.96-distance_to_goal_reward=-0.00.mp4
100%|██████████████████████████████████████| 29/29 [00:00<00:00, 926.57it/s]
100%|███████████████████████████████████████| 10/10 [00:02<00:00,  3.73it/s]
2026-02-10 16:51:22,650 Average episode spl: 0.9703
2026-02-10 16:51:22,650 Average episode success: 1.0000
2026-02-10 16:51:22,650 Average episode distance_to_goal_reward: 0.0000
2026-02-10 16:51:22,650 Average episode reward: 4.1383
2026-02-10 16:51:22,650 Average episode distance_to_goal: 0.0625
(habitat) liuyi@liuyi:~/projects/habitat-lab$ ls -lh videos/ddppo_pretrained_eval
total 176K
-rw-rw-r-- 1 liuyi liuyi 16K Feb 10 16:51 'episode=12_1-ckpt=0-distance_to_goal=0.02-success=1.00-spl=0.96-distance_to_goal_reward=-0.00.mp4'
-rw-rw-r-- 1 liuyi liuyi 22K Feb 10 16:51 'episode=19_1-ckpt=0-distance_to_goal=0.07-success=1.00-spl=0.96-distance_to_goal_reward=-0.00.mp4'
-rw-rw-r-- 1 liuyi liuyi 11K Feb 10 16:51 'episode=23_1-ckpt=0-distance_to_goal=0.11-success=1.00-spl=1.00-distance_to_goal_reward=-0.00.mp4'
-rw-rw-r-- 1 liuyi liuyi 19K Feb 10 16:51 'episode=26_1-ckpt=0-distance_to_goal=0.02-success=1.00-spl=0.95-distance_to_goal_reward=-0.00.mp4'
-rw-rw-r-- 1 liuyi liuyi 13K Feb 10 16:51 'episode=29_1-ckpt=0-distance_to_goal=0.07-success=1.00-spl=0.98-distance_to_goal_reward=-0.00.mp4'
-rw-rw-r-- 1 liuyi liuyi 13K Feb 10 16:51 'episode=3_1-ckpt=0-distance_to_goal=0.05-success=1.00-spl=1.00-distance_to_goal_reward=-0.00.mp4'
-rw-rw-r-- 1 liuyi liuyi 14K Feb 10 16:51 'episode=33_1-ckpt=0-distance_to_goal=0.13-success=1.00-spl=1.00-distance_to_goal_reward=-0.00.mp4'
-rw-rw-r-- 1 liuyi liuyi 20K Feb 10 16:51 'episode=35_1-ckpt=0-distance_to_goal=0.04-success=1.00-spl=0.94-distance_to_goal_reward=-0.00.mp4'
-rw-rw-r-- 1 liuyi liuyi 19K Feb 10 16:51 'episode=39_1-ckpt=0-distance_to_goal=0.06-success=1.00-spl=0.91-distance_to_goal_reward=-0.00.mp4'
-rw-rw-r-- 1 liuyi liuyi 13K Feb 10 16:51 'episode=7_1-ckpt=0-distance_to_goal=0.05-success=1.00-spl=1.00-distance_to_goal_reward=-0.00.mp4'
(habitat) liuyi@liuyi:~/projects/habitat-lab$ python -u -m habitat_baselines.run \
  --config-name=pointnav/ddppo_pointnav.yaml \
  benchmark/nav/pointnav=pointnav_habitat_test \
  habitat_baselines.evaluate=True \
  habitat_baselines.eval.should_load_ckpt=False \
  habitat_baselines.eval.video_option=[disk] \
  habitat_baselines.rl.ddppo.pretrained=True \
  habitat_baselines.rl.ddppo.pretrained_weights=data/ddppo-models/gibson-2plus-resnet50.pth \
  'habitat.gym.obs_keys=[depth,pointgoal_with_gps_compass]' \
  habitat.task.measurements.top_down_map.type=TopDownMap \
  habitat.task.measurements.top_down_map.fog_of_war.draw=True \
  habitat.task.measurements.top_down_map.draw_shortest_path=True \
  habitat_baselines.load_resume_state_config=False \
  habitat_baselines.num_environments=1 \
  habitat_baselines.test_episode_count=10 \
  habitat_baselines.video_dir=videos/ddppo_pretrained_eval_tdm
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
Could not override 'habitat.task.measurements.top_down_map.type'.
To append to your config use +habitat.task.measurements.top_down_map.type=TopDownMap
Key 'top_down_map' is not in struct
    full_key: habitat.task.measurements.top_down_map
    reference_type=Dict[str, MeasurementConfig]
    object_type=dict

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
(habitat) liuyi@liuyi:~/projects/habitat-lab$ python -u -m habitat_baselines.run \
  --config-name=pointnav/ddppo_pointnav.yaml \
  benchmark/nav/pointnav=pointnav_habitat_test \
  habitat_baselines.evaluate=True \
  habitat_baselines.eval.should_load_ckpt=False \
  habitat_baselines.eval.video_option=[disk] \
  habitat_baselines.rl.ddppo.pretrained=True \
  habitat_baselines.rl.ddppo.pretrained_weights=data/ddppo-models/gibson-2plus-resnet50.pth \
  'habitat.gym.obs_keys=[depth,pointgoal_with_gps_compass]' \
  +habitat/task/measurements=top_down_map \
  habitat.task.measurements.top_down_map.fog_of_war.draw=True \
  habitat.task.measurements.top_down_map.draw_shortest_path=True \
  habitat_baselines.test_episode_count=10 \
  habitat_baselines.video_dir=videos/ddppo_pretrained_eval_tdm
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
In 'pointnav/ddppo_pointnav.yaml': Could not find 'pointnav/habitat/task/measurements/top_down_map'

Config search path:
	provider=hydra, path=pkg://hydra.conf
	provider=main, path=file:///home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/config
	provider=habitat, path=pkg://habitat.config
	provider=habitat, path=pkg://habitat_baselines.config
	provider=schema, path=structured://

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
(habitat) liuyi@liuyi:~/projects/habitat-lab$ python -u -m habitat_baselines.run \
  --config-name=pointnav/ddppo_pointnav.yaml \
  benchmark/nav/pointnav=pointnav_habitat_test \
  habitat_baselines.evaluate=True \
  habitat_baselines.eval.should_load_ckpt=False \
  habitat_baselines.eval.video_option=[disk] \
  habitat_baselines.rl.ddppo.pretrained=True \
  habitat_baselines.rl.ddppo.pretrained_weights=data/ddppo-models/gibson-2plus-resnet50.pth \
  'habitat.gym.obs_keys=[depth,pointgoal_with_gps_compass]' \
  '+habitat.task.measurements.top_down_map={type:TopDownMap,draw_shortest_path:True,fog_of_war:{draw:True}}' \
  +habitat/simulator/sim_sensors@habitat_baselines.eval.extra_sim_sensors.third_rgb_sensor=third_rgb_sensor \
  habitat_baselines.load_resume_state_config=False \
  habitat_baselines.checkpoint_folder=data/new_checkpoints_pretrained_eval_tmp \
  habitat_baselines.test_episode_count=10 \
  habitat_baselines.video_dir=videos/ddppo_pretrained_eval_tdm
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
In 'pointnav/ddppo_pointnav.yaml': Could not find 'pointnav/habitat/simulator/sim_sensors/third_rgb_sensor'

Config search path:
	provider=hydra, path=pkg://hydra.conf
	provider=main, path=file:///home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/config
	provider=habitat, path=pkg://habitat.config
	provider=habitat, path=pkg://habitat_baselines.config
	provider=schema, path=structured://

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
(habitat) liuyi@liuyi:~/projects/habitat-lab$ python -u -m habitat_baselines.run \
  --config-name=pointnav/ddppo_pointnav.yaml \
  benchmark/nav/pointnav=pointnav_habitat_test \
  habitat_baselines.evaluate=True \
  habitat_baselines.eval.should_load_ckpt=False \
  habitat_baselines.eval.video_option=[disk] \
  habitat_baselines.rl.ddppo.pretrained=True \
  habitat_baselines.rl.ddppo.pretrained_weights=data/ddppo-models/gibson-2plus-resnet50.pth \
  'habitat.gym.obs_keys=[depth,pointgoal_with_gps_compass]' \
  '+habitat.task.measurements.top_down_map={type:TopDownMap,draw_shortest_path:True,fog_of_war:{draw:True}}' \
  habitat_baselines.load_resume_state_config=False \
  habitat_baselines.checkpoint_folder=data/new_checkpoints_pretrained_eval_tmp \
  habitat_baselines.test_episode_count=10 \
  habitat_baselines.video_dir=videos/ddppo_pretrained_eval_tdm
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
Error merging override +habitat.task.measurements.top_down_map={type:TopDownMap,draw_shortest_path:True,fog_of_war:{draw:True}}
Invalid type assigned: dict is not a subclass of MeasurementConfig. value: {'type': 'TopDownMap', 'draw_shortest_path': True, 'fog_of_war': {'draw': True}}
    full_key: top_down_map
    object_type=None

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
(habitat) liuyi@liuyi:~/projects/habitat-lab$ python -u -m habitat_baselines.run \
  --config-name=pointnav/ddppo_pointnav_pretrained_tdm.yaml \
  benchmark/nav/pointnav=pointnav_habitat_test
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 17:04:59,498 Loading resume state: data/new_checkpoints/.habitat-resume-stateeval.pth
/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ddppo/ddp_utils.py:224: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
  return torch.load(filename, map_location="cpu")
2026-02-10 17:04:59,518 Initializing dataset PointNav-v1
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 17:05:01,818 Initializing dataset PointNav-v1
2026-02-10 17:05:01,820 initializing sim Sim-v0
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
Renderer: NVIDIA GeForce RTX 4060 Laptop GPU/PCIe/SSE2 by NVIDIA Corporation
OpenGL version: 4.6.0 NVIDIA 580.95.05
Using optional features:
    GL_ARB_vertex_array_object
    GL_ARB_separate_shader_objects
    GL_ARB_robustness
    GL_ARB_texture_storage
    GL_ARB_texture_view
    GL_ARB_framebuffer_no_attachments
    GL_ARB_invalidate_subdata
    GL_ARB_texture_storage_multisample
    GL_ARB_multi_bind
    GL_ARB_direct_state_access
    GL_ARB_get_texture_sub_image
    GL_ARB_texture_filter_anisotropic
    GL_KHR_debug
    GL_KHR_parallel_shader_compile
    GL_NV_depth_buffer_float
Using driver workarounds:
    no-forward-compatible-core-context
    nv-egl-incorrect-gl11-function-pointers
    no-layout-qualifiers-on-old-glsl
    nv-zero-context-profile-mask
    nv-implementation-color-read-format-dsa-broken
    nv-cubemap-inconsistent-compressed-image-size
    nv-cubemap-broken-full-compressed-image-query
    nv-compressed-block-size-in-bits
[17:05:01:897409]:[Warning]:[Metadata] SceneDatasetAttributes.cpp(107)::addNewSceneInstanceToDataset : Dataset : 'default' : Lighting Layout Attributes 'no_lights' specified in Scene Attributes but does not exist in dataset, so creating default.
[17:05:01:897479]:[Warning]:[Scene] SemanticScene.h(331)::checkFileExists : ::loadSemanticSceneDescriptor: File `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` does not exist.  Aborting load.
[17:05:01:897489]:[Warning]:[Scene] SemanticScene.cpp(123)::loadSemanticSceneDescriptor : SSD File Naming Issue! Neither SemanticAttributes-provided name : `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` nor constructed filename : `data/scene_datasets/habitat-test-scenes/info_semantic.json` exist on disk.
[17:05:01:897496]:[Error]:[Scene] SemanticScene.cpp(139)::loadSemanticSceneDescriptor : SSD Load Failure! File with SemanticAttributes-provided name `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` exists but failed to load.
[17:05:02:435565]:[Warning]:[Sim] Simulator.cpp(595)::instanceStageForSceneAttributes : The active scene does not contain semantic annotations : activeSemanticSceneID_ = 0
2026-02-10 17:05:02,437 Initializing task Nav-v0
/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/single_agent_access_mgr.py:205: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
  pretrained_state = torch.load(
2026-02-10 17:05:03,011 Number of params to train: 12454917
2026-02-10 17:05:03,012 Agent number of parameters: 12454917
  0%|                                                | 0/10 [00:00<?, ?it/s]Error executing job with overrides: ['benchmark/nav/pointnav=pointnav_habitat_test']
Traceback (most recent call last):
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/run.py", line 31, in main
    execute_exp(cfg, "eval" if cfg.habitat_baselines.evaluate else "train")
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/run.py", line 62, in execute_exp
    trainer.eval()
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/common/base_trainer.py", line 129, in eval
    self._eval_checkpoint(
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/ppo_trainer.py", line 889, in _eval_checkpoint
    evaluator.evaluate_agent(
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/habitat_evaluator.py", line 241, in evaluate_agent
    frame = overlay_frame(frame, disp_info)
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/utils/visualizations/utils.py", line 370, in overlay_frame
    lines.append(f"{k}: {v:.2f}")
TypeError: unsupported format string passed to numpy.ndarray.__format__

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
Exception ignored in: <function VectorEnv.__del__ at 0x7e706bd1f1f0>
Traceback (most recent call last):
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/core/vector_env.py", line 613, in __del__
    self.close()
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/core/vector_env.py", line 470, in close
    write_fn((CLOSE_COMMAND, None))
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/core/vector_env.py", line 131, in __call__
    self.write_fn(data)
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/utils/pickle5_multiprocessing.py", line 63, in send
    self.send_bytes(buf.getvalue())
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/multiprocessing/connection.py", line 200, in send_bytes
    self._send_bytes(m[offset:offset + size])
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/multiprocessing/connection.py", line 411, in _send_bytes
    self._send(header + buf)
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/multiprocessing/connection.py", line 368, in _send
    n = write(self._handle, buf)
BrokenPipeError: [Errno 32] Broken pipe
  0%|                                                | 0/10 [00:00<?, ?it/s]
(habitat) liuyi@liuyi:~/projects/habitat-lab$ cd ~/projects/habitat-lab
conda activate habitat
export TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD=1

python -u -m habitat_baselines.run \
  --config-name=pointnav/ddppo_pointnav_pretrained_tdm.yaml \
  benchmark/nav/pointnav=pointnav_habitat_test
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 17:07:38,852 Initializing dataset PointNav-v1
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 17:07:41,062 Initializing dataset PointNav-v1
2026-02-10 17:07:41,064 initializing sim Sim-v0
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
Renderer: NVIDIA GeForce RTX 4060 Laptop GPU/PCIe/SSE2 by NVIDIA Corporation
OpenGL version: 4.6.0 NVIDIA 580.95.05
Using optional features:
    GL_ARB_vertex_array_object
    GL_ARB_separate_shader_objects
    GL_ARB_robustness
    GL_ARB_texture_storage
    GL_ARB_texture_view
    GL_ARB_framebuffer_no_attachments
    GL_ARB_invalidate_subdata
    GL_ARB_texture_storage_multisample
    GL_ARB_multi_bind
    GL_ARB_direct_state_access
    GL_ARB_get_texture_sub_image
    GL_ARB_texture_filter_anisotropic
    GL_KHR_debug
    GL_KHR_parallel_shader_compile
    GL_NV_depth_buffer_float
Using driver workarounds:
    no-forward-compatible-core-context
    nv-egl-incorrect-gl11-function-pointers
    no-layout-qualifiers-on-old-glsl
    nv-zero-context-profile-mask
    nv-implementation-color-read-format-dsa-broken
    nv-cubemap-inconsistent-compressed-image-size
    nv-cubemap-broken-full-compressed-image-query
    nv-compressed-block-size-in-bits
[17:07:41:142680]:[Warning]:[Metadata] SceneDatasetAttributes.cpp(107)::addNewSceneInstanceToDataset : Dataset : 'default' : Lighting Layout Attributes 'no_lights' specified in Scene Attributes but does not exist in dataset, so creating default.
[17:07:41:142753]:[Warning]:[Scene] SemanticScene.h(331)::checkFileExists : ::loadSemanticSceneDescriptor: File `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` does not exist.  Aborting load.
[17:07:41:142764]:[Warning]:[Scene] SemanticScene.cpp(123)::loadSemanticSceneDescriptor : SSD File Naming Issue! Neither SemanticAttributes-provided name : `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` nor constructed filename : `data/scene_datasets/habitat-test-scenes/info_semantic.json` exist on disk.
[17:07:41:142770]:[Error]:[Scene] SemanticScene.cpp(139)::loadSemanticSceneDescriptor : SSD Load Failure! File with SemanticAttributes-provided name `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` exists but failed to load.
[17:07:41:679761]:[Warning]:[Sim] Simulator.cpp(595)::instanceStageForSceneAttributes : The active scene does not contain semantic annotations : activeSemanticSceneID_ = 0
2026-02-10 17:07:41,681 Initializing task Nav-v0
/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/single_agent_access_mgr.py:205: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
  pretrained_state = torch.load(
2026-02-10 17:07:42,356 Number of params to train: 12454917
2026-02-10 17:07:42,357 Agent number of parameters: 12454917
 10%|████                                    | 1/10 [00:10<01:36, 10.76s/it]2026-02-10 17:07:54,887 Video created: videos/ddppo_pretrained_eval_tdm/episode=7_1-ckpt=0-distance_to_goal=0.05-success=1.00-spl=1.00-distance_to_goal_reward=-0.00.mp4
  5%|█▉                                      | 1/21 [00:00<00:02,  7.04it/s]
Error executing job with overrides: ['benchmark/nav/pointnav=pointnav_habitat_test']
Traceback (most recent call last):
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/run.py", line 31, in main
    execute_exp(cfg, "eval" if cfg.habitat_baselines.evaluate else "train")
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/run.py", line 62, in execute_exp
    trainer.eval()
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/common/base_trainer.py", line 129, in eval
    self._eval_checkpoint(
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/ppo_trainer.py", line 889, in _eval_checkpoint
    evaluator.evaluate_agent(
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/habitat_evaluator.py", line 261, in evaluate_agent
    generate_video(
  File "/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/utils/common.py", line 433, in generate_video
    images_to_video(
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/utils/visualizations/utils.py", line 145, in images_to_video
    writer.append_data(im)
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/imageio/core/format.py", line 590, in append_data
    return self._append_data(im, total_meta)
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/imageio/plugins/ffmpeg.py", line 591, in _append_data
    raise ValueError("All images in a movie should have same size")
ValueError: All images in a movie should have same size

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
Exception ignored in: <function VectorEnv.__del__ at 0x744c368b91f0>
Traceback (most recent call last):
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/core/vector_env.py", line 613, in __del__
    self.close()
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/core/vector_env.py", line 470, in close
    write_fn((CLOSE_COMMAND, None))
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/core/vector_env.py", line 131, in __call__
    self.write_fn(data)
  File "/home/liuyi/projects/habitat-lab/habitat-lab/habitat/utils/pickle5_multiprocessing.py", line 63, in send
    self.send_bytes(buf.getvalue())
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/multiprocessing/connection.py", line 200, in send_bytes
    self._send_bytes(m[offset:offset + size])
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/multiprocessing/connection.py", line 411, in _send_bytes
    self._send(header + buf)
  File "/home/liuyi/miniforge3/envs/habitat/lib/python3.9/multiprocessing/connection.py", line 368, in _send
    n = write(self._handle, buf)
BrokenPipeError: [Errno 32] Broken pipe
 10%|████                                    | 1/10 [00:11<01:39, 11.10s/it]
(habitat) liuyi@liuyi:~/projects/habitat-lab$ python -u -m habitat_baselines.run \
  --config-name=pointnav/ddppo_pointnav_pretrained_tdm.yaml \
  benchmark/nav/pointnav=pointnav_habitat_test
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 17:26:39,687 Initializing dataset PointNav-v1
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 17:26:41,971 Initializing dataset PointNav-v1
2026-02-10 17:26:41,973 initializing sim Sim-v0
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
Renderer: NVIDIA GeForce RTX 4060 Laptop GPU/PCIe/SSE2 by NVIDIA Corporation
OpenGL version: 4.6.0 NVIDIA 580.95.05
Using optional features:
    GL_ARB_vertex_array_object
    GL_ARB_separate_shader_objects
    GL_ARB_robustness
    GL_ARB_texture_storage
    GL_ARB_texture_view
    GL_ARB_framebuffer_no_attachments
    GL_ARB_invalidate_subdata
    GL_ARB_texture_storage_multisample
    GL_ARB_multi_bind
    GL_ARB_direct_state_access
    GL_ARB_get_texture_sub_image
    GL_ARB_texture_filter_anisotropic
    GL_KHR_debug
    GL_KHR_parallel_shader_compile
    GL_NV_depth_buffer_float
Using driver workarounds:
    no-forward-compatible-core-context
    nv-egl-incorrect-gl11-function-pointers
    no-layout-qualifiers-on-old-glsl
    nv-zero-context-profile-mask
    nv-implementation-color-read-format-dsa-broken
    nv-cubemap-inconsistent-compressed-image-size
    nv-cubemap-broken-full-compressed-image-query
    nv-compressed-block-size-in-bits
[17:26:42:055441]:[Warning]:[Metadata] SceneDatasetAttributes.cpp(107)::addNewSceneInstanceToDataset : Dataset : 'default' : Lighting Layout Attributes 'no_lights' specified in Scene Attributes but does not exist in dataset, so creating default.
[17:26:42:055511]:[Warning]:[Scene] SemanticScene.h(331)::checkFileExists : ::loadSemanticSceneDescriptor: File `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` does not exist.  Aborting load.
[17:26:42:055522]:[Warning]:[Scene] SemanticScene.cpp(123)::loadSemanticSceneDescriptor : SSD File Naming Issue! Neither SemanticAttributes-provided name : `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` nor constructed filename : `data/scene_datasets/habitat-test-scenes/info_semantic.json` exist on disk.
[17:26:42:055529]:[Error]:[Scene] SemanticScene.cpp(139)::loadSemanticSceneDescriptor : SSD Load Failure! File with SemanticAttributes-provided name `data/scene_datasets/habitat-test-scenes/van-gogh-room.scn` exists but failed to load.
[17:26:42:594636]:[Warning]:[Sim] Simulator.cpp(595)::instanceStageForSceneAttributes : The active scene does not contain semantic annotations : activeSemanticSceneID_ = 0
2026-02-10 17:26:42,596 Initializing task Nav-v0
/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/single_agent_access_mgr.py:205: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
  pretrained_state = torch.load(
2026-02-10 17:26:43,273 Number of params to train: 12454917
2026-02-10 17:26:43,274 Agent number of parameters: 12454917
 10%|████                                    | 1/10 [00:10<01:37, 10.86s/it]2026-02-10 17:26:55,919 Video created: videos/ddppo_pretrained_eval_tdm/episode=7_1-ckpt=0-distance_to_goal=0.05-success=1.00-spl=1.00-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:26:56,056][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1748, 512) to (1760, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|███████████████████████████████████████| 20/20 [00:00<00:00, 93.29it/s]
 20%|████████                                | 2/10 [00:24<01:40, 12.56s/it]2026-02-10 17:27:09,667 Video created: videos/ddppo_pretrained_eval_tdm/episode=26_1-ckpt=0-distance_to_goal=0.02-success=1.00-spl=0.95-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:27:09,668][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1748, 512) to (1760, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 26/26 [00:00<00:00, 417.69it/s]
 30%|████████████                            | 3/10 [00:33<01:14, 10.68s/it]2026-02-10 17:27:18,117 Video created: videos/ddppo_pretrained_eval_tdm/episode=33_1-ckpt=0-distance_to_goal=0.13-success=1.00-spl=1.00-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:27:18,117][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1748, 512) to (1760, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 15/15 [00:00<00:00, 285.53it/s]
 40%|████████████████                        | 4/10 [00:44<01:05, 10.92s/it]2026-02-10 17:27:29,398 Video created: videos/ddppo_pretrained_eval_tdm/episode=39_1-ckpt=0-distance_to_goal=0.06-success=1.00-spl=0.91-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:27:29,399][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1748, 512) to (1760, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 21/21 [00:00<00:00, 351.04it/s]
 50%|████████████████████                    | 5/10 [00:57<00:58, 11.69s/it]2026-02-10 17:27:42,448 Video created: videos/ddppo_pretrained_eval_tdm/episode=12_1-ckpt=0-distance_to_goal=0.02-success=1.00-spl=0.96-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:27:42,449][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1748, 512) to (1760, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 25/25 [00:00<00:00, 315.02it/s]
 60%|████████████████████████                | 6/10 [01:12<00:50, 12.69s/it]2026-02-10 17:27:57,091 Video created: videos/ddppo_pretrained_eval_tdm/episode=35_1-ckpt=0-distance_to_goal=0.04-success=1.00-spl=0.94-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:27:57,092][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1748, 512) to (1760, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 28/28 [00:00<00:00, 412.79it/s]
 70%|████████████████████████████            | 7/10 [01:21<00:35, 11.79s/it]2026-02-10 17:28:07,017 Video created: videos/ddppo_pretrained_eval_tdm/episode=3_1-ckpt=0-distance_to_goal=0.05-success=1.00-spl=1.00-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:28:07,017][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1748, 512) to (1760, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 18/18 [00:00<00:00, 294.58it/s]
 80%|████████████████████████████████        | 8/10 [01:30<00:21, 10.86s/it]2026-02-10 17:28:15,878 Video created: videos/ddppo_pretrained_eval_tdm/episode=29_1-ckpt=0-distance_to_goal=0.07-success=1.00-spl=0.98-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:28:15,878][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1748, 512) to (1760, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 16/16 [00:00<00:00, 282.53it/s]
 90%|████████████████████████████████████    | 9/10 [01:39<00:10, 10.08s/it]2026-02-10 17:28:24,258 Video created: videos/ddppo_pretrained_eval_tdm/episode=23_1-ckpt=0-distance_to_goal=0.11-success=1.00-spl=1.00-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:28:24,259][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1748, 512) to (1760, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 15/15 [00:00<00:00, 228.07it/s]
100%|███████████████████████████████████████| 10/10 [01:53<00:00, 11.46s/it]2026-02-10 17:28:38,812 Video created: videos/ddppo_pretrained_eval_tdm/episode=19_1-ckpt=0-distance_to_goal=0.07-success=1.00-spl=0.96-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:28:38,813][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1748, 512) to (1760, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 28/28 [00:00<00:00, 224.79it/s]
100%|███████████████████████████████████████| 10/10 [01:54<00:00, 11.41s/it]
2026-02-10 17:28:39,151 Average episode distance_to_goal_reward: 0.0000
2026-02-10 17:28:39,152 Average episode success: 1.0000
2026-02-10 17:28:39,152 Average episode distance_to_goal: 0.0625
2026-02-10 17:28:39,152 Average episode reward: 4.1383
2026-02-10 17:28:39,152 Average episode spl: 0.9703
(habitat) liuyi@liuyi:~/projects/habitat-lab$ 

(habitat) liuyi@liuyi:~/projects/habitat-lab$ python -u -m habitat_baselines.run \
  --config-name=pointnav/ddppo_pointnav_pretrained_tdm.yaml \
  benchmark/nav/pointnav=pointnav_habitat_test \
  habitat.dataset.data_path=data/custom_datasets/pointnav/habitat-test-scenes/v1/val_long10.json.gz \
  habitat_baselines.test_episode_count=10 \
  habitat_baselines.video_dir=videos/ddppo_pretrained_eval_tdm_long10
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 17:43:59,329 Initializing dataset PointNav-v1
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
pybullet build time: Jan 29 2025 23:20:52
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
/home/liuyi/miniforge3/envs/habitat/lib/python3.9/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
2026-02-10 17:44:01,567 Initializing dataset PointNav-v1
2026-02-10 17:44:01,568 initializing sim Sim-v0
PluginManager::Manager: duplicate static plugin StbImageImporter, ignoring
PluginManager::Manager: duplicate static plugin GltfImporter, ignoring
PluginManager::Manager: duplicate static plugin BasisImporter, ignoring
PluginManager::Manager: duplicate static plugin AssimpImporter, ignoring
PluginManager::Manager: duplicate static plugin AnySceneImporter, ignoring
PluginManager::Manager: duplicate static plugin AnyImageImporter, ignoring
Renderer: NVIDIA GeForce RTX 4060 Laptop GPU/PCIe/SSE2 by NVIDIA Corporation
OpenGL version: 4.6.0 NVIDIA 580.95.05
Using optional features:
    GL_ARB_vertex_array_object
    GL_ARB_separate_shader_objects
    GL_ARB_robustness
    GL_ARB_texture_storage
    GL_ARB_texture_view
    GL_ARB_framebuffer_no_attachments
    GL_ARB_invalidate_subdata
    GL_ARB_texture_storage_multisample
    GL_ARB_multi_bind
    GL_ARB_direct_state_access
    GL_ARB_get_texture_sub_image
    GL_ARB_texture_filter_anisotropic
    GL_KHR_debug
    GL_KHR_parallel_shader_compile
    GL_NV_depth_buffer_float
Using driver workarounds:
    no-forward-compatible-core-context
    nv-egl-incorrect-gl11-function-pointers
    no-layout-qualifiers-on-old-glsl
    nv-zero-context-profile-mask
    nv-implementation-color-read-format-dsa-broken
    nv-cubemap-inconsistent-compressed-image-size
    nv-cubemap-broken-full-compressed-image-query
    nv-compressed-block-size-in-bits
[17:44:01:643123]:[Warning]:[Metadata] SceneDatasetAttributes.cpp(107)::addNewSceneInstanceToDataset : Dataset : 'default' : Lighting Layout Attributes 'no_lights' specified in Scene Attributes but does not exist in dataset, so creating default.
[17:44:01:643252]:[Warning]:[Scene] SemanticScene.h(331)::checkFileExists : ::loadSemanticSceneDescriptor: File `data/scene_datasets/habitat-test-scenes/skokloster-castle.scn` does not exist.  Aborting load.
[17:44:01:643262]:[Warning]:[Scene] SemanticScene.cpp(123)::loadSemanticSceneDescriptor : SSD File Naming Issue! Neither SemanticAttributes-provided name : `data/scene_datasets/habitat-test-scenes/skokloster-castle.scn` nor constructed filename : `data/scene_datasets/habitat-test-scenes/info_semantic.json` exist on disk.
[17:44:01:643269]:[Error]:[Scene] SemanticScene.cpp(139)::loadSemanticSceneDescriptor : SSD Load Failure! File with SemanticAttributes-provided name `data/scene_datasets/habitat-test-scenes/skokloster-castle.scn` exists but failed to load.
[17:44:02:388780]:[Warning]:[Sim] Simulator.cpp(595)::instanceStageForSceneAttributes : The active scene does not contain semantic annotations : activeSemanticSceneID_ = 0
2026-02-10 17:44:02,390 Initializing task Nav-v0
/home/liuyi/projects/habitat-lab/habitat-baselines/habitat_baselines/rl/ppo/single_agent_access_mgr.py:205: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
  pretrained_state = torch.load(
2026-02-10 17:44:03,063 Number of params to train: 12454917
2026-02-10 17:44:03,064 Agent number of parameters: 12454917
 10%|████                                    | 1/10 [00:07<01:08,  7.57s/it]2026-02-10 17:44:12,209 Video created: videos/ddppo_pretrained_eval_tdm_long10/episode=12_1-ckpt=0-distance_to_goal=0.16-success=1.00-spl=0.99-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:44:12,381][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1455, 512) to (1456, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 67/67 [00:00<00:00, 213.59it/s]
 20%|████████                                | 2/10 [00:15<01:04,  8.08s/it]2026-02-10 17:44:20,637 Video created: videos/ddppo_pretrained_eval_tdm_long10/episode=36_1-ckpt=0-distance_to_goal=0.01-success=1.00-spl=0.98-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:44:20,637][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1455, 512) to (1456, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 76/76 [00:00<00:00, 468.73it/s]
 30%|████████████                            | 3/10 [00:22<00:51,  7.39s/it]2026-02-10 17:44:27,211 Video created: videos/ddppo_pretrained_eval_tdm_long10/episode=45_1-ckpt=0-distance_to_goal=0.11-success=1.00-spl=0.96-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:44:27,212][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1455, 512) to (1456, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 58/58 [00:00<00:00, 536.01it/s]
 40%|████████████████                        | 4/10 [00:28<00:41,  6.86s/it]2026-02-10 17:44:33,254 Video created: videos/ddppo_pretrained_eval_tdm_long10/episode=41_1-ckpt=0-distance_to_goal=0.15-success=1.00-spl=1.00-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:44:33,254][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1455, 512) to (1456, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 52/52 [00:00<00:00, 452.39it/s]
 50%|████████████████████                    | 5/10 [00:35<00:34,  6.95s/it]2026-02-10 17:44:40,354 Video created: videos/ddppo_pretrained_eval_tdm_long10/episode=16_1-ckpt=0-distance_to_goal=0.06-success=1.00-spl=0.96-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:44:40,355][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1455, 512) to (1456, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 65/65 [00:00<00:00, 574.36it/s]
 60%|████████████████████████                | 6/10 [00:43<00:28,  7.07s/it]2026-02-10 17:44:47,669 Video created: videos/ddppo_pretrained_eval_tdm_long10/episode=2_1-ckpt=0-distance_to_goal=0.14-success=1.00-spl=0.90-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:44:47,669][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1455, 512) to (1456, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 67/67 [00:00<00:00, 581.51it/s]
 70%|████████████████████████████            | 7/10 [00:50<00:21,  7.19s/it]2026-02-10 17:44:55,116 Video created: videos/ddppo_pretrained_eval_tdm_long10/episode=31_1-ckpt=0-distance_to_goal=0.16-success=1.00-spl=1.00-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:44:55,116][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1455, 512) to (1456, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 66/66 [00:00<00:00, 599.77it/s]
 80%|████████████████████████████████        | 8/10 [00:57<00:14,  7.20s/it]2026-02-10 17:45:02,342 Video created: videos/ddppo_pretrained_eval_tdm_long10/episode=17_1-ckpt=0-distance_to_goal=0.05-success=1.00-spl=0.95-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:45:02,343][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1455, 512) to (1456, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 67/67 [00:00<00:00, 624.93it/s]
 90%|████████████████████████████████████    | 9/10 [01:03<00:06,  6.84s/it]2026-02-10 17:45:08,383 Video created: videos/ddppo_pretrained_eval_tdm_long10/episode=43_1-ckpt=0-distance_to_goal=0.02-success=1.00-spl=1.00-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:45:08,383][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1455, 512) to (1456, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 53/53 [00:00<00:00, 605.02it/s]
100%|███████████████████████████████████████| 10/10 [01:11<00:00,  7.11s/it]2026-02-10 17:45:16,112 Video created: videos/ddppo_pretrained_eval_tdm_long10/episode=35_1-ckpt=0-distance_to_goal=0.11-success=1.00-spl=0.97-distance_to_goal_reward=-0.00.mp4
                                                                           [2026-02-10 17:45:16,113][imageio_ffmpeg][WARNING] - IMAGEIO FFMPEG_WRITER WARNING: input image is not divisible by macro_block_size=16, resizing from (1455, 512) to (1456, 512) to ensure video compatibility with most codecs and players. To prevent resizing, make your input image divisible by the macro_block_size or set the macro_block_size to 1 (risking incompatibility).
100%|██████████████████████████████████████| 72/72 [00:00<00:00, 624.69it/s]
100%|███████████████████████████████████████| 10/10 [01:11<00:00,  7.19s/it]
2026-02-10 17:45:16,562 Average episode reward: 13.9786
2026-02-10 17:45:16,563 Average episode distance_to_goal_reward: 0.0000
2026-02-10 17:45:16,563 Average episode spl: 0.9726
2026-02-10 17:45:16,563 Average episode distance_to_goal: 0.0972
2026-02-10 17:45:16,563 Average episode success: 1.0000
(habitat) liuyi@liuyi:~/projects/habitat-lab$ 

