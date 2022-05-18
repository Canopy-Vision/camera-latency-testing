import cv2

img = cv2.imread('hardhat.png')

# screen_res = 1280, 720
# scale_width = screen_res[0] / img.shape[1]
# scale_height = screen_res[1] / img.shape[0]
# scale = min(scale_width, scale_height)
# window_width = int(img.shape[1] * scale)
# window_height = int(img.shape[0] * scale)

cv2.namedWindow('hardhat', cv2.WINDOW_NORMAL)
cv2.moveWindow('hardhat', 2000, 50)
cv2.resizeWindow('hardhat', 1080, 1080)

cv2.imshow('hardhat', img)
cv2.waitKey(0)
cv2.destroyAllWindows()