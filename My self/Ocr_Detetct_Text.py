#!/usr/bin/env python
# coding: utf-8

# In[1]:


import easyocr
import cv2

# Load the captured image
img_path = "captured_images/captured_image.jpg"
img = cv2.imread(img_path)

# If img is None
if img is None:
    exit()

# Define the reader with the languages and GPU option
reader = easyocr.Reader(['en'], gpu=True)

# Perform OCR on the image
result = reader.readtext(img)

# If no text is detected, print message
if len(result) == 0:
    print("No text detected in the image.")
else:
    # Extract and save the detected text to a file
    with open("extracted_text.txt", "w") as file:
        print("Detected text:")
        for detection in result:
            text = detection[1]
            print(text)
            file.write(text + "\n")
    print("Detected text saved to 'extracted_text.txt'")

