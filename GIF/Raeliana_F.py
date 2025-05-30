# import imageio.v3 as iio
#
# filenames = ["flower1.jpg", "flower2.jpg", "flower3.jpg"]
# images = [ ]
#
# for filename in filenames:
#   images.append(iio.imread(filename))
#
# iio.imwrite('Raeliana_Flower.gif', images, duration = 500, loop = 0)
#
#
# import os
# print(os.getcwd())  # This prints the current working directory



import imageio.v3 as iio
import numpy as np

filenames = ["flower1.jpg", "flower2.jpg", "flower3.jpg"]
images = []

# Load images
for filename in filenames:
    img = iio.imread(filename)
    print(f"{filename} shape:", img.shape)
    images.append(img)

# Find a common size (use the first image's shape as standard)
target_shape = images[0].shape

# Resize images that don't match
def resize_image(img, target_shape):
    from PIL import Image
    pil_img = Image.fromarray(img)
    pil_img = pil_img.resize((target_shape[1], target_shape[0]))  # width, height order
    return np.array(pil_img)

for i in range(len(images)):
    if images[i].shape != target_shape:
        print(f"Resizing {filenames[i]} from {images[i].shape} to {target_shape}")
        images[i] = resize_image(images[i], target_shape)

# Now save GIF
iio.imwrite('Raeliana_Flower.gif', images, duration=1500, loop=0)
print("GIF saved successfully!")
