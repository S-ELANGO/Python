import pyqrcode

#get the url from users
url=input("Enter the url:")

#generate the qr code 
qr=pyqrcode.create(url)
qr.svg(
     "qrcode.svg",
     scale=6,
     module_color=(255, 0, 0),      # Red QR
     background=(255, 255, 255)     # White background
)

#show the qr code in terminal
print(qr.terminal())
