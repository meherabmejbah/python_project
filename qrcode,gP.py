import qrcode

data = input("Enter the Data you want to generate in a QR code (message,link etc): ")
qr = qrcode.make(data)
qr.save("Your_qrcode.png")
print("Done...Watch your file....")

