#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:13:08 2021

@author: lena
"""

# This is annoying : 
# for i in np.linspace(0.1,1,10) : 
# print(i)    
# different from :
# np.linspace(0.1,1,10)


######################### Librairies and functions ############################

# Load libraries
import matplotlib.pyplot as plt

# Load functions
from evolution import evolution, evolution_2D
from heatmap import load_heatmap, heatmap, print_heatmap        

# Change font to serif
plt.rcParams.update({'font.family':'serif'})


############################ What to do ? #####################################

# possible choices for what_to_do : 
# "evolution" "evolution 2D"  "heatmap"

what_to_do = "evolution 2D"


######################### General parameters ##################################


### General parameters

## Biological
r = 0.1                               # intrinsic growth rate
s = 0.9                               # fitness disadvantage for drive
h = 0.9                               # dominance coefficient
c = 0.85                              # conversion rate
conversion_timing = "germline"        # "zygote" or "germline"
# Eradication : r = 1, s = 0.52, h = 0.6, c = 0.85  (condition extinction drive only : s > r/(r+1))

# Particular growth/death terms
model = "BN"
# Details (a : allee effect coefficient)
if model == "BN" : growth_dynamic = "logistical"; death_dynamic = "constant"; a = -1  # a not taken into acount in case a (but I use a=-1 it in the persistent line, heatmap.py)
if model == "BA_pos": growth_dynamic = "allee_effect"; death_dynamic = "constant"; a = 0.2
if model == "BA_neg": growth_dynamic = "allee_effect"; death_dynamic = "constant"; a = -0.2
if model == "DN" : growth_dynamic = "constant"; death_dynamic = "logistical"; a = -1  # a not taken into acount in case c (but I use a=-1 it in the persistent line, heatmap.py)
if model == "DA_pos" : growth_dynamic = "constant"; death_dynamic = "allee_effect"; a = 0.2
if model == "DA_neg" : growth_dynamic = "constant"; death_dynamic = "allee_effect"; a = -0.2

# Diffusion
difWW = 1; difDW = 1; difDD = 1    # diffusion coefficient for resp. WW, WD or DD individuals

## Numerical
CI = "center"                      # Initial conditions : "center" for having the border in the center, "left" for having the border on the left
T = 1000                           # final time
L = 1000                           # length of the spatial domain
M = T*6                            # number of time steps
N = L                              # number of spatial steps
theta = 0.5                        # discretization in space : theta = 0.5 for Crank Nicholson, theta = 0 for Euler Explicit, theta = 1 for Euler Implicit  
    
## Save outputs
save_fig = True                    # Save the figures (.svg and .png) 


### Parameters specific for each what_to_do

## Evolution
graph_type = "Allele densities"                          # "Genotype densities", "Genotype frequencies", "Allele densities" or "Allele frequencies" (or None if we don't want any evolution graph fct of time)
show_graph_ini = False                                   # Show graph at time 0
show_graph_end = True                                    # Show graph at time T
wild = True; heterozygous = True; drive = True            # What to draw on the graph
grid = True                                               # A grid or not
semilogy = False                                          # semilogy = False : classical scale, semilogy = True : log scale for y
xlim = None                                               # x scale on the graph (xlim = None, means it's not specify)
mod = T//5                                                # Draw graph every ..mod.. time. Also used to know when tracking points in time graphics.
## Evolution 2D
CI_lenght = N//4
 

## Heatmap
x = "s"; y = "r"     # Heatmap axes
rlog = True          # r in log scale or not (when y = "r")
precision = 50       # Number of value on s and r scale for the heatmap
load = True          # do we load the datas (True) or create them (False)
migale = False       # if True, the datas come from migale cluster (stored in "migale/heatmaps"), if false they come frome "outputs/heatmaps"
vmin = 1; vmax = 2   # Range min and max for the heatmap colour scale
if what_to_do == "heatmap" :
    graph_type = None; show_graph_ini = False; show_graph_end = False    
                     

#################### Group parameters for lisibility ##########################
        
bio_para = [r,s,h,difWW,difDW,difDD,c,conversion_timing,model,a,growth_dynamic,death_dynamic]
num_para = [CI,T,L,M,N,theta,[vmin,vmax]]
graph_para = [wild, heterozygous, drive, mod, grid, semilogy, xlim, graph_type, show_graph_ini, show_graph_end, save_fig]

############################### Main program ##################################

## Evolution
if what_to_do == "evolution" :
    print("\nwhat_to_do =", what_to_do); print("conversion_timing =", conversion_timing); print("\nh =", h); print("c =", c); print("r =", r); print("s =", s)
    W, H, D, time, speed = evolution(bio_para, num_para, graph_para)
    print("\nspeed :", speed[-1])   
  
    
## Evolution 2D
if what_to_do == "evolution 2D" :
    print("\nwhat_to_do =", what_to_do); print("conversion_timing =", conversion_timing); print("\nh =", h); print("c =", c); print("r =", r); print("s =", s)
    W, H, D, time, speed = evolution_2D(bio_para, num_para, graph_para, CI_lenght)
    print("\nspeed :", speed[-1])  
 
       
## Heatmaps
if what_to_do == "heatmap" :
        # Parameters
        T = 500; L = 2000; M = T*6; N = L; CI = 'center'
        # Update parameters
        num_para = [CI,T,L,M,N,theta,[vmin,vmax]] 
        bio_para = [r,s,h,difWW,difDW,difDD,c,conversion_timing,model,a,growth_dynamic,death_dynamic]
        # Obtain the heatmap values                       
        if load : 
            heatmap_values, coex_values = load_heatmap(bio_para, rlog, precision, migale, x, y)
        else :
            heatmap_values = heatmap(bio_para, num_para, graph_para, rlog, precision, x, y)            
        # Print heatmap
        print_heatmap(heatmap_values, bio_para, num_para, rlog, precision, x, y, f"{model}") 

        