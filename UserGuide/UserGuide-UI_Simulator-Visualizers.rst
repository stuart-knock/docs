.. VISUALIZERS COLUMN

.. |launch_full_viz| image:: icons/button_launch_full_visualizer.png
.. |brainicon| image:: icons/action_bar_brain.png

.. tip::
    By clicking on |launch_full_viz| you will be redirected to a new page 
    where the only the currently selected visualizer is displayed. In this new 
    page, you can click on |brainicon| in the top right corner to access a 
    new menu which will allow you to:

      - `Save` a snapshot of the current figure.
      - `Relaunch` the visualizer using a different entity. For instance, a 
        different time-series.

      .. figure:: screenshots/visualizer_save_figure.jpg
	  :width: 90%
	  :align: center
            
	  The main information about the selected project.


All the snapshots you save can be managed in  `Projects` --> `Image Archive` 
page.


Simple Visualizers
..................

Brain Activity Visualizer
~~~~~~~~~~~~~~~~~~~~~~~~~

A 3D visualization of the brain activity (based on WebGL)

It displays the brain activity:

- at the region level: the brain is represented by a coarse-granularity - each 
  region is represented with only one color.

.. figure:: screenshots/brain.jpg
   :width: 50%
   :align: center

   Preview for Brain Activity Visualizer at the region level

- at the surface level: the brain is represented by a fine granularity - each 
  surface vertex has an individual measure.



Time Series Visualizer
~~~~~~~~~~~~~~~~~~~~~~

.. figure:: screenshots/visualizer_timeseries_svgd3.jpg
   :width: 90%
   :align: center

   Preview for Time-Series Visualizer



Analyzers + Visualizers
.......................

Covariance Visualizer
~~~~~~~~~~~~~~~~~~~~~~

Displays the covariance matrix. Axes represent brain nodes. 

.. figure:: screenshots/visualizer_covariance.jpg
   :width: 90%
   :align: center

   Preview for Covariance Visualizer



Cross Coherence Visualizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Displays the cross-coherence matrix. Axes represent brain nodes. 

.. figure:: screenshots/visualizer_cross_coherence.jpg
   :width: 90%
   :align: center

   Preview for Cross Coherence Visualizer



Cross Correlation Visualizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Displays the cross-correlation matrix. Axes represent brain nodes. 



Fourier Spectrum Visualizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plots the power spectrum for each node time-series.

.. figure:: screenshots/visualizer_fft.jpg
   :width: 90%
   :align: center

   Preview for Fourier Spectrum Visualizer


Principal Component Visualizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On the left, the ring plot displays the fraction of the variance that is 
explained by each component.

On the right, the first ten components are plotted against the brain nodes. 

.. figure:: screenshots/analyzers_pca.jpg
   :width: 90%
   :align: center

   Preview for Principal Components Analysis Visualizer



Wavelet Spectrogram Visualizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2D representation that shows how the wavelet spectral coefficients (frequency) 
of the signals variy with time.

.. figure:: screenshots/visualizer_wavelet.jpg
   :width: 90%
   :align: center

   Preview for Wavelet Visualizer