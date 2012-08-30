Background
----------
.. historical considerations

The Virtual Brain provides a neuroinformatics platform, which allows the simulation of large-scale brain network dynamics. The brain connectivity of TVB distinguishes region-based and surface-based connectivity. In the former case, the networks comprise discrete nodes and connectivity, in which each node models the neural population activity of a brain regions and the connectivity is composed of interregional fibers. Region based networks contain typically 30 to 200 network nodes. In the latter case, cortical and subcortical areas are modelled on a finer scale by 5000 to 150 000 points, in which each point represents a neural population model. This approach allows a detailed spatial sampling in particular of the cortical surface resulting in a spatially continuous approximation of the neural activity known as neural field modelling (`Wilson Cowan 1972`_; `Nunez 1974`_, `Amari 1978`_; `Jirsa Haken 1996`_; `Robinson 1997`). Here the connectivity is composed of local intracortical and global intercortical fibers. When simulating brain activity in the simulator core of TVB, then the neural source activity time courses from both region or surface-based approaches are projected into EEG, MEG and  BOLD (blood oxygen level dependent contrast) space using a forward model (`Breakspear Jirsa 2007`_). The first neuroinformatic integration of these elements has been performed by (`Jirsa et al 2002`_) demonstrating neural field modelling in an event related paradigm. Homogeneous connectivity along the lines of (`Jirsa Haken 1996`_) was implemented. Neural field activity was simulated on a spherical surface for computational efficiency and then mapped upon the convoluted cortical surface with its gyri and sulci. The forward solutions of EEG and MEG signals have been computed and showed that a surprisingly rich complexity is observable in the EEG and MEG space, despite simplicity in the neural field dynamics. In particular, neural field models (`Wilson Cowan 1972`_; `Nunez 1974`_, `Amari 1978`_; `Jirsa Haken 1996`_; `Robinson 1997`_) have a spatial symmetry in their connectivity, which is always reflected in the symmetry of the resulting neural source activations, even though it may be significantly less apparent (if at all) in the EEG and MEG space.  This led the authors to conclude that the integration of tractographic data is imperative for future large-scale brain modelling attempts, since the symmetry of the connectivity will constrain the solutions of the neural sources, but not trivially show itself in the other imaging spaces of EEG, MEG and Bold. 



Multi-scale dynamics : large-scale brain models with local mesoscopic dynamics
------------------------------------------------------------------------------


The brain contains :math:`10^{11}` neurons linked by :math:`10^{15}` connections, with each neuron having inputs in the order of :math:`10^{5}`. The complex and highly-nonlinear neuronal interaction patterns are only poorly understood and the number of degrees of freedom of a microscopic model attempting to describe every neuron, every connection and every interaction is astronomically large and therefore far too high for fitting it directly with recorded macroscopic data. The gap between the microscopic sources of scalp potentials at cell membranes and the recorded macroscopic potentials can be bridged by an intermediate mesoscopic description. Mesoscopic dynamics describe the activity of populations of neurons organized as cortical columns or subcortical nuclei. Several features of mesoscopic and macroscopic electric behaviour, e.g., dynamic patterns like synchrony of oscillations or evoked potentials, show good correspondence to certain cognitive functions, e.g., resting-state activity, sleep patterns or event related activity. 

Common assumptions in mean-field modelling are that explicit structural features or temporal details of neuronal networks (e.g. spiking dynamics of single neurons) are irrelevant for the analysis of complex mesoscopic dynamics and the emergent collective behaviour is only weakly sensitive to the details of individual neuron behaviour (`Breakspear Jirsa 2007`_). Basic mean field models capture changes of the mean firing rate (`Brunel Wang 2003`_), where as more sophisticated mean field models account for parameter dispersion in the neurons and the subsequent richer behavioural repertoire of the mean field dynamics (`Assisi et al 2005`_; `Stefanescu Jirsa 2008`_, 2011; `Jirsa Stefanescu 2010`_). These approaches demonstrate the relatively new concept from statistical physics that macroscopic physical systems obey laws that are independent of the details of the microscopic constituents they are built of (`Haken 1972`_). These and related ideas have been exploited in neurosciences (`Kelso 1995`_; `Buzsaki 2006`_). Thus, our main interest lies in deriving the mesoscopic laws that drive the observed dynamical processes at the macroscopic scale in a systematic manner.



.. figure:: images/local_source_node_network.jpg
   :scale: 50 %
   :alt: a scheme of a local source node network

   Figure :counter:`figure`. Schematic of the local source node network architecture underlying mean field modelling.
 
   Excitatory (red circles) and inhibitory (black squares) neurons occupy a volume (left). 
   Couplings are indicated by black connecting lines. Conceptually both neuron types can be 
   clustered in two subpopulations (middle). Each subpopulation can be then characterized 
   by a mean behaviour under certain conditions  (right) and a mean connectivity (:math:`K_{11}`, :math:`K_{21}`, :math:`K_{12}`). 
   (Figure courtesy (`Stefanescu Jirsa 2008`_)).


Noninvasive neuroimaging signals constitute the superimposed representations of the activity of many sources leading to high ambiguity in the mapping between internal states and observable signals, i.e., the pairing between internal states of the neural network and observed neuroimaging signals is surjective, but not bijective. As a consequence, the EEG and MEG backward solution is underdetermined (`Helmholtz 1853`). Therefore, a crucial step towards the outlined goals is the correct synchronization of model and data, that is, the alignment of model states with internal - but often unobservable – states of the system.


Various mean-field models are available in |TVB| simulator reproducing typical features of mesoscopic population dynamics. 
For each node of the large-scale network, a neural population model describes the local dynamics.

When traversing the scale to the large scale network, then each network node is governed by its own intrinsic dynamics superimposed with the dynamics of all other network nodes that are each connected via specific connection weights and time delays yielding the following (generic) evolution equation for the time course of the network mean-field potential at node:


.. math::
    \dot{u_{i}} = g(u_{i}, v_{i}) - c \sum_{j=1}^{N} f_{ij} u_{j}(t - \Delta t_{ij}) + \sum_{k=1}^{P} \gamma_{ik}\, u_{k} + n_{u}

.. math::
    \dot{v_{i}} = h(u_{i}, v_{i}) + n_{v}


The equation describes the stochastic differential equation of a network of connected neural populations. The large-scale network is described by connection weights :math:`f_{ij}` where index :math:`j` indicates the weight of node exerting an influence on the node indexed by :math:`i`. The local network connectivity is described by connection weights :math:`\gamma_{ik}`.  
The time delays depend on a distance matrix :math:`d_{ij}` and a constant conduction speed :math:`\nu`, consequently :math:`\Delta t_{ij}=\frac{d_{ij}}{\nu}`. Weights are scaled by a constant :math:`c`. Additive noise is introduced by the terms :math:`n_{u}` and :math:`n_{v}`.

.. todo: Cross reference to coupling functions within reference manual and why?


A 2D GENERIC OSCILLATOR
~~~~~~~~~~~~~~~~~~~~~~~ 

This choice is motivated by various reasons, but foremost by the fact that a wide range of neuron models can be described by the a 2D dynamic system and that (`Stefanescu Jirsa 2008`_) have shown that population models of such neuron models preserve the mathematical form of the single neuron equations. 2D generic oscillator models generate a wide range of phenomena as observed in neuronal population dynamics such as multistability, coexistence of oscillatory  and non-oscillatory behaviors, various behaviors displaying multiple time scales, to name just a few. 

.. insert figure of different scenarios with trajectories
.. 