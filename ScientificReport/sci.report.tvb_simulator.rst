Large-scale brain dynamics practical implementation: |TVB| Simulator
=====================================================================

.. links to the reference manual, include (maybe) only a short and compact and 'sciency' description

.. Provided the problem we ask is well-posed. 

We want to answer questions that have not been answered before, to make use of the results to ask new questions and improve the functionality of our software.

|TVB| simulator is a very specific type of scientific software: it is a 
**numerical software** and it has some distinguishable traits:

        1. It involves computations with floating point numbers.
        2. It involves large-scale simulations.
        3. Its requirements change rapidly.

These characteristics lead us to have some core principles of design:

- Accuracy
- Reliability
- Robustness
- Efficient
- Easy to use (usability)
- Maintainability
- Adaptability

.. Principles
.. well posedness of the problem 
.. numerical stability and efficiency
.. discretization 
.. flexibility --> So we should try to design the code to allow users to do different (but legitimate) things with our code. 
.. correctness --> bug-free and proof of correctness (unit test)
.. parallel computing
.. maximize the use of the underlying hardware. Cluster?

.. We have a large software system: we bring together pieces of software to solve larger problems. We do not write from scratch well known algorithms. 

**How large are brain dynamics computational tasks?**

Simulating large-scale brain dynamics is a large-scale problem because, since we are mainly solving coupled ordinary and/or stochastic differential equations, it produces a massive amount of data (floating point numbers) waiting to be stored and quantified. 

|TVB| performs region-based and surface-based simulations. In the former case, the networks comprise discrete nodes, in which each node models the neural population activity of a brain regions and the connectivity is composed of interregional fibers. Region based networks contain typically 30 to 200 network nodes, which is a coarse discretization. In the latter case, cortical and subcortical areas are modelled on a refined discretization by 5,000 to 150,000 points, in which each point represents a neural population model. 


.. TODO
.. a learning tool to compute the factor used to scale the connectivity matrix in order according to the selected Model. 

.. Questions to be answered -- from the computing / sci-software perspective

* Mathematical aspects
 
How a new scientific software impacts the structure of mathematics? 
How new mathematical problems arise? 
How to measure the performance of our mathematical problem solving tools?

.. Requirements

* INPUT DATA: TEST DATA: STRESS TESTING: PREFORMANCE TESTING

.. Associated data should be available.

Stress testing is testing to see how well the algorithm behaves with large, extreme,or degenerate inputs. 
The key quantity to watch with stress testing is accuracy. 

Performance testing is about determining how the algorithm behaves with large-scale problems. 
The key quantities to watch with performance testing are time and memory usage.

Test data can be useful as a check against most kinds of bugs and as a way to produce repeatable results, and to compare and contrast results, etc ...