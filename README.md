Title: E-Voucher Generation System for Traffic Light Violations

Description:
For my final year project, I developed an innovative E-Voucher Generation System aimed at automating the detection and penalization of traffic light violations. This project leverages computer vision and optical character recognition (OCR) technologies to identify vehicles that run red lights, capture their license plate information, and automatically generate a challan (e-voucher) in PDF format.

Project Overview:

Detection and Capture: The system detects vehicles violating traffic signals using a live camera feed or uploaded images.
License Plate Recognition: Once a violation is detected, the system focuses on the license plate area, extracting the relevant text using OCR techniques.
Automation: After capturing the license plate number, the system saves the text in a structured format (text file).
Challan Generation: Using the extracted license plate information, the system generates an e-challan in PDF format, streamlining the process of issuing fines for traffic violations.
Key Features:

Real-time Detection: Utilizes live camera feeds to detect vehicles that run red lights.
Image Upload Option: Allows users to upload images for processing, providing flexibility in data input.
Accurate OCR: Employs advanced OCR techniques to accurately extract text from license plates.
Automated E-Challan Generation: Generates e-challans in PDF format, reducing manual effort and increasing efficiency.
User Interaction: Provides options to save the license plate data and generate the e-challan with a simple click of a button.
Technologies Used:

Python: For overall development and scripting.
OpenCV: For image processing and computer vision tasks.
Pytesseract: For optical character recognition (OCR) to read license plate text.
ReportLab: For generating PDF files of the e-challans.
How It Works:

Detection: The system captures images via a webcam or accepts uploaded images.
License Plate Extraction: It isolates the license plate area from the captured image.
Text Extraction: Using OCR, the system reads and extracts the text from the license plate.
Data Storage: The extracted text is saved in a text file for record-keeping.
Challan Generation: The system reads the text file and generates an e-challan in PDF format, ready for issuance.
Impact and Benefits:
This project not only automates the process of detecting and penalizing traffic violations but also enhances the accuracy and efficiency of law enforcement agencies. By reducing the manual effort involved in generating challans, it allows authorities to focus more on maintaining road safety and enforcing traffic laws.
