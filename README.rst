nclcmaps
========

Usage::

    import matplotlib.pyplot as plt
    import nclcmaps
    import numpy as np

    a=np.random.rand(100,100)
    plt.pcolormesh(a,cmap=nclcmaps.cmaps('BlueDarkOrange18'))
    plt.colorbar()
    plt.show()