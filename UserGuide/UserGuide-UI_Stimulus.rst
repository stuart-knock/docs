Stimulus Area
--------------

Spatio-temporal patterns can be generated to create stimulation patterns.

.. figure:: screenshots/stimulus_area.jpg
   :width: 90%
   :align: center

   Preview for Stimulus Area


Region level stimulus
.....................

    .. figure:: screenshots/stimulus_region.jpg
      :width: 90%
      :align: center


Surface level stimulus 
......................

    .. figure:: screenshots/stimulus_surface.jpg
      :width: 90%
      :align: center


.. admonition:: Important

    .. image:: screenshots/important.png
	:align: left
    
    Surfaces with more vertices than 256 x 256 x 256 are filtered out from Model 
    Parameters settings at the surface level, because the algorithm for vertices 
    picking only has that many colors to use. 

    We are planning, for the long-term, to have in |TVB| a surface shrinkage 
    algorithm. Given a large surface, a smaller one will be built to meet the 
    requirements for |TVB|. 


.. Surfaces with vertices more than 256 x 256 x 256 are filtered out from 
.. Surface Level Stimulus, because the algorithm for vertices pick only has so 
.. many colors to use. On long-term, the intention is to have in TVB a 
.. surface-shrink algorithm, that given a huge surface builds a smaller one for 
.. usage inside TVB. 