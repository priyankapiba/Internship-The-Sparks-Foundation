from PIL import Image   # The Image  class is required so that we can load our input image from disk in PIL format, a requirement when using pytesseract
import pytesseract
import cv2
import os

image=cv2.imread('example_03.PNG')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)      # followed by converting it to grayscale .
# write the grayscale image to disk as a temporary file so we can apply OCR to it
filename = "{}.png".format(os.getpid())             # we use os.getpid  to derive a temporary image filename based on the process ID of our Python script
cv2.imwrite(filename, gray)
# load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
text = pytesseract.image_to_string(Image.open(filename))    #we convert the contents of the image into our desired string and store it in text
os.remove(filename)                                         #deleting the temporary file
print(text)
cv2.imshow("Image", image)
cv2.waitKey(0)
