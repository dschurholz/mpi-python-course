# mpi-python-course
MPI Python Course Resources

# Python Course First Week
Find the resources under folder [first_week](https://github.com/dschurholz/mpi-python-course/first_week/).

# Python Course Second Week
Find the resources under folder `second_week`. Please install the program Git following the next set of instructions in this file.

### Install Git
*Git* is a distributed version-control system for tracking changes in source code during software development. We will use *git* to start coding on the second part of the python code.

So first, please install *git* in your local machine. The following instruction will help you in different types of operating systems (OS):

1. Install the proper version for your OS:
    
    * **Windows**:
        download the installer from [Git Download](https://git-scm.com/downloads). Run the downloaded '.exe' file and follow the installation process. Look for the *GitBash* program and run it. The following program should open a window similar to:
            ![Git bash screenshot](https://www.logicbig.com/tutorials/misc/git/git-bash-shell/c/images/outputKey1.png "Windows Git Bash")

    * **MacOS**:
        download the installer from [Git Download](https://git-scm.com/downloads). Run the downloaded '.dmg' file and follow the installation process. Open a terminal\* and run the command `git --version` to see if *git* was installed correctly, you should get something similar to (the version number can be different):
            
            `git version 2.17.1`

        \* To open a terminal in Mac press `Command + Space-bar`, this opens a Spotlight search bar. Type `terminal` in the search bar and press enter. Other way to open a terminal is to go to the Applications folder, then to the Utilities folder and double click on the *terminal* application. 
 
    * **Linux**:
        Install it from a terminal `sudo apt install git-all` and wait for the program to install. Run the `git --version` command to see that installation has been correctly executed, you should get (the version number can be different):
            
            `git version 2.17.1`

### Install cookie-cutter
With a functioning installation of Anaconda or Miniconda, run the following commands:

1. Open a terminal window:

    * **Windows**: look for and run the AnacondaPowershell program.

    * **MacOS**: press `Command + Space-bar`, this opens a Spotlight search bar. Type `terminal` in the search bar and press enter. Other way to open a terminal is to go to the *Applications* folder, then to the *Utilities* folder and double click on the *terminal* application. 

    * **Linux**: press `ctrl + alt + t`

2. You can check that conda is active in your terminal, by noticing a `(base)` prefix in the command line. Install cookie-cutter by running the following command (same in all OS):
    `conda install cookie-cutter`

### Create a new conda environment (optional)
Conda environments allow us to separate dependencies (libraries) that are needed by our different projects. Some projects need different versions of those libraries and having all libraries in the same place for all projects would make this requirement a nightmare, when switching from one project to the next. Thus it is recommended to use a new environment for each new python project.

Open a terminal again (see previous subsection for this). Create and activate a new conda environment (same for all OS):
Run the following command in the terminal window:

`conda create --name python-course`

This will run some steps and create a new environment for our project. Then activate the newly created environment by running:

`conda activate python-course`

Now your terminal should have this `(python-course)` instead of `(base)` at the beginning of the command line.

Every new library that is installed will be added to this environment.

Finally, if you want to return to the `(base)` environment, meaning that you will deactivate the current environment, `(python-course)` for example, just run:

`conda deactivate`

Now `(base)` should show instead of `(python-course)` at the beginning of the command line.

*Handy conda commands*

* `conda env list`: to see all environments created in your local machine.

* `conda list`: to see all libraries installed in the current environment.

For more info check the [Conda documentation](https://docs.conda.io/en/latest/).