import cv2

def compare_images(img1, img2):
    h1 = cv2.calcHist([img1],[0],None,[256],[0,256])
    h2 = cv2.calcHist([img2],[0],None,[256],[0,256])
    return cv2.compareHist(h1, h2, cv2.HISTCMP_CORREL)
