#using the pillow package
from PIL import Image

k=Image.open('download.jpeg')
b=k.convert('L')
b.save('blackandwhite.jpg')
k.show()
b.show()