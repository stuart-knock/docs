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


Launch the Application
======================

On Linux
--------

Unzip the package and it will create a folder TVB_Distribution. In this folder
you should find a number of scripts. To start |TVB| you should run the
`tvb_start.sh` script. You can at any time run the `tvb_start_clean.sh` which
will start |TVB| in a clean state, resetting your program database and deleting
all the |TVB| created folders.

To make sure that no processes will remain opened after you use the application,
you should always close |TVB| by running the `tvb_stop.sh` script.

On MacOS
--------

Unzip the package and it will create a folder TVB_Distribution. In this folder
you should find a number of scripts and an application package. To start |TVB|
you should double click on the `tvb.app` application. You can at any time run
the `tvbStartClean.command` which will start tvb in a clean state, resetting
your program database and deleting all the |TVB| created folders.

To make sure that no processes will remain opened after you use the application,
you should always close |TVB| by running the `tvbStop.command` script.

On Windows
----------

Unzip the package and it will create a folder TVB_Distribution. In this folder
you should find a number of bat scripts and an executable. To start |TVB| you
should double click on the `tvbStart.exe` executable. You can at any time run
the `tvbStartClean.bat` which will start |TVB| in a clean state, resetting your
program database and deleting all the |TVB| created folders.


.. raw:: pdf

   PageBreak
   
.. USER INTERFACE

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


