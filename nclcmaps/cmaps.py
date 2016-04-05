import numpy as np
import os
import glob
import re
from matplotlib.colors import ListedColormap

CMAPSDIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'colormaps')


def _coltbl(name):

    cmap_file = os.path.join(CMAPSDIR, name+'.rgb')
    pattern = re.compile(r'(\d\.?\d*)\s+(\d\.?\d*)\s+(\d\.?\d*)\n')
    with open(cmap_file) as cmap:
        cmap_buff = cmap.read()
    if re.search(r'\s*\d\.\d*', cmap_buff):
        return np.asarray(pattern.findall(cmap_buff), 'f4')
    else:
        return np.asarray(pattern.findall(cmap_buff), 'u1')/255.


def listname():
    cmapsflist = sorted(glob.glob(CMAPSDIR+'/*.rgb'))
    for fname in cmapsflist:
        print(os.path.basename(fname)[:-4])


def cmaps(name):
    rgb = _coltbl(name)
    cmap = ListedColormap(rgb, name=name)
    return cmap
