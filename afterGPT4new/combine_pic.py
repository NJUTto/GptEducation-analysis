import numpy as np
import matplotlib.pyplot as plt

# Load and combine images
img1 = plt.imread('./topic_pic/title/Paper-3.png')
img2 = plt.imread('./topic_pic/title/Paper-4.png')

# Combine images horizontally
combined_img = np.concatenate((img1, img2), axis=1)

# Save combined image
plt.imsave('./topic_pic/combine/Paper.png', combined_img)