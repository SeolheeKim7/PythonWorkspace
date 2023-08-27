from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")  # sample.xlsx file open
ws = wb.active  # active sheet

# ws.insert_rows(8)  # 8th row inserted
# ws.insert_rows(8, 5)  # 8th row inserted, 5 rows
# wb.save("sample_insert_rows.xlsx")


# ws.insert_cols(2)  # B column inserted
ws.insert_cols(2, 3)  # B column inserted, 3 columns
wb.save("sample_insert_cols.xlsx")
