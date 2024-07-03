import cv2
import os
import sys
from tkinter import Tk, filedialog, Button, messagebox

def capture_from_camera():
    cap = cv2.VideoCapture(1)
    cap.set(3, 640)  # width
    cap.set(4, 480)  # height

    while True:
        success, img = cap.read()

        if not success:
            print("Failed to capture image")
            break

        plate_cascade = cv2.CascadeClassifier(harcascade)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

        for (x, y, w, h) in plates:
            area = w * h

            if area > min_area:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

                img_roi = img[y: y + h, x: x + w]
                cv2.imshow("ROI", img_roi)

        cv2.imshow("Result", img)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            # Save the captured image as "captured_image.jpg" in the captured_images folder
            cv2.imwrite(os.path.join(output_dir, "captured_image.jpg"), img_roi)
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
            cv2.imshow("Results", img)
            cv2.waitKey(500)

            # Release the capture and destroy windows
            cap.release()
            cv2.destroyAllWindows()

            # Exit the script
            sys.exit()

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
    if file_path:
        print(f"File path: {file_path}")
        img = cv2.imread(file_path)

        if img is None:
            print("Failed to load image")
            messagebox.showerror("Error", "Failed to load image")
            return

        print(f"Image dimensions: {img.shape}")

        plate_cascade = cv2.CascadeClassifier(harcascade)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

        img_roi = None
        for (x, y, w, h) in plates:
            area = w * h

            if area > min_area:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

                img_roi = img[y: y + h, x: x + w]
                cv2.imshow("ROI", img_roi)

        cv2.imshow("Result", img)

        if cv2.waitKey(0) & 0xFF == ord('s'):
            if img_roi is not None:
                # Save the captured image as "captured_image.jpg" in the captured_images folder
                cv2.imwrite(os.path.join(output_dir, "captured_image.jpg"), img_roi)
                cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
                cv2.imshow("Results", img)
                cv2.waitKey(500)

                # Exit the script
                sys.exit()
            else:
                messagebox.showerror("Error", "No number plate detected to save.")

        cv2.destroyAllWindows()

def main():
    # Create the GUI window
    root = Tk()
    root.title("Number Plate Detection")

    # Create buttons for each functionality
    capture_button = Button(root, text="Capture from Camera", command=capture_from_camera)
    capture_button.pack(pady=10)

    upload_button = Button(root, text="Upload Image", command=upload_image)
    upload_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    harcascade = "model/haarcascade_russian_plate_number.xml"
    min_area = 500
    output_dir = "captured_images"

    # Ensure the captured_images directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    main()
