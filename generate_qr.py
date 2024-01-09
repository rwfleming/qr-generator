import qrcode
from PIL import Image, ImageDraw, ImageFont
import sys

def print_help():
    help_message = """
    Usage: python script.py <url> <two-digit-number> <location> [options]
    
    Arguments:
    - <url>: The URL to be encoded in the QR code.
    - <two-digit-number>: A one or two-digit number to display in the center of the QR code.
    - <location>: The location identifier for the filename of the saved QR code.

    Options:
    - --font-size <size>: Optional. Specify the font size for the number. Default is 100.
    - --padding <size>: Optional. Specify the padding around the number. Default is 10.

    Example: python script.py "https://example.com" "42" "office" --font-size 150 --padding 20
    This will generate a QR code for "https://example.com" with "42" in the center, saved as "QR-office-42.png", with a font size of 150 and a padding of 20.
    """
    print(help_message)

# Check for help
if len(sys.argv) < 4 or sys.argv[1].lower() in ["help", "-h", "--help"]:
    print_help()
    sys.exit(1)

# Parse arguments
url = sys.argv[1]
number = sys.argv[2]
location = sys.argv[3]

# Default values for optional arguments
font_size = 100
padding = 10

# Parsing optional arguments
for i in range(4, len(sys.argv)):
    if sys.argv[i] == '--font-size' and i+1 < len(sys.argv):
        font_size = int(sys.argv[i+1])
    if sys.argv[i] == '--padding' and i+1 < len(sys.argv):
        padding = int(sys.argv[i+1])

# Ensure the number is one or two digits
if not (number.isdigit() and 1 <= len(number) <= 2):
    print("The number must be a one or two-digit number.")
    sys.exit(1)

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# Adding URL or text to QRcode
QRcode.add_data(url)

# Generating QR code
QRcode.make()

# Assigning QR color
QRcolor = 'Black'

# Adding color to QR code
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="white").convert('RGB')

# Create an ImageDraw object of the number
draw = ImageDraw.Draw(QRimg)

# Set the font type
font_path = "/System/Library/Fonts/Helvetica.ttc"
font = ImageFont.truetype(font_path, font_size, index=1)

# Estimate text size
approximate_text_width = font.getmask(number).getbbox()[2]
approximate_text_height = font.getmask(number).getbbox()[3]

# Calculate text position
text_x = (QRimg.size[0] - approximate_text_width) // 2
text_y = (QRimg.size[1] - approximate_text_height) // 2

# Draw a white rectangle (box) behind the number
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

print(f'QR code generated and saved as {filename}!')
