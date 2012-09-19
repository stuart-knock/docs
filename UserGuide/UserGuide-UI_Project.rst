Project
-------

.. tip::
    
    Projects are the way you organise data and simulations in |TVB|. They
    correspond to directories where related data sets and simulation results
    are stored. Information on the currently selected project is always 
    available by clicking on the upper left corner of the interface:
        
        .. figure:: screenshots/project_info.jpg
            :width: 90%
            :align: center
            
            The main information about the selected project.
    

The `Project` tab provides access to the projects that you have created within
|TVB|. The second level menu in the top left corner, next to the Project number,
allows you to navigate between five main subpages, each of which is described in
more detail in the sections below:

    - View All Projects
    - Basic Properties
    - Operations
    - Data Structure
    - Saved Figures
    
    .. figure:: screenshots/project.jpg
        :width: 90%
        :align: center
        
        The Project second level menu
    

View All Projects
..................

This page provides a list of all the existing projects. Upon first user
registration, a default project is created for you:
    
    .. figure:: screenshots/default_project.jpg
        :width: 90%
        :align: center
        
        The default Project

The list of projects includes basic information about each project:

- who owns it
- the number of completed, pending, and failed operations.

as well as providing mechanisms for:

- selecting which project is currently active.
- editing any project's properties
- directly accessing `Operations` and `Data Structure` pages for any project.

In addition to the list of existing projects, the right hand menu provides a
way to:

- Create a new project.
- Import an existing project structure (for example, Exported from a
  colleague's installation of |TVB|).


Basic Properties
...................

Enables you to edit the current project's properties, you are also directed
to this page when you first create a new project:
    
    .. figure:: screenshots/project_form.jpg
        :width: 90%
        :align: center
        
        The Project Properties page
        
    .. note::
        
        You can also access this page for any existing project by clicking the
        edit button near a projects name on the `List of all Projects` page.
    
Fill in the form by:
  
  - adding a project's name (*without spaces*) 
  - writing a short description about the project.

.. tip::
  
  If there are other users registered in the framework, you can choose to
  share the project with them by checking their respective "Visible for" 
  boxes. 

On the right side of the browser there is the `Action Column` from where you can:

  - delete the project,
  - export the project or,
  - save changes. 

Clicking on the "X" button takes you back to the `List of All Projects` page. 

If you were creating a new project it should now be visible.

.. warning::

  Project properties cannot be edited while operations are running!



Operations
...........

A table with the history of operations related to the currently selected
project is displayed. From this board the user can filter, view, reload or
cancel any operation:
    
    .. figure:: screenshots/default_operations.jpg
        :width: 90%
        :align: center
        
        The operation page with default operations
    


Data Structure
...............

This page provides a way to navigate through the data associated with the
current project, there is a tree view:
    
    .. figure:: screenshots/data.jpg
        :width: 90%
        :align: center
        
        The data structure of the default project -- which automatically
        loads the default structural data necessary for a simulation.
    
and a graph view:
    
    .. figure:: screenshots/data_graph.jpg
        :width: 90%
        :align: center
        
        A graph view of the project's datastructure
    

Selecting a data node in the `View` column causes an overlay to appear:
    
    .. figure:: screenshots/data_overlay.jpg
        :width: 90%
        :align: center
        
        A data nodes overlay
    

From this overlay, the user can:

- edit metadata
- launch `Analyzers` and `Visualizers`
- link data to other projects
- export data.

On the right hand menu for this page, an `upload` button appears. This
launches an overlay with tabs for each type of TVB-compatible data:
    
    .. figure:: screenshots/data_uploaders.jpg
        :width: 90%
        :align: center
        
        The data upload overlay
    
Currently the data-types and/or structures supported for upload are:

* CFF connectome format
* Surface GIFTI
* TimeSeries GIFTI
* NIFTI
* RegionMapping
* TVB DataType
* Sensors
* Connectivity (zip)
* Upload Surface (zip)


Image Archive
.............

|TVB| provides you with the possibility of saving images snapshots.

From this page you can manage all the images stored within the current working 
`Project`, as well as:

  - edit figure title,
  - create categories to group your images,
  - search through your figure collection,
  - visualize, download and delete your images.

.. note::

  Only the current project figures will be available. If you want to visualize 
  images from another project, you will have to switch to that project.


    .. figure:: screenshots/project_image_archive.jpg
        :width: 90%
        :align: center
        
        The Image Archive page
