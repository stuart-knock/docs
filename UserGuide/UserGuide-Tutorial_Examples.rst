Examples
--------

We present here some basic simulation scenarios that the user should be able to
reproduce through the |TVB| interface.

.. |example| image:: icons/applications-science.png

.. admonition:: |example| Example 1

    **Generating resting activity data using the default simulator configuration**

    **Objective**: generate 16 seconds of resting state activity data, sampled at 
    2048Hz, by launching a region-based simulation using a stochastic 
    integration method.


  #. Use the default long-range connectivity data.
  #. Apply a linear coupling function (parameters: `a`- rescale connection 
     strength=0.016, `b`- shift=0).
  #. Leave the *Cortical Surface* and the *Stimulus* set to **None**.
  #. Use the default population model and its parameters.
  #. Select the Heun Stochastic integrator. Set the integration step to 
     :math:`dt=0.06103515625` and additive noise (with null correlation time 
     and standard deviation :math:`D=2^{-10}`, use the default 
     random number generator parameters).
  #. Use the default model initial conditions (basically random initial 
     conditions).
  #. Select a Temporal Average Monitor (sampling period = 0.48828125 ms)
  #. Configure the portlets: select a Time Series Visualizer.
  #. Set the simulation length to 16000 ms
  #. Launch the simulation
  #. Observe the results: the default model state variable (membrane potential 
     in FitzHugh-Nagumo model).

  |

    Run time is approximately 4 minutes using one computing core of an Intel 
    Xeon Westemere 3.2 GHz, memory requirement < 1GB, data storage requirement
    ~ 19MB.


|


.. admonition:: |example| Example 2

    **Applying a stimulus on a region-based model**

    **Objective**: Create and apply a time-dependent stimulus to specific 
    region nodes.*

    #. Follow steps 1 and 2 from the previous example.
    #. Build the stimulus (See How to create a stimulus)
    #. Select a node from the 3D view on the left. Change its weight in the 
       'Current weight' cell.
    #. Press the 'Update weight' button.
    #. Do this for at least 5 nodes (assigning for instance 0.25, 0.15, 0.0625, 
       0.03125, 0.015625)
    #. Use a Gaussian for the temporal evolution of the stimulus (mean=15000 
       and standard deviation=4)
    #. Name the stimulus and press the 'Create the stimulus'
    #. Go back to the Burst Area and choose this specific stimulus into the 
       simulator.
    #. Follow steps 4 to 11 from the previous example.
