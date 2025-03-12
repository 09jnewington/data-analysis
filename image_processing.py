import numpy as np
import matplotlib.pyplot as plt

painting = plt.imread("image.png")

print(painting.shape)

painting = painting[:, ::-1]

plt.imsave("image_2.png", painting)


painting2 = painting.copy()    # don't mess the original painting!
painting2[0:30, :, :] = 1.0    # max value for all three components produces white


# Finding clusters in an image

n=5
l=256
im = np.zeros((l,l))
np.random.seed(0)
points = np.random.randint(0, l, (2, n**2))  # sample n*n pixels from the array im
im[points[0], points[1]] = 1
plt.imsave('random_points_image.png', im)