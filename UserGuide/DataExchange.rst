|TVB| Data Storage
==================

The purpose of this chapter is to provide some details about the way |TVB|
instance/installation can exchange data with other |TVB| instances, or with other applications
available in the neuroscience community. Currently, there are several applications that can analyze and record
brain activity in different formats, and one of the goals of |TVB| is to allow users from different backgrounds to have
quick access to their recorded data.

To achieve this, we have implemented some mechanisms to **IMPORT / EXPORT** data at different levels
and formats:

- **Project** - As you may know, |TVB| (TVB) data is organized in projects and one of the options is to transfer
  projects (with attached data) entirely between TVB installations. This mechanism can be used only between
  TVB applications, and no other external tools.

- **Simple Data** - This feature allows you to transfer independent data (e.g. surface, connectivity, time series)
  between two TVB instances or between TVB and an external application. As you may note later, depending on
  the targeted application, data can be exchanged in a custom TVB format or a commonly used format used in the neuroscience
  community (e.g. CFF, GIFTI, NIFTI ...)

|

**Important**

- During export and import operations |TVB| does not apply any space transformation, so users have to ensure their
  data (especially in case of import) is generated/stored in the same space.

.. raw:: pdf

   PageBreak oneColumn


Before proceeding with more details about data exchange, it would be helpful to give you an idea how
|TVB| stores its data. Basically there are two major storage areas:

1. *Database* - where general information/metadata are stored and relation between stored elements
   (e.g. assignment of data to a project, data metadata - creation date, owner, etc...)

2. *Disk* - here we store "the real" data in a HDF5 format (http://www.hdfgroup.org/HDF5). This means that for each data type (e.g. surface, connectivity, time series) we store on the disk, it is given a folder structure in an HDF5 / H5 file which contains all data (e.g. vertices, triangles ...). This format has the following advantages which made it an optimal solution for our product:

|        a. can store huge pieces of data and can access it very fast (even random access)
|        b. can organize data in a tree structure (groups and leaves)
|        c. allow assignment of metadata on every level
|        d. is a format agreed by the community and can be used/opened with different tools/languages   (Python, Matlab, java, C++ ...)

An important aspect of TVB storage is that each data/datatype has associated a GUID, which makes it
unique on every system where that data exists.



Exchange Projects
-----------------

TVB product can be installed both on a server, to be used concurrent by multiple users, but also as a
standalone application on a desktop/laptop for personal use. Specifically for the second scenario, there
was an important request to allow people to exchange data. So, TVB has a mechanism to export and
import an entire project to another system.

Export Project
..............

Using TVB interface, any user can export their projects in a custom format that can be transferred to other
users.


File Format
~~~~~~~~~~~

Export results are a ZIP file (named: date + project name), containing in a folder structure,
all the details about the project. More specifically, it contains:

|    a) A root level XML file with details about the project itself
|    b) Folders for each operation performed as part of the project
|    c) Operation folder contains an XML file with details of the operation and a set of H5/HDF5 files for
        each data type generated during that operation.

*Note*: each of the H5 files has a structure as described above in "TVB Storage" section.

|
|


Import Project
..............

A project exported on one system can now be imported on another machine. In the projects
area, TVB offers the possibility to import a project packed as ZIP file.


File Format
~~~~~~~~~~~

To import a project, user has to provide a ZIP with the same structure like the one described above for
'Export Project'.

**Important**: The same project cannot be imported multiple times on the same machine, because each
project/data has a unique identifier (GUID).


.. raw:: pdf

   PageBreak oneColumn

Export/Import Data
------------------

Apart from exchanging projects between TVB instances, there is another option to transfer data, but at a
lower level - that is to exchange only data types (generated during 'Simulation' or 'Analyze').



Export Data
...........

Using TVB interface, users can view all data types associated with a project and choose to export any of
them in different formats. Below you can see supported export formats and file formats for each of them.



Export Data in TVB Format
~~~~~~~~~~~~~~~~~~~~~~~~~

This export operation results in a file with a format specific to TVB; it is not a
standard format that can be used automatically by other software. This is basically HDF5/H5 format
[`http://www.hdfgroup.org/HDF5 <http://www.hdfgroup.org/HDF5>`_] which, for each data type, contains
both data and metadata. These files can be easily opened in Python / Matlab / Java / C++ or
additional processing.

