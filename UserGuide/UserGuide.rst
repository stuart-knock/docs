.. |TITLE| replace:: User's Guide
.. |DESCRIPTION| replace:: Users's Guide presents the main functionalities of |TVB|
.. |VERSION| replace:: 1.0
.. |REVISION| replace:: 0.1

.. include:: ../templates/pdf_template.rst

Overview of |TVB|
=================

|TVB| is a framework for the simulation of the dynamics of large-scale brain
networks with biologically realistic connectivity. |TVB| uses tractographic data
(DTI/DSI) to generate connectivity matrices and build cortical and subcortical
brain networks. The connectivity matrix defines the connection strengths and 
time delays via signal transmission between all network nodes. Various neural 
mass models are available in the repertoire of |TVB| and define the dynamics of 
a network node.  Together, the neural mass models at the network nodes and the 
connectivity matrix define **the Virtual Brain**. |TVB| simulates and generates 
the time courses of various forms of neural activity including Local Field 
Potentials (LFP) and firing rate, as well as brain imaging data such as 
EEG, MEG and BOLD activations as observed in fMRI. 


|TVB| is foremost a scientific simulation platform and provides all means 
necessary to generate, manipulate and visualize connectivity and network 
dynamics. In addition, |TVB| comprises a set of classical time series analysis 
tools, structural and functional connectivity analysis tools, as well as 
parameter exploration facilities by launching parallel simulations on a cluster. 
The workflow of TVB is divided in **User**, **Project**, **Simulator**, 
**Analysis**, **Stimulus** and **Conectivity**. In **User**, the user can 
manage their account and |TVB| settings. In **Project**, the individual projects 
are defined with all their data and infrastructure. In **Simulator** the 
large-scale simulation is defined and different options to view structural and 
functional data are offered in 2D, 3D, as well other representations to 
visualize results. Having multiple panels allows having a quick overview of the 
current |TVB| model parameters, simulations and results. In **Analysis** certain 
options for data and connectivity analysis are offered. In **Stimulus**, 
patterns of stimuli can be generated. And finally in **Connectivity**, the user 
can edit the connectivity matrices assisted by interactive visualization tools.

This document provides the most basic tutorial to get the new user started 
working with |TVB|, version 1.0. As |TVB| will be updated regularly, please 
check for updates on our web site: http://www.thevirtualbrain.org.


Installing the Application
===========================

As |TVB| redefines what's possible in neuroscience utilizing off-the-shelf computer hardware, a few requirements are essential when using the software.

Requirements for front-end visualization:

- **High definition monitor** -
  Your monitor should be capable of displaying at least 1600 x 1000 pixels. Some views might be truncated if TVB is run on smaller monitors.

- **WebGL and WebSockets compatible browser** -
  We've tested the software on Mozilla Firefox 14+, Apple Safari 5.1+ and Google Chrome 20+.
  Using a different, less capable browser might result in some features not working or the user interface looking awkward at times.

- **WebGL-compatible graphics card** - 
  The graphic card has to support OpenGL version 2.0 or higher. The operating system needs to have a proper card driver as well to expose the graphic card towards WebGL.
  This requirement only affects PCs, not (somewhat recent) Macs.


Requirements for computation/storage power, dependent on the number of parallel simulations that will be executed concurrently:

- **CPU power** - 
  1 CPU core is needed for one simulation. When launching more simulations than the number of available cores, a serialization is recommended.
  This can be done by setting the "maximum number of parallel threads" (in TVB settings) to the same value as the number of cores. 

- **Memory** - 
  For a single simulation 8GB of RAM should be sufficient but 16GB are recommended.

- **Disk space** is also important, as simulating only 10 ms on surface level will occupy 280MB of disk space. A minimum of 50GB of space per user is a rough approximation.
   
- 32 bit packages will work fine, also when running on a 64 bit architecture.
  Please take note that some simulations on surface level might require more memory that 32 bit programs can address, 
  at which point the TVB software will notify you about this with a "Memory Error".

