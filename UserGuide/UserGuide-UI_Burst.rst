Burst Area
----------

Configurable multipanel display that combines |TVB| simulation, analysis and
visualization capabilities.

.. figure:: screenshots/burst.png
   :width: 90%
   :align: center

   Preview for Burst Area

Through this interface, the user can have a quick glimpse (*burst*) of the dynamics
of a certain set of parameters. Moreover, it allows to explore the local dynamics model parameter space
(currently up to 2 parameters within the same *Burst* are supported) in a very methodological way.
From those results, the user will get an idea (a hint) of the most interesting parameter
combination to launch longer simulations.


You can save a new *Burst*, i.e., save a new set of parameters for a given model
or to save a simulation using a different model.

A history of previous *Bursts* is kept and can be accessed at any time.

On the right side there are configurable tabs which allow you to personalize
the windows to be displayed (from Analyzers or simple Visualizers).

Each window can be displayed in full screen by pressing the `Launch full visualizer`
button.

Some of the available visualizers are described below.

Brain Visualizer
................

A 3D (WebGL) visualization of the brain activity.

This visualizer displays the activity on the surface level (fine granularity - each
surface vertex has an individual measure) or on the region level
(coarse-granularity - each region is represented with only one color).


.. figure:: screenshots/brain.png
   :width: 90%
   :align: center

   Preview for Brain Viewer


EEG Visualizer
..............

An animated 2D EEG-like visualization of a timeseries.

You have the option to select particular channels for display
(at startup only maximun 10 are displayed).
You can zoom by selecting a specific area with mouse-selection.


.. figure:: screenshots/eeg.png
   :width: 90%
   :align: center

   Preview for EEG Viewer


BrainEEG
........

A synchronized side by side representation with a 3D webGL and a 2D EEG-like visualization
of brain activity.


.. figure:: screenshots/braineeg.png
   :width: 90%
   :align: center

   Preview for BrainEEG Viewer
   

.. raw:: pdf

   PageBreak oneColumn
   

Topographic Viewer
..................

A comparison between a maximum of 3 brain maps. Each map associates
a vector value to a node in the connectivity matrix.

.. figure:: screenshots/topografic.png
   :width: 90%
   :align: center

   Preview for Topographic Visualizer