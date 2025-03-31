# The spatial spread and the persistence of gene drives are affected by demographic feedbacks, density dependence and Allee effects

## Introduction

Artificial gene drive is a genetic engineering technology that could be used for the control of natural populations. Gene drive alleles bias their own transmission and can therefore spread in a population within a relatively small number of generations, even if they are deleterious. Understanding the potential outcomes of this technology, including the modification and/or the eradication of a natural population, is essential before real-world applications are considered. Here is the code used to simulate the spatial and temporal spread of gene drive alleles in the population in the article "The spatial spread and the persistence of gene drives are affected by demographic feedbacks, density dependence and Allee effects".

## Authors

This code was written by Léna Kläy. The project was carried out in collaboration with Vincent Calvez, Florence Débarre and Léo Girardin.

## Abstract of the article

Homing gene drive alleles bias their own transmission by converting wild-type alleles into drive alleles. If introduced in a natural population, they might fix within a relatively small number of generations, even if they are deleterious. No engineered homing gene drive organisms have been released in the wild so far, and modelling is essential to develop a clear understanding of the potential outcomes of such releases. We use deterministic models to investigate how different demographic features affect the spatial spread of a gene drive. Building on previous work, we first consider the effect of the intrinsic population growth rate on drive spread. We confirm that including demographic dynamics can change outcomes compared to a model ignoring changes in population sizes, because changes in population density can oppose the spatial spread of a drive.  Secondly, we study the consequences of including an Allee effect, and find that it makes a population more prone to eradication following drive spread. Finally, we investigate the effects of the fitness component on which density dependence operates (fecundity or survival), and find that it affects the speed of drive invasion in space, and can accentuate the consequences of an Allee effect. These results confirm the importance of checking the robustness of model outcomes to changes in the underlying assumptions, especially if models are to be used for gene drive risk assessment.

## Contents

This repository contains various folders:

1) `Functions` contains the code to run the simulations (.py), as well as a `README.rmd` file detailing each function,

2) `Outputs` stores the results of the simulations.

3) `Migale` contains the code to run the heaviest simulations on the cluster Migale (INRAE, doi: 10.15454/1.5572390655343293E12) as well as some outputs of previous simulations.

5) `Mathematica` contains the mathematica files used in preliminary mathematical analyses.