- Optional **MatLab or Octave** -
  A special feature in TVB is utilizing functions from the Brain Connectivity Toolbox.
  This feature thus requires a MatLab or Octave package on your computer (installed, activated and added to your OS' global PATH variable).
  The Brain Connectivity Toolbox doesn't need to be installed or enabled separately in any way, as TVB will temporarily append it to your MatLab/Octave path.


The TVB software package can be used in 3 different configurations:

- on a single machine (personal usage).
  This machine will need to meet the technical requirements from above for both the visualization and the computation/storage part.
  Any operation launched will use resources from current machine (graphic card, CPU, disk and RAM).
  
- in a client/server configuration, where TVB is installed on a server and made accessible to an unlimited number of users.

  This configuration is recommended when you have a powerful server to be used as back-end, where TVB is running and simulation or analysis operations are to be executed.
  The server machine will not require powerful graphics, as visualization will not be done here at all. Only the computation requirements from above will need to be met by the server.
  
  The visualization can be accessed from a personal computers by a browser (via HTTP).
  A network connection needs to exist between the server where TVB is running and the computer doing the visualization and access.
  http://${SERVER-IP}:8080 is the default URL. 
  
- using a cluster (similar with server installation, but with parallelization support).
  Please note that for cluster installations, OAR is expected to be configured separately from TVB and accessible to the user for which the TVB software is launched.
     
      
Launching the application is described in the next paragraphs, on all supported platforms.

On Linux
--------

Unzip the package and it will create a folder TVB_Distribution. In this folder
you should find a sub-folder `bin` with a number of scripts:

- tvb_start.sh
- tvb_clean.sh
- tvb_stop.sh
- tvb_command.sh
- tvb_library.sh
- contributor_setup.sh
 

To start |TVB| graphical interface in your web-browser, run the
`tvb_start.sh` script. You can run at any time `tvb_clean.sh` which
will start |TVB| in a clean state, resetting your program database and deleting
ALL folders and their content created by |TVB|. Be careful!

To make sure that no processes will remain open after you use the application,
you should always close |TVB| by running the `tvb_stop.sh` script.

To access the console interface, on a terminal, run `tvb_command.sh` or `tvb_library.sh`.
The interactive Python shell will appear. See the Shell and User Interface sections in this document for
more details on how to use the different interfaces of |TVB|.

The current |TVB| package was tested on Debian Squeeze and Fedora 16. 
Other Linux flavors might also work as long as you have installed a glibc 
version of 2.11 or higher.

For details on script `contributor_setup`, please read document `ContributorsManual.pdf`.

On MacOS
--------

Unzip the package and it will create a folder: TVB_Distribution. In this folder
you should find a number of scripts (in `bin` sub-folder) and an application package (`tvb.app`).

To start |TVB| in your web browser you should double-click on the `tvb.app` 
application. If you would rather use the shell interface, then execute one of the files
`tvb_command` or `tvb_library` from the `bin` folder. See the Shell and User Interface sections in this document for
more details on how to use the different interfaces of |TVB|.

Double click on `tvb.app` will launch the TVB software as a background process and will also try to
fire a browser window for you to start working with TVB. Please be patient, as depending on your computer
resources, the startup process might take about 1-2 minutes.

You can at any time run the `tvb_clean.command` which will reset
your TVB database and delete all folders created by |TVB|.

To make sure that no processes will remain open after you use the application,
you should always close |TVB| by running the `tvb_stop.command` script.

The current |TVB| version was tested on Mac OS X 10.5.8 (Leopard), 10.6.8 (Snow Leopard) and 10.7.2 (Lion)
but should also run smoothly on subsequent versions.

On Windows
----------

Unzip the package and it will create a folder TVB_Distribution. 
In this folder you should find sub-folder `bin` with a number of .bat scripts. 

To start |TVB| you should use `tvb_start.bat`. This will launch the TVB software with a console 
process for debugging, and will also try to fire a browser window for you to start working with TVB web interface.
If you rather use the shell interface, then execute one of the files
`tvb_command` or `tvb_library` from the `bin` folder. See the Shell and User Interface sections in this document for
more details on how to use the different interfaces of |TVB|.

You can at any time run `tvb_clean.bat` which will start tvb in a clean state, resetting
your program database and deleting all folders created by |TVB|.

To make sure that no processes will remain open after you use the application,
you should close |TVB| by running `tvb_stop.bat`, or close the previous opened console.

This version was tested on Windows XP (x32), Windows Server 2008 (x64) and Windows 7 (x64).



.. raw:: pdf

   PageBreak

.. SHELL INTERFACE
.. include:: UserGuide-Shell.rst
   
.. GRAPHICAL USER INTERFACE

.. include:: UserGuide-UI.rst

.. raw:: pdf

   PageBreak

.. TEST CASES

.. include:: UserGuide-Tutorial.rst

.. raw:: pdf

   PageBreak

.. DATA EXCHANGE

.. include:: DataExchange.rst

.. raw:: pdf

   PageBreak

.. COPYRIGHT

.. include:: ../templates/copyright_notice.rst


