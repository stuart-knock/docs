Simulator Area
---------------

Configurable multipanel display that combines |TVB| simulation, analysis and
visualization capabilities.

.. figure:: screenshots/simulator.jpg
   :width: 90%
   :align: center

   Preview for Simulator Area

Through this interface, the user can have a quick glimpse (*burst*) of the dynamics
of a certain set of parameters. Moreover, it allows to explore the local dynamics model parameter space
(currently up to 2 parameters within the same simulation are supported) in a very methodological way.
From those results, the user will get an idea (a hint) of the most interesting parameter
combination to launch longer simulations.

You can save a new simulation (or *burst*), i.e., save a new set of parameters for a given model
or to save a simulation using a different model.

A history of previous all is kept and can be accessed at any time or deleted. Please, note that deleting a simulation will also delete all data that had been produced and were related to that particular simulation. 

On the right side there are configurable tabs which allow you to personalize
the windows to be displayed (from Analyzers or simple Visualizers).

Each window can be displayed in full screen by pressing the `Launch full visualizer`
button.

   

.. SIMULATOR COLUMN

    Surface
        the surfaces (cortex, skull, skin) for the resolution of forward problems.
    Connectivity
        connectivity matrix to use in the simulation.
    Coupling
        coupling fucntion between nodes of the network.
    Stimulus
        optional stimulation of the brain.
    Model and parameters:
        model type (such as Fitzhugh-Nagumo for example) and the parameters used in
        the simulation.
    Integrator
        the integration scheme for the differential equations and integration step (in physical unit).
	If the integration scheme is stochastic:
	Noise
	    the additive or multiplicative noise term used in the integration scheme.
    Monitors
        the data registered during the simulations.
    Simulation length:
        duration in physical time of the simulation (not to be confused with the
        computing duration)
    `Launch` simulation button on the right. 
    
.. VIEW COLUMN

.. include:: UserGuide-UI_Simulator-Visualizers.rst