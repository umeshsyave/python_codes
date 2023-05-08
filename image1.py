from PIL import Image,ImageFilter

img=Image.open('leopard.jpg')
filters=img.filter(ImageFilter.FIND_EDGES)
new=img.convert('L')
filters.save('leopard1.png')
new.save('leopard2.png')


#print(img.format)
#print(img.size)
#print(img.mode)
#print(img.show())    opens image in photos application