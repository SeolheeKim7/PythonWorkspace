from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

img = Image("img.png")

ws.add_image(img, "C3")  # add image to C3 cell

wb.save("sample_image.xlsx")  # save
