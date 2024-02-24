import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('test.png')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY) 
ret, thresh2 = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV) 
ret, thresh3 = cv2.threshold(img, 220, 255, cv2.THRESH_TRUNC) 
ret, thresh4 = cv2.threshold(img, 220, 255, cv2.THRESH_TOZERO) 
ret, thresh5 = cv2.threshold(img, 220, 255, cv2.THRESH_TOZERO_INV) 

cv2.imshow('test.png', img)
cv2.imshow('testGrayscale.png', grayImg)
cv2.imshow('threshold1', thresh1)
cv2.imshow('threshold2', thresh2)
cv2.imshow('threshold3', thresh3)
cv2.imshow('threshold4', thresh4)
cv2.imshow('threshold5', thresh5)
cv2.waitKey(0)
cv2.destroyAllWindows()