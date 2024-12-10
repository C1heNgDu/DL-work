import cv2

# 读取图像
image = cv2.imread('D:\\AIM-LAB\\pigmentRing\\3-1.bmp', cv2.IMREAD_GRAYSCALE)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))


clahe_image = clahe.apply(image)
save_path = "D:\\AIM-LAB\\pigmentRing\\3-1-c.bmp"
cv2.imwrite(save_path, clahe_image)
