.. |TITLE| replace:: User's Guide
.. |DESCRIPTION| replace:: Users's Guide presents the main functionalities of |TVB|
.. |VERSION| replace:: 1.0
.. |REVISION| replace:: 0.1

.. include:: ../templates/pdf_template.rst


|TVB| is a framework for the simulation of the dynamics of large-scale brain networks with biologically
realistic connectivity. |TVB| uses tractographic data (DTI/DSI) to generate connectivity matrices and build
cortical and subcortical brain networks. The dynamics of these networks is simulated and generates the time
courses of Local Fields Potentials in the brain, as well as brain imaging data such as EEG, MEG and BOLD
activations as observed in fMRI. Possible simulation studies currently include studies of the resting state,
lesions, and various stimulation paradigms. |TVB| is foremost a simulation platform, but also provides
a set of classical time series analysis tools, structural and functional connectivity analysis tools, as
well as parameter exploration facilities by launching parallel simulations on a cluster.

This document provides the most basic tutorial to get the new user started working with the first versions
of |TVB|. This version displays the full functionality of |TVB|. It is not limited to the basic simulation
and visualization functions, it now allows the user to handle parameter manipulation, stimulus generation
and connectivity edition. As the application will be regularly updated over the next few months so will
be this documentation. Hence please check regularly for updates on the web site: |TVB_URL|.

The principal structure of the workflow of |TVB| is composed of USER, PROJECT, BURST, SPACE-TIME, ANALYZE
and CONNECTIVITY. In **Project**, the individual projects are defined with all their data and
infrastructure. In **Burst** the large-scale simulation is defined and different options to view
structural and functional data are offered in 2D, 3D, as well other representations to visualize results.
Having multiple panels allow to have a quick overview of the current model parameters, simulations and
results. In **Analyze** certain options for data and connectivity analysis are offered.
In **SpaceTime**, stimulation patterns can be generated. And finally in **Connectivity**, the
user can edit the connectivity matrices assisted by interactive visualization tools.



Launch the Application
======================

On Linux
--------

Unzip the package and it will create a folder TVB_Distribution. In this folder
you should find a number of scripts. To start |TVB| you should run the `tvb_start.sh`
script. You can at any time run the `tvb_start_clean.sh` which will start tvb in a
clean state, resetting your program database and deleting all the |TVB| create folders.

To make sure that no processes will remain opened after you use the application, you
should always close |TVB| by running the `tvb_stop.sh` script.

On MacOS
--------

Unzip the package and it will create a folder TVB_Distribution. In this folder
you should find a number of scripts and an application package. To start |TVB| you
should double click on the `tvb.app` application. You can at any time run the
`tvbStartClean.command` which will start tvb in a clean state, resetting your program
database and deleting all the |TVB| create folders.

To make sure that no processes will remain opened after you use the application, you
should always close |TVB| by running the `tvbStop.command` script.

On Windows
----------

Unzip the package and it will create a folder TVB_Distribution. In this folder
you should find a number of bat scripts and an executable. To start |TVB| you
should double click on the `tvbStart.exe` executable. You can at any time run the
`tvbStartClean.bat` which will start TVB in a clean state, resetting your program
database and deleting all the |TVB| created folders.


.. raw:: pdf

   PageBreak
   
.. USER INTERFACE

.. include:: UserGuide-UI.rst

.. TEST CASES

.. include:: TestCases.rst 

.. DATA EXCHANGE

.. include:: DataExchange.rst 


