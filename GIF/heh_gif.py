import imageio.v3 as iio

filenames = [ "heh1.PNG", "heh2.PNG"]
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('heh.gif', images, duration = 500, loop = 0)


import os
print(os.getcwd())

