from openpyxl import Workbook
wb = Workbook()  # create new file
ws = wb.active  # ctive sheet
ws.title = "ShSheet"  # sheet name change
wb.save("sample.xlsx")
wb.close()
