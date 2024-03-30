#  Importing the QR Code module
import qrcode

# Enter the url or anytrhing which you want.
inputURL = input("Enter anything which you want: ")  # like: "https://www.google.com"

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 10,
)

qr.add_data(inputURL)
qr.make(fit = True)

# convert QR code to image
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")

# print the data
print(qr.data_list)