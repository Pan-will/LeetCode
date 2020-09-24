"""
图像翻转的代码。
"""
import cv2

# 定义读取图片的路径
img_dir = "photo.jpg"
# 定义存储结果图片的路径
save_dir = ""
img = cv2.imread(img_dir)

# 水平镜像翻转
flip_horizontal = cv2.flip(img, 1)
# 垂直镜像翻转
flip_vertical = cv2.flip(img, 0)
# 对角镜像翻转
flip_hv = cv2.flip(img, -1)
# 保存处理后的图片
cv2.imwrite("save_path1.jpg", flip_horizontal)
cv2.imwrite("save_path2.jpg", flip_vertical)
cv2.imwrite("save_path3.jpg", flip_hv)
