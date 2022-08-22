from PIL import Image

file_name = "MonaLisa.jpg"
img = Image.open(file_name)
img.show()

colors = img.getpixel((320, 240))

print(colors)