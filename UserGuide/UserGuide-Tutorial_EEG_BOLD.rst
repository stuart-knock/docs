|example| Tutorial
------------------

**Simulating EEG-fMRI whole brain dynamics for individual connectivity matrices**

**Objective**: 
learn how to generate simulated EEG and fMRI signals.

**Summary**: 
In |TVB| platform it is possible to edit a connectivity matrix to mimic brain 
lesions. In the present study, a lesion in a given node area is modeled by 
removing all the incoming and ongoing connections into and from this node.


1. Upload a connectivity data set following the steps described in the **Import 
   Data** section.

2. Upon uploading, the new connectivity set appears as entry in the `Project Data 
   Structure Tree`. 


  .. image:: screenshots/tutorial_eeg_bold_01.jpg
     :width: 90%
     :align: center


3. Upon clicking the new list entry, the `Datatype Details` overlay appears 
   enabling examination of object properties like summary statistics and basic 
   editing like setting metadata properties. Here you can assign your new 
   connectivity set to a custom subject name by changing the default `John Doe` 
   to a custom name and clicking `Save`. 

  .. image:: screenshots/tutorial_eeg_bold_02.jpg
     :width: 90%
     :align: center

  .. image:: screenshots/tutorial_eeg_bold_03.jpg
     :width: 90%
     :align: center


4.  In order to view and visually inspect your connectivity information launch 
    the Connectivity Viewer by selecting the tab `Visualizers` in the Datatype 
    Details overlay and clicking on `ConnectivityViewer`. At this point, it is 
    possible to adjust certain weights or tract lengths or to perform a lesion. 
    Please refer to the relevant sections of this tutorial for further details. 

5. You can now simulate brain activity using your own connectivity data. Switch 
   to the `Simulator` interface in order to configure simulation details. First, 
   assure that your new connectivity set is selected from the `Long-range connectivity` 
   drop-down menu. Then, configure further simulation properties like long-range 
   coupling function, conduction speed, cortical surface, stimuli, local 
   dynamics model, ranges and initial conditions of state variables, variables 
   to be recorded, integration scheme and step size, monitors and the simulation 
   length. For demonstration purposes use default settings, select **Spherical EEG** 
   and **BOLD** as monitors, name the new simulation and launch it. 

.. note::

  Please check that simulation length is larger than the BOLD sampling period!!

  .. image:: screenshots/tutorial_eeg_bold_04.jpg
     :width: 90%
     :align: center

6. In the `Projects` interface select `Operations` from the second-level tab 
   menu to follow the current status of the simulation. 

