Test cases tutorial
===================

Simple simulation scenarios
---------------------------

We present here some basic simulation scenarios that the user should be able to
reproduce through the interface.


Example 1: Generating resting activity from the default data
............................................................

- Objective: generate 16 seconds of 2048Hz resting state activity data at the region level using a stochastic integration method.


1. Use the default long-range connectivity data.

2. Apply a linear coupling function (parameters: rescale connection strength=-0.016, shift=0).

3. Leave the *Cortical Surface* and the *Stimulus* set to **None**.

4. Use the default population model and its parameters.

5. Select the Heun Stochastic integrator. Intergration step set to :math:`dt=0.06103515625`
and additive noise (with null correlation time and an amplitude standard deviation :math:`D=2^{-10}`, use the default random number generator parameters).

6. Use the default model initial conditions (basically random initial conditions).

7. Select a Temporal Average Monitor (sampling period = 0.48828125 ms)

8. Configure the portlets: select a Time Series MPLH5 plot.

9. Set the simulation lenght to 16000 ms

10. Launch the simulation

11. Observe the results: the default model state variable (membrane potential in FitzHugh-Nagumo model).


Note: Run time is approximately 4 minutes using one computing core intel Xeon westemere 3.2 Ghz, memory requirement < 1GB, data storage
requirement ~ 19MB.


Example 2: Applying a stimulus on a region-based model
......................................................

- Objective: Apply a time-dependent stimulus to specific region nodes.

1. Follow steps 1 and 2 from the previous example.

2. Build the stimulus (See How to create a stimulus)

3. Select a node from the 3D view on the left. Change its weight in the 'Current weight' cell.

4. Press the 'Update weight' button.

5. Do this for at least 5 nodes (assigning for instance 0.25, 0.15, 0.0625, 0.03125, 0.015625)

6. Use a Gaussian for the temporal evolution of the stimulus (mean=15000 and standard deviation=4)

7. Name the stimulus and press the 'Create the stimulus'

8. Go back to the Burst Area and choose this specific stimulus into the simulator.

9. Follow steps 4 to 11 from the previous example.



Advanced test cases
-------------------


Track Burst History (?)
.......................

    PRECONDITION: minimal data set in place (connectivity matrix, surface and parcellation, nodes, fibre lengths)

    1. Set model family, parameters and generate network dynamics, as well as EEG and fMRI signals.

    2. Visualize time series of all nodes (or subset) and their FFT (or subset).

    3. Choose scalar measure: pick a single frequency component from FFT.  Key word: “chaining of analyzers”

    4. Set parameters and generate network dynamics

    5. Repeat steps 2 through 4 multiple times as often as desired.

    FUNCTION: track history, select and store figures from results, visualize them eventually next to
       each other. Selection of data on the basis of meta-data.


Example 3. Parameter Space Exploration
......................................

- Objective: Running a batch job on the cluster or parallel processes in the local machine.

1. Follow steps 1 to 3 from the Example 1.

2. Click on the 'V' button next to the model parameters if you want to see the
available parameter range and step size. At present, a maximum of 2 parameters
can be explored at the same time.

3. Launch simulation

4. Choose three points within the parameter space. Each parameter set is
represented by a scalar measure.

5. A discrete representation will be displayed on the right side of the screen and it
will be updated each time several simulations are finished.

.. figure:: screenshots/testcase_parameter_exploration.png
   :width: 70%
   :align: center

   Each point in this two dimensional graph represents two metrics: by default Global Variance
   corresponds to the size of the point and Variance of the Variance of nodes maps the color scale. 
		
5. Choose three points and run longer simulations for these three parameter sets.

6. For each set, run the simulation four times for different degrees of noise.

7. Save data. These data will now be analyzed.

8. Generate cross correlation matrix and coherence across all EEG sensors
	(or subset) and for fMRI signal across all regions (or subset).

9. Visualize on EEG map (circular map à la LP plus surface à la SK) and cross sections (fMRI).

10. Analyze EEG data via PCA. Visualize results:
        a. Plot modes of principal components and eigenvalues
        b. FFT or time series


Example 4. Perform a lesion
...........................

- Objective: learn how to use the connectivity editor by lesioning the connections
  between different brain regions.

1. Display the connectivity matrix with the Connectivity Viewer

2. Perform a Lesion.

3. Save the new connectivity matrix.


Example 5.
..........

How to generate Temporal and Spatiotemporal Stimuli?
====================================================

Region-based stimulus
---------------------

#. Select a node from the 3D view on the left. Change its weight in the 'Current weight' cell.

#. Press the 'Update weight' button.

#. Do this for at least 5 nodes (assigning for instance 0.25, 0.15, 0.0625, 0.03125, 0.015625)

#. Use a Gaussian for the temporal evolution of the stimulus

#. Name the stimulus and press the 'Create the stimulus'

#. Visualize the resulting pattern

#. Stimulus should be available from the Burst page

Surface-based stimulus
----------------------

#
Advanced surface-based
----------------------

Objective: generating a complex stimulus (a composition of sine waves)

#.



