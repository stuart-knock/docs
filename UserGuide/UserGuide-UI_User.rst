User
----

TVB Settings
.............

Once started, |TVB| should automatically open your default browser and start on the
default `http://127.0.0.1:8080/settings/settings`. If not, you should manually open your favorite browser from our list of supported browsers and open the before mentioned URL. This should open up the following settings page:

.. figure:: screenshots/settings.jpg
   :width: 90%
   :align: center

   Settings Page

These are the configurable settings for |TVB|. Note that the `Name` of the administrator
is the only one that cannot be changed later on. The others will be accessible afterward
from the profile page of the administrator. These settings are:

Administrator User Name:
	the name of the administrator.

Password:
	the password of the administrator. This can be changed later by clicking the
	`Change password` link from the profile page.

Administrator Email:
	the email of the administrator. Emails requesting validations for new users will
	be sent to this address. This can be changed by clicking the `edit` link from the
	profile page.

Root folder for all projects:
	this is the root storage for |TVB|. All your projects will be stored here, as well
	as the logging file and the files used as input and output for the backend server.
	Please provide here a valid folder path, on a drive which has enough space for storing TVB data.
	This field will be present on the settings page later on, but you won't be able to change it.
	In case you are forced to change this path/folder, we recommend that you export your 
	existing projects, stop |TVB|, start it with clean option (and configure new folder)
	then import your projects back in the system.

Max Disk Size (in MB):
	Is the amount of disk space that you (as administrator) can specify as limit for each user, 
	to occupy with TVB Data. When a user exceeds this limit, he is no longer allowed to run simulations 
	or other operations producing data. When this limit is exceeded, the user will still be able to 
	visualize his previously created data, and, if desired, to remove data for making space for new results.
	A default region level simulation with length 1000 ms takes approximatively 1 MB of disk space.
	A surface level simulation, with Local Connectivity pre-computed, Raw monitor and length of 10 ms takes 280 MB.

DB engine:
	currently supported are *sqlite* and *postgresql* databases. You will need to provide a
	valid database URL in case you choose postgresql. In the case of sqlite a default
	`tvb-database.db` will always be used. Please take into consideration that when
	switching to a new database **your existing data will be lost**.

Server name:
	usually the IP of the server that will run |TVB|. You can also leave it to the default
	if you are just running |TVB| locally.

Cherrypy port:
	the port used by cherrypy. You need to make sure this port is not used by some other
	application otherwise |TVB| will not start.

Matplotlib port:
	the port used by matplotlib. You need to make sure this port is not used by some other
	application otherwise some visualizers will not work.

Deploy on cluster:
	set true if you want to run |TVB| on a cluster environment.

RPC server:
	if you are not running on a cluster, this will be the port used by the backend server. If
	`Deploy on cluster` is checked this will not be used.

Maximum number of vertices: 
	maximum number of vertices for a surface. 


After selecting your desired settings press the `Apply` button. This will restart |TVB| with the
new settings. The restart could take a few minutes.


Register
.........

If you want to create a new user, you should `register` using the `new account
link` which gives the following form:


.. figure:: screenshots/register.jpg
   :width: 90%
   :align: center

   |TVB| register page


When the `register` button is clicked, an email is sent to `ADMINISTRATOR_EMAIL`
address. This is the administrator's task to validate the new account. The
administrator needs to be logged in to validate an account.


This area is where you login and logout of |TVB|. 
It also provides some basic information, such as:

- what version of |TVB| you are currently running, 
- a summary of recent changes to |TVB| software and
- availability of updated versions of |TVB|.

.. figure:: screenshots/user.jpg
   :width: 90%
   :align: center

   The User details page

