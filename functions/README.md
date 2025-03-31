# Functions

This folder contains all the code needed to run the deterministic simulations. 

## The `main.py` file

Most of the simulations are launched from the file `main.py`. All the parameters can be adjusted at the top of this file and the value of the variable `what_to_do` determine the type simulation ran:

1) `what_to_do = "evolution"` simulates the model. It plots screenshots of the traveling wave at different times in 1D space (some of them are used in Figure 1). The function used to simulate the system are written in `evolution.py` and the functions used to plot the graph are written in the `graph.py`.

2) `what_to_do = "evolution 2D"` simulates the model. It plots screenshots of the traveling wave at different times in 2D space. The function used to simulate the system are written in `evolution.py` and the functions used to plot the graph are written in the `graph.py`.

3) `what_to_do = "heatmap"` plot an heatmap representing the speed of the traveling wave function of two variables denoted `x` and `y` in the code. The possibilities are: i) `x = 's'` and `y == 'r'`, ii) `x = 'h'` and `y == 'r'` and iii) `x = 'h'` and `y == 's'`. Figure 4 shows the speed function of `s` and `r`. The functions used to simulate and plot the heatmap are written in `heatmap.py`.


## Other files `.py` that can be run independently

`illustrations_bio.py`: plots . If `what_to_do = "density_nd"`, the code plots the final drive densities (Figure2), if `what_to_do = "under_upper_boundary"` it plots the under or upper boundary lines (Figure 3).

`fig_rode_debarre_2019.py`: It plots Figures 13 and 14 from article <https://doi.org/10.1007/s00285-023-01926-4>.

