Large-scale brain dynamics practical implementation: |TVB| Simulator
====================================================================

.. links to the reference manual, include (maybe) only a short and compact and 'sciency' description

|TVB| simulator is a very specific type of scientific software: it is a 
** numerical software ** and it has some distinguishable traits:

        1. It involves computations with floating point numbers.
        2. It involves large-scale simulations.
        3. Its requirements change rapidly, this is to say that the code must be flexible.


       
Simulating large-scale brain dynamics is a large-scale problem because, since we 
are mainly solving coupled ordinary and/or stochastic differential equations, 
it produces a massive amount of data (floating point numbers) waiting to be 
stored and quantified. 

How large are brain dynamics computational tasks?
Think about the whole brain scale: we can use a coarse discretization and 
represent each brain region as a node (CROSSREF: region based simulations). 
However if we wish to have a more detailed comprehension of the dynamics within 
a specific region, or in plane of the cortical surface then we should 
refine discretization (CROSSREF: region based simulations)


.. The brain connectivity of TVB distinguishes region-based and surface-based connectivity. In the former case, the networks comprise discrete nodes and connectivity, in which each node models the neural population activity of a brain regions and the connectivity is composed of interregional fibers. Region based networks contain typically 30 to 200 network nodes. In the latter case, cortical and subcortical areas are modelled on a finer scale by 5,000 to 150,000 points, in which each point represents a neural population model. 






.. Principles
.. well posedness of the problem -- (don't let the user do whatever he wants). 
.. numerical stability and efficiency
.. discretization --> spatial and temporal
.. flexibility --> So we should try to design the code to allow users to do different (but legitimate) things with our code. 
.. correctness --> bug-free and proof of correctness (unit test)
.. parallel computing
.. maximize the use of the underlying hardware. Cluster?

We have a large software system: we bring together pieces of software to solve larger problems. We do not write from scratch well known algorithms.

- Provided the problem we ask is well-posed. We want to answer questions that have not been answered before, and make use of the results and our software to ask new questions and improve the functionality (new requirements) of our platform.
- We have chosen numerically stable algorithms.
- Modularization! Simplicity is better, we do not want a monolithic system. |TVB| Simulator is composed by modules. 
- Tested (as much as possible) the stability of the models. 
- A problem(challenge): tune the scaling of the connectivity matrices to avoid having overflows (Inf, NaNs)




