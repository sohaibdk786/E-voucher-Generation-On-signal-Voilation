import random
import datetime
from PIL import Image, ImageDraw, ImageFont

# Paths to files
image_path = r"C:\Users\Chaudhary\Desktop\My self\Pdf_Template.jpeg"
font_path = r"C:\Users\Chaudhary\Desktop\My self\Font\ArchivoBlack-Regular.ttf"
output_image_path = r"C:\Users\Chaudhary\Desktop\My self\modified_image.jpeg"
output_pdf_path = r"C:\Users\Chaudhary\Desktop\My self\generated_echallan.pdf"
text_file_path = r"C:\Users\Chaudhary\Desktop\My self\extracted_text.txt"

# Load the image
image = Image.open(image_path)
draw = ImageDraw.Draw(image)

# Load the font
font = ImageFont.truetype(font_path, size=20)
font_vehicle_no = ImageFont.truetype(font_path, size=24)  # Larger font for vehicle number

# Define coordinates for placing text (further adjusted)
coordinates = {
    'Notice Number:': (655, 142),  # Adjusted
    'Due Date:': (621, 167),      # Adjusted
    'Name:': (621, 190),          # Adjusted
    'Address:': (590, 215),       # Adjusted
    'DATE&TIME OF OFFENCE': (78, 338),  # Adjusted
    'VEHICLE NO': (708, 1092.5),     # Adjusted
}

# Function to calculate due date excluding weekends
def calculate_due_date(days):
    due_date = datetime.datetime.now()
    while days > 0:
        due_date += datetime.timedelta(days=1)
        if due_date.weekday() < 5:  # 0-4 are weekdays, 5-6 are weekends
            days -= 1
    return due_date

# Generate random and current data
notice_number = str(random.randint(1000, 9999))
due_date = calculate_due_date(7).strftime("%Y-%m-%d")
name = random.choice(['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown'])
address = random.choice(['123 Main St, Lahore', '456 Elm St, Lahore', '789 Oak St, Lahore', '101 Pine St, Lahore'])
current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Read vehicle number from the text file
with open(text_file_path, 'r') as file:
    vehicle_no = file.read().strip()

# Text to be placed
texts = {
    'Notice Number:': notice_number,
    'Due Date:': due_date,
    'Name:': name,
    'Address:': address,
    'DATE&TIME OF OFFENCE': current_datetime,
    'VEHICLE NO': vehicle_no,
}

# Place the text on the image
for key, coord in coordinates.items():
    if key == 'VEHICLE NO':
        draw.text(coord, texts[key], font=font_vehicle_no, fill="black")
    else:
        draw.text(coord, texts[key], font=font, fill="black")

# Save the modified image as JPEG
image.save(output_image_path)

# Convert the image to PDF using PIL
image.convert('RGB').save(output_pdf_path, "PDF", resolution=100.0)

print(f"PDF generated and saved to {output_pdf_path}")
