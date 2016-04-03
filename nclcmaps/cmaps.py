import numpy as N
import os
from matplotlib.colors import ListedColormap


def _coltbl(name):
    cmaps_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'colormaps')
    cmap_file = os.path.join(cmaps_dir, name+'.rgb')
    rgb = N.loadtxt(cmap_file, skiprows=6)
    rgb = rgb[1:-1]
    rgb = rgb/255
    return rgb


def cmaps(name):
    rgb = _coltbl(name)
    cmap = ListedColormap(rgb, name=name)
    return cmap
