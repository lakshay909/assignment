import cv2
import numpy as np

path = '/Users/lakshaynarula/Desktop/Codes/Text and Visual analysis/IMG_0204.jpeg'
img = cv2.imread(path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, np.mean(gray), 255, cv2.THRESH_BINARY_INV)

# Get contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))

# Let's get the largest contour
cnt = sorted(contours, key=cv2.contourArea)[-1]

# Create a mask of the same size as the input image
mask = np.zeros_like(gray)

# Draw the largest contour on the mask
maskedFinal = cv2.drawContours(mask, [cnt], -1, (255, 255, 255), thickness=cv2.FILLED)

# Extract region of interest (ROI) from the original image based on the contour
x, y, w, h = cv2.boundingRect(cnt)
roi = img[y:y+h, x:x+w]

# Apply the mask to the ROI
masked_roi = cv2.bitwise_and(roi, roi, mask=maskedFinal[y:y+h, x:x+w])

# Create a white background image with the same shape as the original image
white_bg = np.full_like(img, (255, 255, 255), dtype=np.uint8)

# Replace the corresponding region of the white background with the masked ROI
white_bg[y:y+h, x:x+w] = masked_roi

cv2.imshow("Original", img)
cv2.imshow("Masked Final", maskedFinal)
cv2.imshow("Final Image", white_bg)

cv2.waitKey(0)
cv2.destroyAllWindows()
