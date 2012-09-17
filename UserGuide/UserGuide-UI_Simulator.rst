Simulator Area
---------------

A configurable multicolumn interface that combines |TVB| simulation, analysis 
and visualization capabilities.

    .. figure:: screenshots/simulator.jpg
      :width: 90%
      :align: center

      Preview for Simulator Area


Through this page, you can not only explore the parameter space of the local 
dynamics models (currently up to 2 parameters within the same simulation 
are supported) in a very methodological way, but also have a quick glimpse 
(*burst*) of the large-scale dynamics of a certain set of parameters and a given
connectivity matrix. 

From those results, the most relevant set of parameters can distinguished to 
launch longer simulations.

You can save a new simulation (or *burst*), i.e., save a new set of parameters 
for a given model or to save a simulation using a different model.


.. BURST HISTORY COLUMN

SELECT: Burst
.............

On the left column, a history of all previous simulations is kept and can be 
accessed at any time. Each simulation (*burst*) can be renamed or deleted by 
clicking on the upper right `pencil` icon. 

.. caution:: 
    Please notice that **deleting a burst will also delete all data that had 
    been produced and were related to that particular simulation**.


.. SIMULATOR COLUMN

Configuration: Simulation
..........................

On the central column, you have access to all the simulation configurable 
settings.

On the top of this column you have the field to enter the name of the current 
burst and the `Launch` button to start the simulation.

By clicking on the `Configure Interface` you can select which of the Simulator 
fields are visible. `Launch` simulation button is on the right. 


Region-based simulations
~~~~~~~~~~~~~~~~~~~~~~~~

The `Set up region Model` button leads you to an interactive phase-plane display. 
This tool let you see the 2-dimensional planes of the general n-dimensional 
phase space, and allows you to observe how the behaviour of the physical model 
changes as a function of its parameters. See the Reference Manual for more 
details about this interactive display.

    .. figure:: screenshots/simulator_phase_plane_interactive.jpg
      :width: 90%
      :align: center

      Preview for region model configuration.


Surface-based simulations
~~~~~~~~~~~~~~~~~~~~~~~~~

If you are launching a surface-based simulation, then it is possible to add 
more complexity by spatially varying the model parameters.
 
Click on `Set up surface model`. A new configuration page will be loaded.

    .. figure:: screenshots/simulator_spatialized_parameters.jpg
      :width: 90%
      :align: center

      Preview for surface model configuration.



.. VIEW COLUMN

VIEW: Visualizers for selected burst
....................................

* On the right column, there are three `portlet` tabs. Each one of those can be 
  personalized by selecting:

  - TVB time-series Visualizers that directly display simualtion results, or
  - TVB Visualizers associated with a TVB Analyzer. Simulation results are first
    processed an the analysis results are shown in the corresponding visualizer.

You can set up to 4 Visualizers/Analyzers per `portlet` tab.

* The `Burst Results` tab contains the current simulation data structure tree.

.. note::

    Maximize this column by clicking on the `zoom` icon located in the top right
    corner.

.. include:: UserGuide-UI_Simulator-Visualizers.rst