from PIL import Image
im = r"bullet.PNG"
img = Image.open(im)

resized_im = img.resize((round(img.size[0]*0.5), round(img.size[1]*0.5)))

#Display the resized imaged
resized_im.show()

resized_im.save("bullet.PNG")
