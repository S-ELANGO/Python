import pyqrcode

#get the url from users
url=input("Enter the url:")

#generate the qr code 
qr=pyqrcode.create(url)
qr.svg("qrcode.svg",scale=5)

#show the qr code in terminal
print(qr.terminal())
