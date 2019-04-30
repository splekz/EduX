import cv2


img = cv2.imread('simplesat.png')

cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)

cv2.imshow('dst_rt', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