In case you want to process HDF5 files with Matlab you can find API documentation here:
http://www.mathworks.com/help/techdoc/ref/f16-5702.html#f16-15000

.. NOTE:: The HDF5 functionality referenced above was only introduced in Matlab 2011a.


File Format
***********

As a result of a Simulation or Analyze function, TVB can generate either a data type or a group of data
types. Each of such structures can be exported as follows:

|     a.if a simple data type is exported, the result is an HDF5 file which has a root node datatype
        metadata and leaves the real data.
|     b. if a data type group is exported, the result is a ZIP file containing:

|          - at root level, an XML file with the details of the operation that generated the data types
|          - a list of HDF5 files, one for each data type included in the exported group. Each file has
             structure/details as described above in the case of simple data type export.
             *This format applies to any TVB data type.*



Export Data in CIFTI Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This operation is not implemented yet. The goal is to generate a CIFTI file according to format described here:

http://www.nitrc.org/projects/cifti/


File Format
***********

Will be defined when export implemented.


.. raw:: pdf

   PageBreak oneColumn


Import Data
...........

Probably this is the most important feature of data exchange, since it allows TVB to bring together data
generated independently by other systems/applications and allows it's users to perform different analyses
on it and visualize them. Since there is an abundance of formats available for neuroimaging data, TVB tries to support as
many as possible for an improved user experience.


Import Data in TVB Format
~~~~~~~~~~~~~~~~~~~~~~~~~

In correlation with export operations, TVB interface allows import of data in TVB format that has been exported from other
systems. This format applies to any TVB data type. Depending on the uploaded file format, imported
data can be as follows:


File Format
***********

1. If user uploads a ZIP file, the system automatically assumes a datatype group must be imported and
   then process the file accordingly. More specifically, it tries to find an XML file, within the ZIP file,
   describing the operation(s) that generated the data types and thelist of HDF5 files for each datatype.

2. If user uploads a simple HDF5/H5 file, the system assumes that a simple data type is imported and tries
   to process the file accordingly. Basically it reads the metadata stored in the root node group and determines the
   data type (e.g. connectivity, time series ...). Based on the detected type of data, the rest of the details are
   filled and the object is stored in the database.

|
|

