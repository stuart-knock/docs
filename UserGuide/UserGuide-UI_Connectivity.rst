Connectivity Area
-----------------

.. figure:: screenshots/connectivity_area.png
   :width: 90%
   :align: center


Connectivity 3D
...............

Connectivity 3D Edges
~~~~~~~~~~~~~~~~~~~~~

This connectivity visualizer allows you to see the structural information as
base model part of TVB. On the left panel, the connectivity matrix is displayed
in 3D.

.. figure:: screenshots/connectivity.png
   :width: 90%
   :align: center

   Preview for Connectivity Viewer 3D Edges

The 3D semi-transparent surface arround the connectivity nodes, whether it is
the cortical surface or the outer-skin, is used just for giving space guidance.

You can select an individual node and righ-click on it to visualize the incoming
or outgoing edges. For each node you can choose a different color to apply to its
edges.

.. figure:: screenshots/connectivity3d_coloredges.png
   :width: 90%
   :align: center

   Preview for Connectivity Viewer 3D Edges - Coloring incoming / outgoing edges


Connectivty 3D View
~~~~~~~~~~~~~~~~~~~

A 3D (WebGL) representation of the connectivity matrix.
Two specific node-measures can be displayed here by node gradient colors and
different node sizes.

.. figure:: screenshots/connectivity3d.png
   :width: 90%
   :align: center

   Preview for Connectivity 3D Viewer
 

Connectivity 2D Viewer
......................

A 2D representation of the connectivity matrix.

One can select node-by-node in the connectivity, to emphasize connections
between nodes and strength. Views are 2D Left, 2D Top and 2D Right.


.. figure:: screenshots/connectivity2d_left.png
   :width: 30%
   :align: left

.. figure:: screenshots/connectivity2d_top.png
   :width: 30%
   :align: center

.. figure:: screenshots/connectivity2d_right.png
   :width: 30%
   :align: right

   Preview for Connectivity 2D Viewer

Connectivity Matrix Editor
~~~~~~~~~~~~~~~~~~~~~~~~~~

On the right of every Connectivity display, a 2D table is also available for
easily editing the connectivity and the tract matrix, e.g., perform lesions and
save changes for a compared simulation.

You can select the quadrant to be displayed on the 2D table by accesing the
quadrant selector on the upper left corner of the matrix:

	- quadrants 1 and 4 are the intra-hemisphere connectivity weights,

	- and quadrants 2 and 3 are the inter-hemisphere connectivity weights.

.. figure:: screenshots/connectivity_quadrants.png
   :width: 90%
   :align: center

   Preview for Quadrant Selection

The Selection View tab on top of the connectivity matrix, labeled as *Weights
Matrix*, allows you to perform basic algebraic operations on a set of nodes.
In addition to that, you can specify the edge type, i.e., if the connection
strengths to be modified are going out or coming in from/to the selected nodes.

.. figure:: screenshots/connectivity3d_edges_operations.png
   :width: 90%
   :align: center

   Preview for Selection View

The operations are:
	- Assignation (set): assigns the given numeric value to all the nodes within the set.
	- Addition (add): adds the new value to the current value in the connectivity matrix.
	- Subtraction (decrease): subtracts the new value to the current value in the connectivity matrix.
	- Multiplication (multiply): multiplies the current value in the connectivity matrix by the given numeric value.
	- Division (divide): divides the current value in the connectivity matrix by the given numeric value.

Hit the `Run` button to perform the selected operation.

By default the set includes all the nodes. You can deselect the nodes from the
node list. If you wish to save a particular selection, enter a new name and hit
the Save Selection button.

.. figure:: screenshots/connectivity3d_newselection.png
   :width: 90%
   :align: center

   Preview for New Selection

The Connectivity Matrix editor allows you to perform lesions and save this changes
in a new connectivity matrix:

	- Deselect the nodes you want lesion by clicking directly on the region	labels. This will remove all the incoming and ongoing connections into	and from those nodes.
	- Hit the `Save Interest` button to save the new connectivity matrix.
	- Press the `Refresh` button below the Connectivity Matrix field, to see your new matrix. Select it.
	- `Launch` the viewer again

Your connectivity matrix should be displayed. The connection strengths of the
lesioned nodes should be set to 0.


Matrix  MPLH5 View
..................

A 2D (matplotlib) representation of the connectivity matrix. Here, the four
quadrants of the weights matrix can be observed.

.. figure:: screenshots/connectivity_mplh5.png
   :width: 90%
   :align: center

   Preview for Matrix Display