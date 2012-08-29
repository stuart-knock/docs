Large-scale brain dynamics practical implementation: |TVB| Simulator
====================================================================

.. links to the reference manual, include (maybe) only a short and compact and 'sciency' description

|TVB| simulator is a very specific type of scientific software: it is a 
**numerical software** and it has some distinguishable traits:

        1. It involves computations with floating point numbers.
        2. It involves large-scale simulations.
        3. Its requirements change rapidly, this is to say that the code must be flexible.

       
Simulating large-scale brain dynamics is a large-scale problem because, since we are mainly solving coupled ordinary and/or stochastic differential equations, it produces a massive amount of data (floating point numbers) waiting to be stored and quantified. 

* How large are brain dynamics computational tasks?

|TVB| performs region-based and surface-based simulations. In the former case, the networks comprise discrete nodes, in which each node models the neural population activity of a brain regions and the connectivity is composed of interregional fibers. Region based networks contain typically 30 to 200 network nodes, which is a coarse discretization. In the latter case, cortical and subcortical areas are modelled on a refined discretization by 5,000 to 150,000 points, in which each point represents a neural population model. 


.. Principles
.. well posedness of the problem -- (don't let the user do whatever he wants). 
.. numerical stability and efficiency
.. discretization --> spatial and temporal
.. flexibility --> So we should try to design the code to allow users to do different (but legitimate) things with our code. 
.. correctness --> bug-free and proof of correctness (unit test)
.. parallel computing
.. maximize the use of the underlying hardware. Cluster?

.. We have a large software system: we bring together pieces of software to solve larger problems. We do not write from scratch well known algorithms.

Goals and TODOs
~~~~~~~~~~~~~~~
.. Provided the problem we ask is well-posed. 

We want to answer questions that have not been answered before, to make use of the results to ask new questions and improve the functionality (new requirements) of our software.

- We have chosen numerically stable algorithms.
- Keep it simple. We do not want a monolithic system. |TVB| Simulator is composed by a few modules. 
- Testing and debugging. 
- A challenge: tune (learning tool) the scaling of the connectivity matrices to avoid having overflows (Inf, NaNs)


.. |TVB| : a Web-based scientific research tool
.. ============================================

.. Education, research and Information Technologies. 

