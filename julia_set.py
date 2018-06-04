#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Image width and height; parameters for the plot
im_width, im_height = 1000, 1000
#alpha=np.pi
#c = complex(0.7885*np.cos(alpha),0.7885*np.sin(alpha))
zabs_max = 10
nit_max = 1000
xmin, xmax = -1.5, 1.5
xwidth = xmax - xmin
ymin, ymax = -1.5, 1.5
yheight = ymax - ymin


alpha = np.linspace(0,2*np.pi,300)
for k in range(160,300):
    print(k)
    c = complex(0.7885*np.cos(alpha[k]),0.7885*np.sin(alpha[k]))

    julia = np.zeros((im_width, im_height))
    for ix in range(im_width):
        for iy in range(im_height):
            nit = 0
            # Map pixel position to a point in the complex plane
            z = complex(ix / im_width * xwidth + xmin,
                        iy / im_height * yheight + ymin)
            # Do the iterations
            while abs(z) <= zabs_max and nit < nit_max:
                z = z**2 + c
                nit += 1
                shade = 1-np.sqrt(nit / nit_max)
                ratio = nit / nit_max
                julia[iy,ix] = ratio
    plt.figure(1)
    fig, ax = plt.subplots()
    ax.imshow(julia, interpolation="spline36",cmap=cm.RdGy,label=r"$c=0.7885e^{i%2.5f}$" %alpha[k])
    # Set the tick labels to the coordinates of z0 in the complex plane
    xtick_labels = np.linspace(xmin, xmax, xwidth / 0.5)
    ax.set_xticks([(x-xmin) / xwidth * im_width for x in xtick_labels])
    ax.set_xticklabels([xtick for xtick in xtick_labels])
    ytick_labels = np.linspace(ymin, ymax, yheight / 0.5)
    ax.set_yticks([(y-ymin) / yheight * im_height for y in ytick_labels])
    ax.set_yticklabels([ytick for ytick in ytick_labels])
    plt.title(r"Julia Set for $c=0.7885e^{i%2.5f}$" %alpha[k])
    plt.savefig("/home/stamatis/M.Sc_Computational_Physics/2nd_sem/Non_Linear_Dynamics/project/Julia_graphs/%s.pdf"% str(k),dpi=600)
    plt.clf()
    plt.close('all')
    
