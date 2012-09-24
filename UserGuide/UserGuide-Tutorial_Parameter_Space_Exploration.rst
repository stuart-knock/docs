Tutorial 2
----------

**Parameter Space Exploration**

**Objective**: First, to run a batch job on the cluster or parallel processes in the
local machine to compute. Second, to understand the parameter space display.

  #. Follow steps 1 to 3 from the Example 1.
  #. Click on the 'V' button next to the model parameters if you want to see
      the available parameter range and step size. At present, a maximum of 2
      parameters can be explored at the same time.
  #. Launch simulation
  #. Choose three points within the parameter space. Each parameter set is 
      represented by a scalar measure.
  #. A 2D discrete representation will be displayed on the right side of the 
      screen and it will be updated each time several simulations are finished.
  #. From those results, the most relevant set of parameters can be 
      distinguished. Choose three points and run longer simulations for those 
      parameter sets.
  #. For each set, run the simulation four times for different degrees of 
      noise.
  #. Save data. These data will now be analyzed.
  #. Generate cross correlation matrix and coherence across all EEG sensors 
      (or subset) and for fMRI signal across all regions (or subset).
  #. Visualize on EEG map (circular map à la LP plus surface à la SK) and 
      cross sections (fMRI).
  #. Analyze EEG data via PCA. Visualize results:
    a. Plot modes of principal components and eigenvalues
    b. FFT or time series


  

.. figure:: screenshots/simulator_pse_configuration.jpg
  :width: 60%
  :align: center
  
  Each point in this two dimensional graph represents two metrics: by default
  Global Variance corresponds to the size of the point and Variance of the
  Variance of nodes maps the color scale. 
