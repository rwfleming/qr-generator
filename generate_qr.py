import qrcode
from PIL import Image, ImageDraw, ImageFont
import sys

# Check if a URL and a number are passed as arguments
if len(sys.argv) < 3:
    print("Usage: python script.py <url> <two-digit-number>")
    sys.exit(1)

# The URL and the number are the first and second arguments passed to the script
url = sys.argv[1]
number = sys.argv[2]
location = sys.argv[3]

# Ensure the number is two digits
if len(number) != 2 or not number.isdigit():
    print("The number must be a two-digit number.")
    sys.exit(1)

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# Adding URL or text to QRcode
QRcode.add_data(url)

# Generating QR code
QRcode.make()

# Taking color name from user
QRcolor = 'Black'

# Adding color to QR code
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="white").convert('RGB')

# Create an ImageDraw object
draw = ImageDraw.Draw(QRimg)

# Set the font size and type
font_size = 100
font_path = "/System/Library/Fonts/Helvetica.ttc"
font = ImageFont.truetype(font_path, font_size, index=1)

# Alternative way to estimate text size
approximate_text_width = font.getmask(number).getbbox()[2]
approximate_text_height = font.getmask(number).getbbox()[3]

# Calculate text position
text_x = (QRimg.size[0] - approximate_text_width) // 2
text_y = (QRimg.size[1] - approximate_text_height) // 2

# Draw a white rectangle (box) behind the number
padding = 10
draw.rectangle(
    [text_x - padding, text_y - padding, text_x + approximate_text_width + padding, text_y + approximate_text_height + padding],
    fill="white"
)

# Draw the text on top of the white box
draw.text((text_x, text_y), number, fill="black", font=font)

# Generate the filename
filename = f'QR-{location}-{number}.png'

# Save the QR code generated
QRimg.save(filename)

print('QR code generated!')
