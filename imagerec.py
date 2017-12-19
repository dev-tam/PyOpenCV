#!/usr/bin/python2.7
# import Image
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

i = Image.open('images/dot.png')
iar = np.asarray(i)

# print iar

plt.imshow(iar)
plt.show()