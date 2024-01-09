# QR Code Generator with Centered Number

This script generates a QR code for a specified URL and overlays a one or two-digit number in the center. The generated QR code is saved as a PNG file with a naming convention based on the specified location and number.

The problem this script is trying to solve is organizing plastic garage bins for storage.  The contents of each bin is put in a docx file in a dropbox folder with an assigned 01-99 number.  This makes searching for a specific item easy.  The link to each doc is then used to generate the QR code.  The code then gets printed and taped to the outside of the bin.  This allows you to also easily scan the bin to view the contents without having to pull it down.  As the contents of the bins get added/removed/change, the document each of the QR codes points to can be updated as needed.

## Requirements

- Python 3
- Pillow library
- qrcode library

You can install the required libraries using pip:

```bash
pip3 install Pillow qrcode
```

## Usage

To use the script, you need to pass three mandatory arguments:
1. The URL to encode in the QR code.
2. A one or two-digit number to display in the center of the QR code.
3. A location identifier for the filename of the saved QR code.

Additionally, there are two optional arguments for customization:
- `--font-size <size>`: Specify the font size for the number. Default is 100.
- `--padding <size>`: Specify the padding around the number. Default is 10.

The script can be executed from the command line as follows:

```bash
python3 script.py <url> <two-digit-number> <location> [--font-size <size>] [--padding <size>]
```

### Examples

To create a QR code for the URL `https://example.com` with the number `42` in the center and save it with the location identifier `office`, you would run:

```bash
python3 script.py "https://example.com" "42" "office"
```

This command generates a QR code saved as `QR-office-42.png`.

To additionally customize the font size to 150 and padding to 20, the command would be:

```bash
python3 script.py "https://example.com" "42" "office" --font-size 150 --padding 20
```

## Help

If you need assistance with the script's usage, you can use the following command:

```bash
python3 script.py help
```

This will display detailed usage instructions.

## Customization

- The script uses the Helvetica font for the centered number. Ensure the font is available on your system or modify the script to use a different font.
- The font size and padding around the number can be customized using the optional `--font-size` and `--padding` arguments.
