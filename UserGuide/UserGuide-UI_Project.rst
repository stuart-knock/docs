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
    - Operations
    - Data Structure
    - Project Properties
    - Saved Figures
    
    .. figure:: screenshots/project_area.jpg
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
    
    .. figure:: screenshots/data_description.jpg
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

On the right hand menu for this page, an `upload` buttons appear. This
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


Project Properties
...................

Enables you to edit the current project's properties, you are also directed
to this page when you first create a new project:
    
    .. figure:: screenshots/project_form.jpg
        :width: 90%
        :align: center
        
        The Project Properties page
        
    .. note::
        
        You can also access this page for any existing project by clicking the
        edit button near a projects name on the "View All Projects" page.
    
The central element of this page is a form where a project's name
(*without spaces*) should be defined and a short description should be
given. When other users are registered in the framework, you can choose to
share the project with other users by checking their respective "Visible
for" boxes. Then save changes by clicking on the `Save` button located on
the right side and to get back to the "View All Projects" page. If you were
creating a new project it should now be visible.

The right hand menu for this page also provides a way of exporting or
deleting the project.


Saved Figures
..............

This page displays all the figures saved by clicking `Save Figure` button in
the top right me

.. #TODO: need to add a figure here, and maybe more description.nu on the visualization pages.


