import numpy as np
import matplotlib.pyplot as plt

# Load and combine images
img1 = plt.imread('./pic/作业+答题问答+原创性.png')
img2 = plt.imread('./gpt4/pic_gpt4/作业+答题问答+原创性.png')

# Combine images horizontally
combined_img = np.concatenate((img1, img2), axis=1)

# Save combined image
plt.imsave('./combine_pic/作业+答题问答+原创性.png', combined_img)