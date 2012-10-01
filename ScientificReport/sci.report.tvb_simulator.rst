|TVB|: A large-scale brain modeling platform 
============================================

.. links to the reference manual, include (maybe) only a short and compact and 'sciency' description

.. We want to answer questions regarding the human brain that have not been 
   answered before. Results should enlighten the path to new questions that will 
   help us improve the performance of our software.


|TVB| project could have not existed without other previous open-source projects 
in the area of Neuroscience. And even though |TVB| is not the first computing 
tool in this community, from the technical and scientific point of view, |TVB| 
is unique in its modern and new access to the domain, and it is the first tool
for large-scale brain modeling. 

**How large are brain dynamics computational tasks?**

Simulating large-scale brain dynamics is a large-scale problem because, since 
we are mainly solving coupled ordinary and/or stochastic differential equations, 
it produces a massive amount of data (floating point numbers).


|TVB| performs region-based and surface-based simulations. In the former case, 
the networks comprise discrete nodes, in which each node models the neural 
population activity of a brain regions and the connectivity is composed of 
interregional fibers. Region based networks contain typically 30 to 200 network 
nodes, which is a coarse discretization. In the latter case, cortical and 
subcortical areas are modelled on a refined discretization by 5,000 to 150,000 
points, in which each point represents a neural population model.  


.. It will be open to learn from and to take advantage of new existing tools. 

The purpose of |TVB| then is to provide a customized computing platform for:

  - simulating and, 
  - analyzing

functional and structural data of human brains. The same degree of analysis is
applicable to both simulated and experimental data.


.. note::

    TVB is intended to be an open-source software-product, available for usage 
    in an on-line installation, but also available for download and install by 
    any interested person or institution.


Scientific Software Aspects
---------------------------

|TVB| is a very specific type of scientific software: it is a  
**numerical software** and it has some distinguishable traits:

        1. It involves computations with floating point numbers.
        2. It involves large-scale simulations.
        3. Its requirements change rapidly.

|

These characteristics lead us to have some core principles of design:

  - Accuracy
  - Reliability
  - Robustness
  - Efficient
  - Easy to use (usability)
  - Maintainability
  - Adaptability

and neuroscience specific functional requirements such as:

  - possibility to configure, execute and monitor large scale brain 
    **simulations**,
  - configure and execute **data analysis** algorithms and methods,
  - **visualize** brain input data and analysis results.

|

In addition to these characteristics, when using TVB, a researcher needs to 
have the freedom to:
 
    - configure simulations and data analysis techniques. 
    - both interfere with existing simulation or libraries for analysis
    - **configure the equations** (modeling) of the brain network model, and
    - be able to build his/her own libraries and to **plug** them into the |TVB|.


.. The extensions of functionality of TVB should be as easy as possible, which means as little coding as possible.


High-performance computing for parallel simulations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A common and expected use of TVB is the exploration of the local dynamics 
model parameter space. Hence TVB also runs on a high-performance cluster, 
accessible over web from anywhere. This enables the functionality of operating 
in batch mode, in which several simulations, one for each value of a given 
parameter, can be performed at the same time


.. The results will be captured in parametric maps of convenient measures and appropriately visualized.


.. A high priority objective is optimizing our software for high performance computing for advanced simulations.
.. Principles
.. well posedness of the problem 
.. numerical stability and efficiency
.. discretization 
.. flexibility --> So we should try to design the code to allow users to do different (but legitimate) things with our code. 
.. correctness --> bug-free and proof of correctness (unit test)
.. parallel computing
.. maximize the use of the underlying hardware. Cluster?

.. We have a large software system: we bring together pieces of software to solve larger problems. We do not write from scratch well known algorithms. 




.. TODO
.. a learning tool to compute the factor used to scale the connectivity matrix in order according to the selected Model. 

.. Questions to be answered -- from the computing / sci-software perspective

* Mathematical questions
  - How a new scientific software impacts the structure of mathematics? 
  - How new mathematical problems arise? 
  - How to measure the performance of our mathematical problem solving tools?

.. Requirements

Input Data 
~~~~~~~~~~

.. Associated data should be available.

Input data for TVB can be retrieved from multiple sources: functional 
neuroimaging like EEG, MEG, sEEG, fMRI and structural imaging such as MRI, DTI, 
DSI, but also data from the literature etc.

Stress testing is testing to see how well the algorithm behaves with large, 
extreme, or **degenerate inputs**. The key quantity to watch with stress testing is 
accuracy. 

.. Performance testing is about determining how the algorithm behaves with large-scale problems. 
.. The key quantities to watch with performance testing are time and memory usage.

Test Data
~~~~~~~~~
Test data can be useful as a check against most kinds of bugs and as a way to 
produce repeatable results, and to compare and contrast with new data. It also
useful for stress testing.


.. DO NOT INCLUDE THIS
   include:: sci.report.analysis.rst