Import Volume Time Series from NIFTI-1 Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NIFTI [http://www.nitrc.org/projects/nifti ] is a standard format maintained by "The Neuroimaging
Informatics Technology Initiative (NIfTI) and NIfTI Data Format Working Group" and allows the exchange of data
with different meanings (imaging data, statistical values, etc.; stored as vectors, matrix, label set or mesh).
NIFTI data can be stored in <.nii> or <.hdr+.img> files, or any of these in zipped format (<.gz> files).

For the moment, TVB accommodates import of Volume Time Series from NIFTI files.


File Format
***********

For import, TVB users can upload either .nii or .gz files containing NIFTI data in the format specified by
[http://www.nitrc.org/projects/nifti]

|
|

Import Sensors
~~~~~~~~~~~~~~

TVB allows users to import data about sensors used for brain imaging. More specifically, TVB supports three
types of sensors: EEG, MEG and INTERNAL. During the import process, the user has to select a file to import and
the type of the imported sensors. Based on the selected type, the data from the uploaded file will be processed
accordingly.


File Format
***********

During import, the user might upload either a TXT file or a zipped TXT in bz2 format. This TXT file should
contain data separated by spaces and grouped as follows:

1. each line contains details of a sensor
2. for each sensor there are four or seven columns

|        a. first column represents the name / label of the sensor
|        b. next three columns represents the position of sensor (x, y, z)
|        c. next three columns (if present) represents the orientation of sensor. These are required only for MEG sensors.


|
|

Import Connectivity from ZIP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature allows import of connectivity from a ZIP file. The ZIP should contain files with connectivity details as
follows:

File Format
***********

ZIP file should include files with the following naming schema and format:

1. If any file name contains "weight", it will be considered as the container for connectivity weights and the parse
process expects the following format:

|        a. text file containing values separated by spaces / tabs
|        b. contains a matrix of weights

2. If any file name contains "position" it will be considered as the container for connectivity
   centers and the parse process expects the following format:

|        a. text file containing values separated by spaces / tabs
|        b. on the first row there should be the labels/description of each column
|        c. each row represents data for a region center
|        d. each row should have at least 4 columns: region label and center position (x, y, z)

3. If any file name contains "tract" it will be considered as container for connectivity tract lengths and
   the parse process expects the following format:

|        a. text file containing values separated by spaces / tabs
|        b. contains a matrix of tract lengths

4. If any file name contains "orientation" it will be considered as container for connectivity center
   orientations and parse process expects the following format:

|        a. text file containing values separated by spaces / tabs
|        b. each row represents orientation for a region center
|        c. each row should have at least 3 columns for region center orientation (3 float values separated with spaces or tabs)

5. If any file name contains "area" it will be considered as container for connectivity areas and
   the parse process expects the following format:

|        a. text file containing one area on each line (as float value)

|
|

Import Surface from ZIP
~~~~~~~~~~~~~~~~~~~~~~~

Using this option, users have the possibility to import a surface from a more human readable
format into TVB. Basically users have to upload a zip file containing surface data and specify what type of surface
they upload (Cortical Surface, Brain Skull, Skull Skin or Skin Air).

File Format
***********

Uploaded ZIP file should contain files with a specified naming schema and format as follow:

1. If any file name contains "vertices" it will be considered as container for surface vertices
   and parse process expects the following format:

|        a. this is a space separated values file
|        b. each row represents position of a vertex
|        c. each row should have three columns (x, y, z as float values)

2. If any file name contains "normals" it will be considered as container for surface vertices normals and
   parse process expects the following format:

|        a. this is a space separated values file
|        b. each row represents a vertex normal
|        c. each row should have three columns (with float values)

3. If any file name contains "triangles" it will be considered as container for surface triangles and
   parse process expects the following format:

|        a. this is a space separated values file
|        b. each row represents a triangle
|        c. each row should have three columns (int values) - each value representing the index of a vertex
            from the vertices array. This indices could be ZERO based or not, depending on the source which
            generated the surface. This is the user is required to specify this at import time.

There are systems/applications that generate and store surface data in two parts: for left and right side.
If this is the case, the imported ZIP file is expected to contain text files with the same naming and format, but
the name should contain after prefix letter "r" or "l" (e.g. <trianglesl.txt> and <trianglesr.txt>)

|
|

Import Surface and TimeSeries from GIFTI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is a geometry format (http://www.nitrc.org/projects/gifti/) under the Neuroimaging Informatics Technology
Initiative (NIfTI) that allows exchange of brain data (surface, time series, shapes, labels ...)
Basically this is format XML based which stores both data and associated metadata in a single file, with .gii
extension.

If uploaded .gii file contains a surface (Cortical Surface or SkinAir) during import TVB stores found vertices
/ triangles and computes normals for them.

In case .gii file contains a TimeSeries, user will be asked to specify what is the surface for which TimeSeries
is imported. Important to know: number of vertices from imported time series must be the same like the
one of the selected surface. Otherwise import procedure will fail.

File Format
***********
This is a standard format, supported by a large community so all details about it and samples can be found here:
http://www.nitrc.org/projects/gifti


**Note**: At this moment |TVB| supports only import of data from a single .gii file. It does not handles cases
when metadata is defines in .gii (XML) file and real data in external files.

|
|

Import Data from CFF
~~~~~~~~~~~~~~~~~~~~

CFF (Connectome File) is a complex format that tries to put together all data necessary for brain
simulations or analysis. Because of its complexity and lack of support from the community, this format is not
used very often. For this reason, we decided to implement **import** only of a custom form of CFF, for demo
purposes.  Support for CFF import might be removed in the future versions.

The current |TVB| version includes a set of demo data, housed in a folder that contains
two CFF files which could be imported for testing.

Since CFF is a complex format you can use it for uploading single data (e.g one surface, connectivity, 
local connectivity, region mapping) but also you could group multiple such data into a single CFF file. 


File Format
***********

For this feature, the user has to upload a CFF file (which is basically a ZIP file) containing a root file <meta.cml>
which describes the content of the archive. This file specifies what data types are packed (e.g.
connectivity, surface, region mapping) and which files contain data for these types. In our demo data,
files are in different formats: starting from raw data (numpy dump), GIFTI, NXGPickle.
