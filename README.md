# QR Code Generator with Centered Number

This script generates a QR code for a specified URL and overlays a two-digit number in the center. The generated QR code is saved as a PNG file with a naming convention based on the specified location and number.

## Requirements

- Python 3
- Pillow library
- qrcode library

You can install the required libraries using pip:

```bash
pip3 install Pillow qrcode
```

## Usage

To use the script, you need to pass three arguments:
1. The URL to encode in the QR code.
2. A two-digit number to display in the center of the QR code.
3. A location identifier for the filename of the saved QR code.

The script can be executed from the command line as follows:

```bash
python3 script.py <url> <two-digit-number> <location>
```

### Example

To create a QR code for the URL `https://example.com` with the number `42` in the center and save it with the location identifier `office`, you would run:

```bash
python3 script.py "https://example.com" "42" "office"
```

This command generates a QR code saved as `QR-office-42.png`.

## Help

If you need assistance with the script's usage, you can use the following command:

```bash
python3 script.py help
```

This will display detailed usage instructions.

## Customization

- The script uses the Helvetica font for the centered number. Ensure the font is available on your system or modify the script to use a different font.
- You can adjust the font size and the padding around the number by modifying the corresponding values in the script.
