Simulator Area
---------------

A configurable multicolumn interface that combines |TVB| simulation, analysis 
and visualization capabilities.

    .. figure:: screenshots/simulator.jpg
      :width: 90%
      :align: center

      Preview for Simulator Area


.. SIMULATOR COLUMN

Configure Simulation
.....................

On the central column, you have access to all the simulator components 
configurable settings. 

On the top of this column you have a field to enter the new simulation name. 
The `Launch` button on the top right of this column is used to start the 
simulation.


The `Configure Interface` button allows you to select which of the simulation 
fields are visible.


|TVB| performs region-based and surface-based simulations. 


Region-based simulations
~~~~~~~~~~~~~~~~~~~~~~~~

The `Set up region Model` button leads you to an interactive phase-plane display. 
This tool shows the 2-dimensional planes of the general n-dimensional 
phase space of the local dynamics model. It allows to observe how the dynamic 
behaviour of the physical model changes as a function of its parameters. 
See the API documentation for more details about this interactive display.

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


Parameter Space Exploration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to launch parallel simulations to systematically explore the 
parameter space of the local dynamics model. In the current TVB version, up to 
2 parameters can be inspected at the same time.

.. figure:: screenshots/simulator_pse_configuration.jpg
   :width: 60%
   :align: center
               
   The results will be presented in a discrete two dimensional graph. Each 
   point represents the results of a simulation for an unique combination of
   parameters. The disk size corresponds to Global Variance and the color scale
   corresponds to Variance of the Variance of nodes.  


.. HISTORY COLUMN

History
.......

On the left column, a history of all simulations is kept and can be 
accessed at any time. Each simulation can be renamed or deleted by 
clicking on the upper right `pencil` icon. 

.. caution:: 
    Please notice that **deleting a simulation will also delete all 
    resulting data that had been produced**.


.. VIEW COLUMN

VIEW: Visualizers for selected burst
....................................

* On the right column, there are three `View` tabs. Each one of those can be 
  personalized by selecting:

  - TVB time-series Visualizers that directly display simualtion results, or
  - TVB Visualizers associated with a TVB Analyzer. Simulation results are first
    processed an the analysis results are shown in the corresponding visualizer.

You can set up to 4 Visualizers/Analyzers per `View` tab.

* The `Results` tab contains the current simulation data structure tree.

.. note::

    Maximize this column by clicking on the `zoom` icon located in the top right
    corner.

.. include:: UserGuide-UI_Simulator-Visualizers.rst