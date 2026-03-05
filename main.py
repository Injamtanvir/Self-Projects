import qrcode

inp = input("Enter the URL to encode in the QR code: ")
img = qrcode.make(inp)
type(img)
img.save("qrcode.png")
print("QR code generated and saved as 'qrcode.png'")