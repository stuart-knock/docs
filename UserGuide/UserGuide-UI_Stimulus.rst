Stimulus
--------

Spatio-temporal patterns can be generated to create stimulation patterns.

.. figure:: screenshots/stimulus_area.jpg
   :width: 90%
   :align: center

   Preview for Stimulus Area

.. note:: 
  
   **You can build stimuli for region-based and surface-based simulations**


Region level stimulus
.....................

**Edit Stimulus Equations page**

In this page we can define a stimulus temporal profile for each node 
independently. 

    .. figure:: screenshots/stimulus_region_edit.jpg
      :width: 90%
      :align: center


- On the left column, you will find configurable fields that will allow you to:
	
    - load a  preexisting `Region Stimulus` entity,
    - enter the name for a new entity and
    - select the associated `Connectivity` matrix that will be used to create a stimulus pattern.

|

Additionally, you can:

    - select the Temporal Equation that defines the profile and 
    - modify its parameters.

- On the right column, the stimulus temporal profile is presented.  

|

From the action bar in the right side you have access to:

|

**Set Region Scaling** page where you can:

	- select the nodes to which the temporal stimulus will be applied and
        - set the scaling value (stimulus strength) for those nodes.

	.. figure:: screenshots/stimulus_region_set_scaling.jpg
	   :width: 90%
	   :align: center

	   Preview for node selection in Stimulus at a region level

Click on **Save New Stimulus Region** button to create the new stimulus entity.
 

Surface level stimulus 
......................

**Edit Stimulus Equations**

In the case of a surface level stimulus, besides the temporal profile, you can 
define the spatial profile of your pattern.

    .. figure:: screenshots/stimulus_surface_edit.jpg
      :width: 90%
      :align: center
      
      Preview for Stimulus Surface edits

On the left column:
    
    - choose a preexisting `Surface Stimulus` or
    - enter the name for a new entity and :

      - select the associated `Surface` datatype. 
      - select the Spatial Equation that describes the spatial spread of the 
        stimulus and
      - set its parameters.

From the action bar in the right side you have access to:

**View Stimulus Progress** page where you are able to:

      - select the spatial focal points:

	- click on the surface, a blue pin will point to the selected point;  
        - click on `Add Focal Point` button to select this vertex, an orange 
          arrow will mark the added point;
	- repeat for each focal point.

|

.. figure:: screenshots/stimulus_surface_set_focal_points.jpg
   :width: 90%
   :align: center

   Preview for selecting the focal points

On the right column you will have the list of the selected focal points. You can 
delete them independently.  


.. hint :: 

	The spatial pattern will be centered around the focal points. 


Finally, after clicking on **Save New Stimulus Surface** button to create the 
new stimulus entity, you can visualize the evolution of the spatiotemporal pattern.

.. |play_icon| image:: icons/play_icon.png

Click on the |play_icon| button to launch the animation.

.. figure:: screenshots/stimulus_surface_play.jpg
   :width: 90%
   :align: center
   
   Preview of a spatiotemporal stimulus animation


.. tip::

	You can increase the complexity of a stimulus pattern by building 
        on top of one Stimulus entity.

        For an example on how to do it, please read the Test Cases in the User 
        Guide document.





