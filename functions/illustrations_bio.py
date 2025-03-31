#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:34:21 2023

@author: lena
"""

#import matplotlib
#import colorsys
#colorNames = list(matplotlib.colors.cnames.keys())

import matplotlib.pyplot as plt
import numpy as np

# Font and graph parameters 
plt.rcParams.update({'font.family':'serif'})
label_size = 12 
line_size = 2

# Models and parameters
what_to_do = "density_nd"   # "under_upper_boundary" or "density_nd"
model = "DA"   # "BN" or "BA" or "DN" or "DA" 
boundary = 'upper' # 'under' or 'upper'
a = -0.2   # Strengh of the Allee effect (only used for models BA and DA, for "density_nd")



## Print the extinction and bistability line for all possible a values
if what_to_do == "under_upper_boundary" : 
    fig, ax = plt.subplots() 
    s = np.linspace(0.0001, 0.9999, 2000)
    acolor=['navy','darkblue','royalblue','cornflowerblue','lightskyblue','greenyellow','gold', 'orange','red','crimson','purple']
    if model in ["BN", "DN"] :      
        ax.semilogy(s, s/(1-s), color='black', linewidth=line_size)
    if model in ["BA","DA"] :
        for i in range(11):
            a_list = np.round(np.linspace(-1,1,11)[i],2)
            A_list = ((1-a_list)/2)**2  
            if model == "BA" :  
                if boundary == "upper" : 
                    ax.semilogy(s, -s/(a_list*(1-s)), label=f"a={a_list}", color=acolor[i], linewidth=line_size, linestyle='-.')         
                if boundary == "under" : 
                    ax.semilogy(s, s/(A_list*(1-s)), label=f"a={a_list}", color=acolor[i], linewidth=line_size, linestyle='--')
            if model == "DA" :  
                if boundary == "upper" : 
                    s_under = s[np.where(s>-a_list)]; s_above = s[np.where(s<-a_list)]
                    ax.semilogy(s_under, -s_under/(a_list+s_under), label=f"a={a_list}", color=acolor[i], linewidth=line_size) 
                    ax.semilogy(s_above, -s_above/(a_list+s_above), color=acolor[i], linewidth=line_size)
                if boundary == "under" : 
                    s_under = s[np.where(s>A_list)]; s_above = s[np.where(s<A_list)]
                    ax.semilogy(s_under, s_under/(A_list-s_under), label=f"a={a_list}", color=acolor[i], linewidth=line_size)
                    ax.semilogy(s_above, s_above/(A_list-s_above), color=acolor[i], linewidth=line_size)            
    plt.legend()
    ax.set(xlabel='s (fitness disadvantage for drive)', ylabel="r (intrinsic growth rate)", xlim = (0,1), ylim = (0.01,10)) 
    ax.xaxis.label.set_size(label_size)
    ax.yaxis.label.set_size(label_size)     
    plt.grid()
    fig.savefig(f"../outputs/boundary/{model}_{boundary}_boundary.png", format='png')
    plt.show()


# Heatmap density n_D^*
if what_to_do == "density_nd" :
        precision = 1000
        res = np.zeros((precision,precision))
        s_values = np.linspace(0.01,0.99,precision)
        r_values = np.logspace(-2, 1, num=precision)
        for s_index in range(precision) :
            for r_index in range(precision) :
                s = s_values[s_index]
                r = r_values[r_index]
                if model == "BN" :
                    res[r_index, s_index] = 1 - s/(r*(1-s))
                if model == "BA" :
                    if (1+a)**2-4*(a+(s/(r*(1-s)))) < 0 : res[r_index, s_index] = -1
                    else : res[r_index, s_index] = 0.5*(1+a+np.sqrt((1+a)**2-4*(a+(s/(r*(1-s))))))
                if model == "DN" : 
                    res[r_index, s_index] = 1 - s*(r+1)/r
                if model == "DA" : 
                    if (1+a)**2-4*(a+(s*(r+1)/r)) < 0 : res[r_index, s_index] = -1
                    else: res[r_index, s_index] = 0.5*(1+a+np.sqrt((1+a)**2-4*(a+(s*(r+1)/r))))    
                if res[r_index, s_index] < 0 :
                    res[r_index, s_index] = np.nan
        fig, ax = plt.subplots()
        im = ax.imshow(res, cmap='YlGnBu', vmin=0, vmax=1)
        ax.figure.colorbar(im, ax=ax)  # Add the colorbar
        ax.set_xticks(np.linspace(0,precision,5)); ax.set_yticks(np.linspace(0,1,4)*(precision-1))    
        ax.set_xticklabels(np.linspace(0,1,5)); ax.set_yticklabels(np.around(np.logspace(-2, 1, num=4),2))  
        #ax.set_title(f"model = {model}, a = {a}, A = {A}")                 
        ax.set_xlabel("s (fitness disadvantage for drive)", fontsize=12) 
        ax.set_ylabel("r (intrinsic growth rate)", fontsize=12)
        plt.gca().invert_yaxis()  
        fig.tight_layout()
        if model == "BN" or model == "DN" :
            fig.savefig(f"../outputs/density/{model}.png", format='png')
        if model == "BA" or model == "DA" :
            fig.savefig(f"../outputs/density/{model}_a_{a}.png", format='png')
        plt.show()
    

