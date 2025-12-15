import pyqrcode

url = input("Enter the url: ")

qr = pyqrcode.create(url)

qr.png(
    "qrcode.png",
    scale=6,
    module_color=(255, 0, 0),
    background=(255, 255, 255)
)
print(qr.terminal())
print("QR code saved as qrcode.png")