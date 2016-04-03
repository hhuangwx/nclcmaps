import numpy as np
import os
import re
from matplotlib.colors import ListedColormap


def _coltbl(name):
    cmaps_dir = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), 'colormaps')
    cmap_file = os.path.join(cmaps_dir, name+'.rgb')
    pattern = re.compile(r'\s*(\d[\d\.]*)\s+(\d[\d\.]*)\s+(\d[\d\.]*).*')
    with open(cmap_file) as cmap:
        cmap_buff = cmap.read()
    if re.search(r'\s*\d\.\d*', cmap_buff):
        return np.asarray(pattern.findall(cmap_buff), 'f4')
    else:
        return np.asarray(pattern.findall(cmap_buff), 'u1')/255.


def cmaps(name):
    rgb = _coltbl(name)
    cmap = ListedColormap(rgb, name=name)
    return cmap
