Introduction
============

Overview
--------
.. abstract

.. include:: sci.report.abstract.rst


Motivation and Goals
-------------------- 

.. introduction

Non-invasive neuroimaging modalities like electroencephalography (EEG), magnetoencephalography, functional magnetic resonance imaging (fMRI) and positron emission tomography provide a macroscopic picture of neuronal dynamics, but fall short of identifying mesoscopic or microscopic brain dynamics such as population oscillations or neuronal spike trains. However, macroscopic signal features are thought to emerge from the interaction of neuronal populations, while the explicit mechanism – the neural code – still remains unclear. Instead of attempting to understand neuronal interactions in every detail, a reasonable first step is to reproduce functionally relevant dynamics using a large-scale network model that spans several salient brain regions each being equipped with a dynamical mathematical model that is able to capture relevant features of brain activity at the mesoscopic scale, i.e., the scale of cortical columns, nuclei and populations comprising up to several hundreds of neurons. 

A major goal of science is to express observed real world phenomena in terms of a testable mathematical model that is able to predict future events and that can be used for analyses of unobserved ‘hidden’ model parameters that cannot be directly measured but inferred from experimental data. Multi-modal neuroimaging captures different aspects of brain dynamics that can be related to cognitive states. However, up to now, only very few principles underlying the observed complex signal dynamics have been elucidated. 

Model-based integration of different neuroimaging modalities enables the exploration of consequences of biophysically relevant parameter changes in the system as they occur in changing brain states or during pathology. This in turn allows us to identify and counteract unfavourable processes in the brain and to promote beneficial processes. Hence we aim to uncover (i) fundamental neuronal mechanisms that give rise to typical features of brain dynamics and (ii) how inter-subject variability in brain structure results in differential brain dynamics.

In contrast to simple functional models that associate dependent variables with one or a few independent variables, brain dynamics are based on the complex nonlinear interaction of several independent subsystems. Model-based multi-modal data integration approaches have many advantages over conventional approaches like direct data-fusion or converging evidence (Horwitz and Poeppel 2002; Valdes-Sosa, Sanchez-Bornot et al. 2009).

Converging evidence is indicated when similar patterns of evidence are found in different imaging modalities pointing to the same conclusion. However, we neither understand the complex interaction of neural substrates nor the explicit relation between different imaging modalities or even the relation of individual modalities to their underlying generators. Therefore, it is almost impossible to determine when findings from different modalities are congruent and when not.

Direct data fusion aims for the direct comparison of data sets from different imaging modalities using mathematical or statistical assessment criteria. However, these approaches rest on the assumption of identical neuronal signal generators or that signals from different modalities have compatible features. Anyhow, the signals of spatio-temporal source activity patterns do not necessarily need to overlap in different modalities nor do high statistical correlations between activation levels need to point to the true site of the signal source (Schulz, Chau et al. 2004).

Model-based approaches, on the other hand, are able to integrate information from different modalities in a complementary manner, while avoiding limitations arising from pure statistical comparisons that do not account for the distinct underlying neurophysiological sources that generate the respective signals and potentially relate to different aspects of brain activity. Thus, in our view, the most reasonable way to integrate multimodal neuroimaging data together with existing knowledge about brain functioning and physiology is by means of a computational model that describes the emergence of high-level phenomena on the basis of basic bottom-up interaction between elementary brain processing units. Instead of modelling the interaction between abstract entities or concepts, the building blocks of our model are neurons respectively neural populations. We advocate the use of model building blocks that correspond to real neurophysiological entities as most useful for expanding our knowledge about the generation of simulated signals that show similar dynamics like actual neuroimaging signals. 





