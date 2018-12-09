import rawpy
import numpy as np
import cv2
import imageio
import copy as cp
import scipy.misc

# 加载图像，提取图像的大小维度
in_path = '0.ARW'
raw = rawpy.imread(in_path)
raw_image = raw.raw_image_visible
H = raw_image.shape[0]
W = raw_image.shape[1]

# 新建一个rgb三个图像通道
r_image = cp.deepcopy(raw_image)
g_image = cp.deepcopy(raw_image)
b_image = cp.deepcopy(raw_image)
for i in range(0, H, 2):
    for j in range(0, W, 2):
        r_image[i + 1][j] = raw_image[i][j]
        r_image[i + 1][j + 1] = raw_image[i][j]
        r_image[i][j + 1] = raw_image[i][j]

for i in range(0, H, 2):
    for j in range(0, W, 2):
        temp = raw_image[i + 1][j] / 2 + raw_image[i][j + 1] / 2
        g_image[i][j] = temp
        g_image[i + 1][j + 1] = temp
        g_image[i + 1][j] = temp
        g_image[i][j + 1] = temp


for i in range(0, H, 2):
    for j in range(0, W, 2):
        b_image[i + 1][j] = raw_image[i + 1][j + 1]
        b_image[i][j] = raw_image[i + 1][j + 1]
        b_image[i][j + 1] = raw_image[i + 1][j + 1]

rgb_image = cv2.merge([b_image, g_image, r_image])

rgb_image = im = np.maximum(rgb_image - 512, 0) / (16383 - 512)  # subtract the black level

rgb = raw.postprocess(use_camera_wb=True, half_size=False, no_auto_bright=True, output_bps=16)
imageio.imsave('source.tiff', rgb)  # 保存最佳格式

rgb = raw.postprocess()
imageio.imsave('default.tiff', rgb)  # 默认rawpy 处理效果


rgb_image = np.minimum(np.maximum(rgb_image, 0), 1)
scipy.misc.toimage(rgb_image * 255, high=255, low=0, cmin=0, cmax=255).save('rgb_image.jpg')  # 自定义方法处理效果


