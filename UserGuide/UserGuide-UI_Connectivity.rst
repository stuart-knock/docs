Connectivity
------------

In this area you can edit both types of TVB connectivity objects:

    - long-range connectivity and,
    - local connectivity.

    .. figure:: screenshots/connectivity_area.jpg
      :width: 90%
      :align: center

      Preview for Connectivity Area



Long Range Connectivity
.......................

    .. figure:: screenshots/connectivity_large_scale.jpg
       :width: 90%
       :align: center

       Large Scale Connectivity configuration page


From this page you can access: 

  - an interactive display tool on the `Control` right column and 
  - several Long Range Connectivity visualizations on the left `View` column.

      - 3D Views

	- Edges
	- Nodes

      - 2D Projections

	- Left
	- Right
	- Top

      - a (MPLH5) matrix plot



Connectivity Matrix Editor
~~~~~~~~~~~~~~~~~~~~~~~~~~

From the This 2D display allows you to:

  - easily edit the connectivity (tract lengths) matrix, and
  - create a modified version of your connectivity matrix
  - select a small subset of nodes
    - perform basic algebraic operations on that group
  - save all changes to use the new Connectivity object in a simulation.


.. note:: 

    In the Matrix Editor only one quadrant at the time is being displayed.
    You can select which quadrant is shown by accessing the quadrant selector 
    button in the upper left corner of the matrix display.
     
    - quadrants 1 and 4 are the intra-hemisphere connectivity weights,
    - and quadrants 2 and 3 are the inter-hemisphere connectivity weights.


      .. figure:: screenshots/connectivity_quadrants.jpg
	:width: 50%
	:align: center

      Preview for Quadrant Selection


The `Weights` button opens a menu that allows you to perform basic algebraic 
operations on a set of selected nodes specifying the edge type:

    - Incoming --> Incoming
    - Incoming --> Outgoing
    - Outgoing --> Incoming
    - Outgoing --> Outgoing

.. i.e., if the connection strengths to be modified are going out or coming in from/to the selected nodes.

.. figure:: screenshots/connectivity3d_edges_operations.jpg
   :width: 90%
   :align: center

   Preview for Operations on a selection of nodes


.. note:: 
  Available operations are:

  - Assignation (set): assigns the given numeric value to all the nodes within 
    the set.
  - Addition (add): adds the new value to the current value in the connectivity 
    matrix.
  - Subtraction (decrease): subtracts the new value to the current value in the 
    connectivity matrix.
  - Multiplication (multiply): multiplies the current value in the connectivity 
    matrix by the given numeric value.
  - Division (divide): divides the current value in the connectivity matrix by 
    the given numeric value.


Click on the `Apply weight change` button to perform the selected operation.

By default the set includes all the available nodes in the connectivity matrix. 
You can create a smaller selection by clicking on the `Quick-select` button and
editing the list of node names. 

.. |savetick| image:: icons/save_tick.png

To save a particular selection, enter a new name and click on |savetick|.

    .. figure:: screenshots/connectivity3d_newselection.jpg
      :width: 90%
      :align: center

      Preview for New Selection


|
|

Connectivity 3D Edges
~~~~~~~~~~~~~~~~~~~~~

This connectivity visualizer allows you to see the structural information as
base model part of TVB. On the left panel, the connectivity matrix is displayed
in 3D.

.. figure:: screenshots/connectivity3d.jpg
   :width: 50%
   :align: center

   Preview for Connectivity Viewer 3D Edges

The 3D semi-transparent surface arround the connectivity nodes, whether it is
the cortical surface or the outer-skin, is used just for giving space guidance.

You can select an individual node and righ-click on it to visualize the incoming
or outgoing edges. For each node you can choose a different color to apply to its
edges.

.. figure:: screenshots/connectivity3d_coloredges.jpg
   :width: 50%
   :align: center

   Preview for Connectivity Viewer 3D Edges - Coloring incoming / outgoing edges


|
|

Connectivty 3D View (Nodes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A 3D representation of the connectivity matrix nodes. (WebGL)

Two specific connectivity node-metrics, (previously computed) can be used to 
independently set: 
  
  - the node color and
  - the node size. 


.. figure:: screenshots/connectivity3d_viewer.jpg
   :width: 50%
   :align: center

   Preview for Connectivity 3D Viewer
 

|
|

Connectivity 2D Viewer
~~~~~~~~~~~~~~~~~~~~~~

A 2D representation of the connectivity matrix nodes and edges. 

There are three main views (projections):
 
  - 2D Left
  - 2D Top
  - 2D Right

.. figure:: screenshots/connectivity2d_left.jpg
   :width: 30%
   :align: left

.. figure:: screenshots/connectivity2d_top.jpg
   :width: 30%
   :align: center

.. figure:: screenshots/connectivity2d_right.jpg
   :width: 30%
   :align: right

   Preview for Connectivity 2D Viewer


|
|

Matrix (MPLH5) View
~~~~~~~~~~~~~~~~~~~~

A 2D matrix plot to have a complete overview of the initially selected connectivity 
matrix.

.. figure:: screenshots/connectivity_mplh5.jpg
   :width: 30%
   :align: right
   
   Preview for Matrix Display



Local Connectivity
..................

In this page, you can generate the spatial profile of local connectivity that 
will be used in surface-based simulations.

    .. figure:: screenshots/connectivity_local.jpg
      :width: 90%
      :align: center

    Local Connectivity editing page


On the lower right of the browser you will have access to different 
functionalities by clicking on:

    - `Create Local Connectivity` button: to generate the Local Connectivity entity.

    - `View Local Connectivity` button: to launch a 3D brain visualizer displaying the spatial profile of the newly generated entity.

	.. figure:: screenshots/local_connectivity_viewer.jpg
	  :width: 70%
	  :align: center

	Local Connectivity Viewer


    - `Edit Local Connectivity` button: to go back to the main Local Connectivity editing page.




 
 