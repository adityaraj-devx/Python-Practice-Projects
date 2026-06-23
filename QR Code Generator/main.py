import qrcode

link = input("Enter the text or URL: ").strip()
filename = input("Enter the filename: ").strip()

qr = qrcode.QRCode(box_size=12, border=4)

qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("some_file.png")

print(f"QR code has been created {filename}")