from PIL import Image

filename = input("Enter the filename: ").strip()

img = Image.open(filename)
img.save("new_image.jpg", "JPEG", optimize=True, quality=50)

print(f"Compressed image has been saved {filename}")