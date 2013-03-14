.. |TITLE| replace:: Contributors Manual
.. |DESCRIPTION| replace:: Provides a tutorial with the steps you need to take in order to start contributing into TVB aswell as a demo of using TVB in console mode.
.. |VERSION| replace:: 1.0
.. |REVISION| replace:: 0.1

.. include:: ../templates/pdf_template.rst   
      

.. Purpose:

.. To provide a step by step flow that will get TVB set-up and ready for contributions. 
.. To offer a short tutorial of how TVB can be used from a console script with storage activated as part of the full TVB framework.

.. Contents:
..   	GIT setup for contributors. 
		Contribution tutorial.
		Console mode usage with enabled storage.
.. Created and Maintained by: Developers. Should be updated in case any changes to contribution flow.


	GIT setup for contributors

The following steps assume you have the latest TVB package from www.thevirtualbrain.org. You also need to make sure you have a GIT client installed and available from command line. You can test this by trying to run git --version.

The official TVB Github repository can be found https://github.com/tvb-admin/tvb_scientific_library . The first step you need to do is fork this repository. You should now have your own Github clone. 

Now assuming you have your TVB distribution package in ~/TVB_Distribution. Go into the bin folder located at ~/TVB_Distribution/bin .

Depending on the operating system you are using open a terminal / command line prompt in this directory and the execute the following:

On linux: sh contributor_setup.sh ${github_url}

On windows: contributor_setup.bat ${github_url}

In the commands above replace ${github_url} with the url of your forked repositiory on github.

The steps above should create a folder ~/TVB_Distribution/tvb_scientific_library which contains the simulator, analyzers, basic and logger subfolders. This is the clone of your GIT forked repository and you are now ready to contribute to TVB!


	Contribution tutorial.

You should always create a separate branch with a self-explanatory name for the new features you want to add to TVB. In order to do this just (from ~/TVB_Distribution/tvb_scientific_library folder): git checkout my-awesome-new-feature . During feature development make sure you make pulls from master often in order to quickly fix any conflicts that might appear.

Once you are done with your changes and believe they can be integrated into TVB, go to your github repository, switch to your feture branch and issue a Pull Request describing the improvements you did. 

	
	Console mode usage with enables storage.
	
The TVB distribution package comes with a working IDLE based environment which you can use if this is more comfortable for you than using the Web Interface. You can start this from the same ~/TVB_Distribution/bin folder above by running sh tvb_console.sh / tvb_console.bat .

.. include:: console_storage_true.py

.. raw:: pdf

   PageBreak
