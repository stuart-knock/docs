# -*- coding: utf-8 -*-

"""
Make use of the phase plane interactive tool to generate phase-plane images
for the most significant scenarios (set of parameters) of the Generic2dOscillator 
model.

Figures are generated one at a time.

Usage:
   #From an ipython prompt in the images/ directory, with TVB in your python path
    run phase_plane_trajectories_Generic2dOscillator.py

Notes: `initial conditions` are the suggested starting points to generate 
a meaningful trajectory for a given set of parameters.

.. moduleauthor:: Paula Sanz Leon <Paula@tvb.invalid>

"""
# TODO: use the tester_factory. I'd like to draw sample trajectories for each phase
# plane so nice figures will be generated automatically. 
# NOTE: I'm thinking to move this script to contrib/simulator/demos, although 
# it is redundant 'cause in PhasePlaneInteractive there are clear instructions 
# on how to use it.

import numpy

import tvb.simulator.models
from tvb.simulator.phase_plane_interactive import PhasePlaneInteractive
import tvb.simulator.integrators
import tvb.simulator.noise

# stochastic integrator
hiss = tvb.simulator.noise.Additive(nsig = numpy.array([2**-10,]))
INTEGRATOR = tvb.simulator.integrators.HeunStochastic(dt=2**-5, noise=hiss)

# bistability (default set of parameters): fixed point and limit cycle
# initial conditions for the fixed point (-2.0, -5.0)  
# initial conditions for the limit cycle (1.0, 0.0)
# fixed point only if Iext = -2.0  and limit cycle only if  Iext = 1.0
MODEL_1 = tvb.simulator.models.Generic2dOscillator()
ppi_fig_1 = PhasePlaneInteractive(model=MODEL_1, integrator=INTEGRATOR)

# excitable
# initial conditions (-2.0, -5.0)
# if a is set to 2.0, we obtain a limit cycle
MODEL_2 = tvb.simulator.models.Generic2dOscillator(a=-2.0, b=-10.0, c=0.0, Iext=0.0)
ppi_fig_2 = PhasePlaneInteractive(model=MODEL_2, integrator=INTEGRATOR)

# SNIC bifurcation
# initial conditions (-2.0, -5.0)
# if b is set to 0.4 we obtain an oscillatory regime
MODEL_3 = tvb.simulator.models.Generic2dOscillator(a=0.5, b=0.6, c=-4.0, Iext=0.0)
ppi_fig_3 = PhasePlaneInteractive(model=MODEL_3, integrator=INTEGRATOR)


# show the figures
ppi_fig_1.show()
ppi_fig_2.show()
ppi_fig_3.show()
   