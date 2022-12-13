from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

img = Image('gatito.jpg')
ws.add_image(img, 'E2')

img2 = Image('pez.jpg')
img2.anchor = 'M2'
ws.add_image(img2)

wb.save('04imgAnimal.xlsx')
