#  Importing the BAR Code module
from barcode import Code128
from barcode.writer import ImageWriter

# Enter the url or anytrhing which you want.
data = input("Enter anything which you want: ")  # Like: 0123456789

# convert BAR code to image
img = Code128(data, writer=ImageWriter())
img.save("barCode")