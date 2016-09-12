from PIL import Image
filename = "test-house.png"
img = Image.open(filename)
new_img = img.resize((256,256))
new_img.save('test-house-256x256','png')
new_img.show()