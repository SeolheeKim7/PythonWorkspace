from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")  # sample.xlsx file open
ws = wb.active  # active sheet

# ws.delete_rows(8)  # 8th row deleted
# ws.delete_rows(8, 3)  # 8th row deleted, 3 rows
# wb.save("sample_delete_rows.xlsx")

# ws.delete_cols(2)  # B column deleted
ws.delete_cols(2, 2)  # B column deleted, 2 columns
wb.save("sample_delete_cols.xlsx")
